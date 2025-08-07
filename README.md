# Security Alert Bot (sec-alert-bot)

## Description

Discord bot for send notifications about security and erratas from multiple open source projects

Currently supporting:

 - Debian DSA
 - FreeBSD Security Advisories and Errata Notices (malfunctioning, see below)
 - FreeBSD VuXML (ports security announces)

This code is dual licensed under the [BSD 2-Clause 'Simplified' License](LICENSE) and
[GNU General Public License v3.0](COPYING).

## Notes

### FreeBSD Security Advisories and Errata Notices
Currently, the RSS source is not generating the right data, it already was reported.
