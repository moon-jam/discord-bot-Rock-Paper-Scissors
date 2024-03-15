# Rock Paper Scissors Discord Bot

## Overview

This is a Discord bot that allows users to play the game of Rock, Paper, Scissors. The bot is built using the discord.py library and uses slash commands for interaction.

## Features

- The game can be played by multiple players.
- Utilizes Discord's Slash Commands, allowing players to interact with the game directly in the chat.
- The game results are visualized in a table format at the end of the game. This graphical table lists all players' choices and highlights the winners or players who tied, providing a clear and concise view of the outcomes. This ensures consistent formatting across all devices and platforms. See the example below:
![Game Result Table Example](./assets/table.png)

## Game Rules

- Start a new game with `/start_game`
- Play by choosing rock, paper, or scissors with `/play`
- End the game at any time with `/end_game`
- Display the game rules with `/rules`
- The game ends when all three choices have been made by the players or the game is forcibly ended.

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

### Configuration

Configuration variables are stored in `config.py`. You need to set the following:

- `discord_bot_token`: The token of your Discord bot.
- `channel_id`: The ID of the channel where the bot will be used.
- `victory_color`: This is the color used to highlight the winners or players who tied in the game result table. The default color is "#FFFAB5".

## FAQ

**Q: How many players can play the game?**
A: The game can be played by multiple players. The game ends when all three choices are made or a winner is determined.

**Q: How to end the game?**
A: You can end the game at any time by using the `/end_game` command.

**Q: Can the game be started without multiple players?**
A: No, the game requires at least two players to start.

## Font

The Chinese font used in this project is [Taipei Sans TC Beta Regular](https://sites.google.com/view/jtfoundry). This font is licensed under the [SIL Open Font License 1.1](https://opensource.org/license/OFL-1.1).

According to the SIL Open Font License 1.1, you are free to use, modify, and distribute this font, but you must keep the copyright notice and license of the original font. For detailed permissions and restrictions, please refer to the [SIL Open Font License 1.1](https://opensource.org/license/OFL-1.1).

## License

This project is licensed under the terms of the MIT license. For more information, see the [LICENSE](./LICENSE) file.

## TODO

- [x] Add English version
