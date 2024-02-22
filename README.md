# Rock Paper Scissors Discord Bot

## Overview

This is a Discord bot that allows users to play the game of Rock, Paper, Scissors. The bot is built using the discord.py library and uses slash commands for interaction.

## Features

- Start a new game with `/start_game`
- Play by choosing rock, paper, or scissors with `/play`
- End the game at any time with `/end_game`
- Display the game rules with `/rules`
- The game can be played by multiple players
- The game ends when all three choices are made or a winner is determined

## Setup

### Using a Virtual Environment

1. Clone the repository
2. Create a virtual environment:

    ```bash
    # If python is linked to Python 3 on your system
    python -m venv env

    # If python3 is the command for Python 3 on your system
    python3 -m venv env
    ```

3. Activate the virtual environment:

    ```bash
    source env/bin/activate
    ```

4. Install the requirements:

    ```bash
    # If pip is linked to Python 3 in your virtual environment
    pip install -r requirements.txt

    # If pip3 is the command for Python 3 in your virtual environment
    pip3 install -r requirements.txt
    ```

5. Run the bot:

    ```bash
    # If python is linked to Python 3 in your virtual environment
    python bot.py

    # If python3 is the command for Python 3 in your virtual environment
    python3 bot.py
    ```

### Using Global Python

1. Clone the repository
2. Install the requirements:

    ```bash
    # If pip is linked to Python 3 on your system
    pip install -r requirements.txt

    # If pip3 is the command for Python 3 on your system
    pip3 install -r requirements.txt
    ```

3. Run the bot:

    ```bash
    # If python is linked to Python 3 on your system
    python bot.py

    # If python3 is the command for Python 3 on your system
    python3 bot.py
    ```

## Configuration

Configuration variables are stored in `config.py`. You need to set the following:

- `discord_bot_token`: The token of your Discord bot.
- `channel_id`: The ID of the channel where the bot will be used.

## FAQ

**Q: How many players can play the game?**
A: The game can be played by multiple players. The game ends when all three choices are made or a winner is determined.

**Q: How to end the game?**
A: You can end the game at any time by using the `/end_game` command.

**Q: Can the game be started without multiple players?**
A: No, the game requires at least two players to start.

## License

This project is licensed under the terms of the MIT license. For more information, see the [LICENSE](./LICENSE) file.
