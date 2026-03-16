# SPDX-License-Identifier: BSD-2-Clause or GPL-3.0-only
#
# Copyright (c) 2026 Joel Pelaez Jorge.
# All rights reserved.
#
# This source code is licensed under both the BSD-style license (found in the
# LICENSE file in the root directory of this source tree) and the GPLv3 (found
# in the COPYING file in the root directory of this source tree).
# You may select, at your option, one of the above-listed licenses.

import logging

import discord

from domain.manager import Manager
from model.entry import Entry
from domain.bot import Bot


logger = logging.getLogger("bot.DiscordBot")


class DiscordBot(discord.Client, Bot):
    """Discord Bot class for send messages

    This is the Bot implementation for Discord platform, it allows to send messages
    to a specific channel.

    Attributes:
        token (str): Discord bot token
    """

    token: str
    _manager: Manager

    def __init__(self, token: str, channel_id: int):
        """Initialize Discord bot using a bot token and a target channel

        Args:
            token (str): Discord bot token
            channel_id (int): Discord bot channel ID
        """
        super().__init__(intents=discord.Intents.default())
        self.token = token
        self.channel_id = channel_id

    def register_manager(self, manager: Manager) -> None:
        """Register the manager to start when the bot is ready"""
        self._manager = manager

    async def on_ready(self):
        """Called when the bot is ready."""
        logger.info("%s has connected to Discord", self.user)
        if self._manager is not None:
            await self._manager.on_ready()

    async def on_disconnect(self):
        """Called when the bot is disconnected."""
        logger.info("%s has disconnected from Discord", self.user)
        if self._manager is not None:
            await self._manager.on_disconnect()

    async def on_resumed(self):
        """Called when the bot is resumed."""
        logger.info("%s has been resumed from Discord", self.user)
        if self._manager is not None:
            await self._manager.on_resumed()

    async def start_async(self):
        """Starts the bot on async mode.

        This method starts the bot using the async call.
        """
        async with self:
            await self.start(self.token, reconnect=True)

        # Terminate the manager
        await self._manager.on_terminate()

    async def send_formatted_message(self, entry: Entry) -> bool:
        try:
            channel = self.get_channel(self.channel_id)
            embed = discord.Embed(
                title=entry.title,
                description=entry.content,
                url=entry.link,
                type="rich",
            )
            message = await channel.send(embed=embed)
            return message is not None
        except TypeError:
            logger.error("message structure error", exc_info=True)
        except ValueError:
            logger.error("message size error", exc_info=True)
        except discord.NotFound:
            logger.error("message was deleted recently.", exc_info=True)
        except discord.Forbidden:
            logger.error(
                "target channel is not forbidden for sending messages", exc_info=True
            )
        except discord.HTTPException:
            logger.error("general HTTP error while sending message", exc_info=True)

        return False

    async def send_message(self, message) -> bool:
        try:
            channel = self.get_channel(self.channel_id)
            if channel is not None:
                message = await channel.send(message)
                return message is not None
        except TypeError:
            logger.error("message structure error", exc_info=True)
        except ValueError:
            logger.error("message size error", exc_info=True)
        except discord.NotFound:
            logger.error("message was deleted recently.", exc_info=True)
        except discord.Forbidden:
            logger.error(
                "target channel is not forbidden for sending messages", exc_info=True
            )
        except discord.HTTPException:
            logger.error("general HTTP error while sending message", exc_info=True)

        return False
