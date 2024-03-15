import discord
from typing import Optional
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice
from matplotlib.font_manager import fontManager
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from config import victory_color, default_language
from lang import MESSAGES, DESCRIPTIONS, CHOICES_DESCRIPTIONS, COLUMNS

fontManager.addfont("./TaipeiSansTCBeta-Regular.ttf")
matplotlib.rc("font", family="Taipei Sans TC Beta")

# TODO: switch language to English


class Slash(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.game_active = False
        self.players = {}
        self.winner = []
        self.tie_players = []
        self.language = default_language

    @app_commands.command(
        name="set_language", description=DESCRIPTIONS["set_language"][default_language]
    )
    @app_commands.choices(
        choice=[
            Choice(name="English", value="en"),
            Choice(name="中文", value="zh"),
        ]
    )
    async def set_language(self, interaction: discord.Interaction, choice: Choice[str]):
        language = choice
        self.language = language.value
        await interaction.response.send_message(
            MESSAGES["language_set"][self.language].format(language.name)
        )

    @app_commands.command(
        name="start_game", description=DESCRIPTIONS["start_game"][default_language]
    )
    async def start_game(self, interaction: discord.Interaction):
        if self.game_active:
            MESSAGES["game_already_started"][self.language]
            return

        self.game_active = True
        self.players = {}
        self.winner = []
        self.tie_players = []
        await interaction.response.send_message(MESSAGES["start_game"][self.language])

    @app_commands.command(
        name="end_game", description=DESCRIPTIONS["end_game"][default_language]
    )
    async def end_game_command(self, interaction: discord.Interaction):
        if not self.game_active:
            await interaction.response.send_message(
                MESSAGES["game_not_started"][self.language]
            )
            return
        await interaction.response.send_message("Processing end_game...")
        await self.end_game(interaction)
        print("game forced end")

    @app_commands.command(
        name="play", description=DESCRIPTIONS["play"][default_language]
    )
    @app_commands.describe(choice=DESCRIPTIONS["input_move"][default_language])
    @app_commands.choices(
        choice=[
            Choice(name=CHOICES_DESCRIPTIONS["rock"][default_language], value="rock"),
            Choice(
                name=CHOICES_DESCRIPTIONS["scissors"][default_language],
                value="scissors",
            ),
            Choice(name=CHOICES_DESCRIPTIONS["paper"][default_language], value="paper"),
        ]
    )
    async def play(self, interaction: discord.Interaction, choice: Choice[str]):
        try:
            if not self.game_active:
                await interaction.response.send_message(
                    MESSAGES["game_not_started"][self.language]
                )
                return

            player = interaction.user.display_name
            if player in self.players:
                await interaction.response.send_message(
                    MESSAGES["already_moved"][self.language]
                )
                return

            await interaction.response.send_message("Processing play...")
            self.players[player] = choice.value

            if len(self.players) == 1:
                await interaction.edit_original_response(
                    content=MESSAGES["need_more_players"][self.language]
                )
            elif len(set(self.players.values())) == 3:
                await self.end_game(interaction)
            elif len(set(self.players.values())) == 2:
                self.determine_winner()
                if self.tie_players:
                    await interaction.edit_original_response(
                        content=MESSAGES["tie_players"][self.language]
                        + f"** {'**, **'.join(self.tie_players)}"
                        + "**"
                    )
                elif self.winner:
                    await interaction.edit_original_response(
                        content=MESSAGES["current_winner"][self.language]
                        + f"** {'**, **'.join(self.winner)}"
                        + "**"
                    )
        except Exception as e:
            print(f"err: {e}")

    def determine_winner(self):
        choices = list(self.players.values())
        if len(set(choices)) == 1:
            self.tie_players = list(self.players.keys())
        elif len(set(choices)) == 3:
            return
        elif "rock" in choices and "scissors" in choices:
            self.winner = [
                player for player, choice in self.players.items() if choice == "rock"
            ]
            self.tie_players = []
        elif "scissors" in choices and "paper" in choices:
            self.winner = [
                player
                for player, choice in self.players.items()
                if choice == "scissors"
            ]
            self.tie_players = []
        elif "paper" in choices and "rock" in choices:
            self.winner = [
                player for player, choice in self.players.items() if choice == "paper"
            ]
            self.tie_players = []

    async def end_game(self, interaction: discord.Interaction):
        try:
            print("end_game started")

            # 創建 DataFrame
            data = {
                COLUMNS["player"][self.language]: list(self.players.keys()),
                COLUMNS["choice"][self.language]: list(self.players.values()),
            }
            df = pd.DataFrame(data)

            # 繪製表格
            cell_colours = []
            for player, choice in zip(
                df[COLUMNS["player"][self.language]],
                df[COLUMNS["choice"][self.language]],
            ):
                if player in self.winner or player in self.tie_players:
                    cell_colours.append([victory_color, victory_color])
                else:
                    cell_colours.append(["lightgray", "lightgray"])

            num_rows, num_cols = df.shape
            figsize = (20, (num_rows + 1) * 0.4)
            fig, ax = plt.subplots(figsize=(figsize))
            ax.axis("tight")
            ax.axis("off")
            the_table = ax.table(
                cellText=df.values,
                colLabels=df.columns,
                cellLoc="center",
                loc="center",
                cellColours=cell_colours,
                colColours=["gray"] * len(df.columns),
            )
            the_table.auto_set_font_size(False)
            the_table.set_fontsize(12)
            the_table.scale(2, 2)

            fig.tight_layout()
            # 保存表格圖片
            plt.savefig("table.png", bbox_inches="tight", pad_inches=0.1)
            file = discord.File("table.png", filename="table.png")

            if len(set(self.players.values())) == 3:
                await interaction.edit_original_response(
                    content=MESSAGES["game_ended_all_moves"][self.language]
                    + f"** {'**, **'.join(self.winner)}"
                    + f"**\n"
                    + MESSAGES["all_players_choices"][self.language],
                    attachments=[file],
                )
            elif self.tie_players:
                await interaction.edit_original_response(
                    content=MESSAGES["game_ended_tie"][self.language]
                    + f"** {'**, **'.join(self.tie_players)}"
                    + f"**\n"
                    + MESSAGES["all_players_choices"][self.language],
                    attachments=[file],
                )
            else:
                await interaction.edit_original_response(
                    content=MESSAGES["game_ended_winner"][self.language]
                    + f"** {'**, **'.join(self.winner)}"
                    + f"**\n"
                    + MESSAGES["all_players_choices"][self.language],
                    attachments=[file],
                )

            self.game_active = False
            self.players = {}
            self.winner = []
            self.tie_players = []
            print("end_game finished")
        except Exception as e:
            print(f"err: {e}")

    @app_commands.command(
        name="rules", description=DESCRIPTIONS["rules"][default_language]
    )
    async def rules(self, interaction: discord.Interaction):
        await interaction.response.send_message(MESSAGES["rules"][self.language])


async def setup(bot: commands.Bot):
    await bot.add_cog(Slash(bot))
