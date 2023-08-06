
# beves

beves is a simple wrapper to send messages with Telegram Bot. Useful to alert on something or to notify when scripts are finished!

Table of contents
=================

- Introduction

- Installing

- Getting started

- Usage

- References

- License

Introduction
------


This module provides a simple way to send messages with Telegram Bot. Is useful to notify you when scripts are finished.
You can import it into your code or using the command-line utility. In the command-line utility, beves
reads the message data as a parameter or from stdin.


Installing
------

You can install or upgrade beves with:

```bash
$ pip install beves --upgrade
```
Or you can install from source with:

```bash
$ git clone https://github.com/andremmorais/beves --recursive
$ cd beves
$ python setup.py install
```

Getting started
------

To use Beves you will need the bot token and the chat_id of the sender.

The token can be generated talking with @BotFather on telegram and the chat_id can checked at `https://api.telegram.org/bot<YourBOTToken>/getUpdates`

Initialize beves config

```bash
$ beves
Token: xxxxx
Chat ID: xxxxx
```
Run from command-line with message data as argv

```bash
$ sleep 5 && beves "sleep finished";
```
Run from command-line with message data from stdin

```bash
$ echo "this is a test message" | beves
```
Run from command-line passing token and chat_id as args

```bash
$ beves -t xxxxx -i xxx "this is a test message"
```
Importing into your code

```python
from beves import Beves
bot = Beves()
bot.push('test')
```
If you dont have the configuration you will need to pass them as arguments:

```python
from beves import Beves
bot = Beves('token', 'chat_id')
bot.push('test')
```

Usage
------

```bash
usage: beves [-h] [-t TOKEN] [-i CHAT_ID] [-c CONFIG] [-v] [--version]
             [message [message ...]]

Simple wrapper to send notifications with Telegram Bot

positional arguments:
  message               Message to send

optional arguments:
  -h, --help            show this help message and exit
  -t TOKEN, --token TOKEN
                        telegram bot token
  -i CHAT_ID, --chat_id CHAT_ID
                        sender chat id
  -c CONFIG, --config CONFIG
                        configuration file instead of
                        /Users/andre.morais/.beves
  -v, --verbosity       increase output verbosity
  --version             show program's version number and exit
```

References
------

- Telegram Bots <https://core.telegram.org/bots>
- Telegram API documentation <https://core.telegram.org/bots/api>
- python-telegram-bot documentation <https://python-telegram-bot.readthedocs.io/>

License
------

You may copy, distribute and modify the software provided that modifications are described and licensed for free under [LGPL-3](https://www.gnu.org/licenses/lgpl-3.0.html). Derivatives works (including modifications or anything statically linked to the library) can only be redistributed under LGPL-3, but applications that use the library don't have to be.

