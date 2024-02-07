import discord
from typing import Optional
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice

class Slash(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.game_active = False
        self.players = {}
        self.winner = []
        self.tie_players = []

    @app_commands.command(name = "start_game", description = "開始猜拳遊戲")
    async def start_game(self, interaction: discord.Interaction):
        self.game_active = True
        await interaction.response.send_message("遊戲開始，請輸入你的拳")

    @app_commands.command(name = "end_game", description = "強制終止遊戲")
    async def end_game_command(self, interaction: discord.Interaction):
        if not self.game_active:
            await interaction.response.send_message("遊戲尚未開始")
            return

        await self.end_game(interaction)
        await interaction.response.send_message("遊戲已被強制終止")

    @app_commands.command(name = "play", description = "出拳")
    @app_commands.describe(choice = "輸入你的拳")
    @app_commands.choices(
        choice = [
            Choice(name = "石頭", value = "rock"),
            Choice(name = "剪刀", value = "scissors"),
            Choice(name = "布", value = "paper"),
        ]
    )
    async def play(self, interaction: discord.Interaction, choice: Choice[str]):
        if not self.game_active:
            await interaction.response.send_message("遊戲尚未開始")
            return

        player = interaction.user.name
        if player in self.players:
            await interaction.response.send_message("你已經出過拳了")
            return

        self.players[player] = choice.value

        if len(self.players) == 1:
            await interaction.response.send_message("需要更多玩家參與遊戲")
        elif len(self.players) >= 2:
            self.determine_winner()
            if self.tie_players:
                await interaction.response.send_message(f"目前平手的玩家有 {', '.join(self.tie_players)}")
            elif self.winner:
                await interaction.response.send_message(f"當前勝利者是 {', '.join(self.winner)}")

        if len(set(self.players.values())) == 3 or self.winner:
            await self.end_game(interaction)

    def determine_winner(self):
        choices = list(self.players.values())
        if len(set(choices)) == 1:
            self.tie_players = list(self.players.keys())
        elif "rock" in choices and "scissors" in choices:
            self.winner = [player for player, choice in self.players.items() if choice == "rock"]
        elif "scissors" in choices and "paper" in choices:
            self.winner = [player for player, choice in self.players.items() if choice == "scissors"]
        elif "paper" in choices and "rock" in choices:
            self.winner = [player for player, choice in self.players.items() if choice == "paper"]

    async def end_game(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"遊戲結束，勝利者是 {', '.join(self.winner)}，所有人的選擇是 {self.players}")
        self.game_active = False
        self.players = {}
        self.winner = []

async def setup(bot: commands.Bot):
    await bot.add_cog(Slash(bot))