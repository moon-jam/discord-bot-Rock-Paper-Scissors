import discord
from typing import Optional
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice
from matplotlib.font_manager import fontManager
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from config import victory_color

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

    @app_commands.command(name="start_game", description="開始猜拳遊戲")
    async def start_game(self, interaction: discord.Interaction):
        if self.game_active:
            await interaction.response.send_message("遊戲已經開始")
            return

        await interaction.response.send_message("Processing start_game...")
        self.game_active = True
        self.players = {}
        self.winner = []
        self.tie_players = []
        await interaction.edit_original_response(content="遊戲開始，請輸入你的拳")

    @app_commands.command(name="end_game", description="強制終止遊戲")
    async def end_game_command(self, interaction: discord.Interaction):
        if not self.game_active:
            await interaction.response.send_message("遊戲尚未開始")
            return
        await interaction.response.send_message("Processing end_game...")
        await self.end_game(interaction)
        print("遊戲已被強制終止")

    @app_commands.command(name="play", description="出拳")
    @app_commands.describe(choice="輸入你的拳")
    @app_commands.choices(
        choice=[
            Choice(name="石頭", value="rock"),
            Choice(name="剪刀", value="scissors"),
            Choice(name="布", value="paper"),
        ]
    )
    async def play(self, interaction: discord.Interaction, choice: Choice[str]):
        try:
            if not self.game_active:
                await interaction.response.send_message("遊戲尚未開始")
                return

            player = interaction.user.display_name
            if player in self.players:
                await interaction.response.send_message("你已經出過拳了")
                return

            await interaction.response.send_message("Processing play...")
            self.players[player] = choice.value

            if len(self.players) == 1:
                await interaction.edit_original_response(content="需要更多玩家參與遊戲")
            elif len(set(self.players.values())) == 3:
                await self.end_game(interaction)
            elif len(set(self.players.values())) == 2:
                self.determine_winner()
                if self.tie_players:
                    await interaction.edit_original_response(content=
                        f"目前平手的玩家有 ** {'**, **'.join(self.tie_players)}" + "**"
                    )
                elif self.winner:
                    await interaction.edit_original_response(
                        content=f"當前勝利者是 ** {'**, **'.join(self.winner)}" + "**"
                    )
        except Exception as e:
            print(f"發生錯誤: {e}")

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
            data = {"玩家": list(self.players.keys()), "選擇": list(self.players.values())}
            df = pd.DataFrame(data)

            # 繪製表格
            cell_colours = []
            for player, choice in zip(df["玩家"], df["選擇"]):
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
                await interaction.edit_original_response(content=
                    f"遊戲結束，三種拳都已經被出過了，最後一拳還未出時，勝利者是 ** {'**, **'.join(self.winner)}"
                    + f"**\n所有人的選擇是：",
                    attachments=[file]
                )
            elif self.tie_players:
                await interaction.edit_original_response(content=
                    f"遊戲結束，平手的玩家有 ** {'**, **'.join(self.tie_players)}"
                    + f"**\n所有人的選擇是：",
                    attachments=[file]
                )
            else:
                await interaction.edit_original_response(content=
                    f"遊戲結束，勝利者是  ** {'**, **'.join(self.winner)}" + f"**\n所有人的選擇是：",
                    attachments=[file]
                )

            self.game_active = False
            self.players = {}
            self.winner = []
            self.tie_players = []
            print("end_game finished")
        except Exception as e:
            print(f"發生錯誤: {e}")

    @app_commands.command(name="rules", description="顯示遊戲規則")
    async def rules(self, interaction: discord.Interaction):
        rules_message = """
歡迎來到猜拳遊戲！以下是遊戲規則：

1. 使用 /start_game 開始遊戲。
2. 使用 /play 並選擇你的拳（石頭、剪刀或布）。
3. 如果遊戲中有超過一個玩家，遊戲將決定勝利者。
4. 如果所有三種拳都被選擇，遊戲將結束。
5. 使用 /end_game 可以在任何時候終止遊戲。

祝你遊戲愉快！
        """
        await interaction.response.send_message(rules_message)


async def setup(bot: commands.Bot):
    await bot.add_cog(Slash(bot))
