# Uwuifier Discord Bot

[![CodeQL](https://github.com/Electronic-Mango/philosopher-discord-bot/actions/workflows/codeql.yml/badge.svg)](https://github.com/Electronic-Mango/philosopher-discord-bot/actions/workflows/codeql.yml)
[![Black](https://github.com/Electronic-Mango/philosopher-discord-bot/actions/workflows/black.yml/badge.svg)](https://github.com/Electronic-Mango/philosopher-discord-bot/actions/workflows/black.yml)
[![Flake8](https://github.com/Electronic-Mango/philosopher-discord-bot/actions/workflows/flake8.yml/badge.svg)](https://github.com/Electronic-Mango/philosopher-discord-bot/actions/workflows/flake8.yml)

Bot uwuifiying your Discord conversations, built with [disnake](https://github.com/DisnakeDev/disnake) and [owoify-py](https://github.com/deadshot465/owoify-py).


## Table of contents
- [Requirements](#requirements)
- [Running the bot](#running-the-bot)
  - [From source](#from-source)
  - [Docker](#docker)
  - [Supplying configuration variables](#supplying-configuration-variables)
- [Commands](#commands)
  - [Uwuifying all messages](#uwuifying-all-messages)
  - [Inspirational quotes](#inspirational-quotes)
- [Why?](#why)


## Requirements
This bot was built using `Python 3.10`.
Full list of Python requirements is in `requirements.txt` file.


## Running the bot
You can run the bot from source, or in a Docker container.


### From source
1. Create a Discord bot
1. Install all packages from `requirements.txt`
1. Fill `.env`
1. Execute `src/main.py` via Python


### Docker
1. Create a Discord bot
1. Fill `.env`
1. Run `docker compose up -d --build` in terminal

You can skip `--build` flag if you didn't change the source code.

`.env` is not added to the Docker image, just used as a source for environment variables.
So if you make any changes there, just restart the container.
There's no need to rebuild the image.


### Supplying configuration variables
The default way of supplying required configuration variables is through `.env` file, both when running from source, or via Docker.

However, you can also supply them via environment variables.
Environment variables should take precedent over values in `.env`.


## Commands

* `help` - prints help
* `all` - uwuifies ALL messages sent in this channel (available onlu in servers)
* `this` - uwuifies text given as an argument to this command
* `previous` - uwuifies previous message in this channel (extept bot messages or other commands)
* `that` - uwuifies message which this command replies to, allowing for "targeted" uwuification
* `quote` - sends an inspirational uwuified quote


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


### Inspirational quotes
You can supply your API source for inspirational quotes via `.env` file.
You also need to specify via JSON key names which JSON values should be treated as quote text and which as quote author.


## Why?

Why not?

Also this: https://austinhenley.com/blog/makinguselessstuff.html