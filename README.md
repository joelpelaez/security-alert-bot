# Security Alert Bot

## Description

Discord bot for send notifications about security and erratas from multiple open source projects

Currently supporting:

 - Debian DSA
 - FreeBSD Security Advisories and Errata Notices (malfunctioning, see below)
 - FreeBSD VuXML (ports security announces)

This code is dual licensed under the [BSD 2-Clause 'Simplified' License](LICENSE) and
[GNU General Public License v3.0](COPYING).

This project will support extending with new bots platforms as Slack.

## Limitations

 - By now is only implementing Discord bot, but the code abstractions allows to add other bot implementations.
 - The current version only support one channel to send notifications, it will support multiple channels to send
notifications messages.
 - Some settings must be changed in [config.py](config.py) file directly instance of the environment variables.

## Notes

### FreeBSD Security Advisories and Errata Notices
Currently, the RSS source is not generating the correct data, it already was reported:
[FreeBSD Bugzilla #288511](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=288511).
