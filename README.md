# Uwuifier Discord Bot

[![CodeQL](https://github.com/Electronic-Mango/philosopher-discord-bot/actions/workflows/codeql.yml/badge.svg)](https://github.com/Electronic-Mango/philosopher-discord-bot/actions/workflows/codeql.yml)
[![Black](https://github.com/Electronic-Mango/philosopher-discord-bot/actions/workflows/black.yml/badge.svg)](https://github.com/Electronic-Mango/philosopher-discord-bot/actions/workflows/black.yml)
[![Flake8](https://github.com/Electronic-Mango/philosopher-discord-bot/actions/workflows/flake8.yml/badge.svg)](https://github.com/Electronic-Mango/philosopher-discord-bot/actions/workflows/flake8.yml)

Bot uwuifiying your Discord conversations, built with [disnake](https://github.com/DisnakeDev/disnake) and [owoify-py](https://github.com/deadshot465/owoify-py).



## Table of contents

- [Requirements](#requirements)
- [Configuration](#configuration)
- [Commands](#commands)
  - [Message context commands](#message-context-commands)
  - [Slash commands](#slash-commands)
  - [Uwuifying all messages](#uwuifying-all-messages)
  - [Inspirational quotes](#inspirational-quotes)
- [Running the bot](#running-the-bot)
  - [From source](#from-source)
  - [Docker](#docker)
- [Why?](#why)



## Requirements

This bot was built using `Python 3.10`.
Full list of Python requirements is in `requirements.txt` file.



## Configuration

Bot loads its configuration from `.env` files.
Default `.env` file in the project root contains configuration parameters, all of which should be filled before the bot is started.
Some parameters already have default values, which you can tweak further.
Detailed description of each parameter is in the `.env` file itself.

Although, technically, only `DISCORD_BOT_TOKEN` parameter needs to be provided with your Discord bot token for the bot to start.
However, without other parameters bot might not behave as you'd expect.

All parameters can be overwritten by environment variables with the same name.

Default `.env` also defines parameter `CUSTOM_DOTENV`, which is a path to a separate `custom.env` file.
This custom file can also be used to overwrite values from the default one, without modifying project files.



## Required bot permissions

### Message content

This bot requires **message content privileged gateway intent** to function correctly.
This requirement comes from `previous` and `all` commands, which wouldn't be able to read message contents otherwise.

You can enable this content for the whole bot in [Discord Developer Portal](https://discord.com/developers/applications) and specific bot settings.

Currently bot won't even start without this privileged intent enabled.
You can remove this requirement by modifying `src/bot/bot.py` file and its `_prepare_intents()` function.
Currently this function creates `Intents` with message content privileged intent enabled:

```python
def _prepare_intents() -> Intents:
    intents = Intents().default()
    intents.message_content = True
    return intents
```

You can modify it to return default `Intents` instead:

```python
def _prepare_intents() -> Intents:
    return Intents().default()
```

**The bot will start, but `all` and `previous` commands won't function correctly.**


### Managing webhooks and messages

`all` command also required permissions to **modify channel webhooks** and **manage messages** to function correctly.

Without these permissions bot will start, however `all` command will return an ephemeral message with information that permissions are missing.



## Commands

### Message context command

This command is available from the context menu of selected message.

 * `uwuify this message` - uwuifies message which this command replies to, allowing for "targeted" uwuification


### Slash commands

These commands are available when you start typing `/`.

 * `/help` - prints help message
 * `/all` - uwuifies ALL messages sent in this channel (**available only in servers and with relevant bot permissions**)
 * `/this <text to uwuify>` - uwuifies text given as an argument to this command
 * `/previous` - uwuifies previous message in this channel (except this bot messages)
 * `/quote` - sends an inspirational uwuified quote


### Uwuifying all messages

Uwuifying all messages is done through a webhook.
When `all` command is executed a webhook is added to the channel.
This new webhook will have the same name and avatar as the bot.
Afterwards, when any message other than a command is send in this channel a uwuified version will be sent through this webhook.
This message will also have original author's name and avatar.
Original message is removed.

Decision whether to replace messages is done based on whether this webhook is present in channel.
No persistent data is stored on bot side.
This way bot will know which channel to uwuify even after it's restarted.

**This functionality is only available in servers and with relevant permissions**.


### Inspirational quotes

You can supply your API source for inspirational quotes via `.env` file.
You also need to specify via JSON key names which JSON values should be treated as quote text and which as quote author.



## Running the bot

You can run the bot from source, or in a Docker container.


### From source

1. Create a Discord bot
1. Install all packages from `requirements.txt`
1. Fill `.env` or `custom.env` or other custom configuration file
1. Execute `src/main.py` via Python


### Docker

1. Create a Discord bot
1. Fill `.env`
1. Run `docker compose up -d --build` in terminal

You can skip `--build` flag if you didn't change the source code.

`.env` is not added to the Docker image, just used as a source for environment variables.
So if you make any changes there, just restart the container.
There's no need to rebuild the image.

You can supply a custom `.env` by modifying `docker-compose.yml` and:

 * loading a custom `.env` file as a source of environment variables, just keep in mind that this file **MUST** exist
 * configuring `CUSTOM_DOTENV` environment variable to point to some custom `.env` file in a mounted volume, this file can be missing from the container, it just won't be loaded



## Why?

Why not?

Also this: https://austinhenley.com/blog/makinguselessstuff.html
