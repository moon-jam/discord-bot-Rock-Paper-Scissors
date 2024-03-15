# lang.py
MESSAGES = {
    "start_game": {
        "en": "Game started, please make your move",
        "zh": "遊戲開始，請輸入你的拳"
    },
    "game_already_started": {
        "en": "Game has already started",
        "zh": "遊戲已經開始"
    },
    "game_not_started": {
        "en": "Game has not started yet",
        "zh": "遊戲尚未開始"
    },
    "already_moved": {
        "en": "You have already made your move",
        "zh": "你已經出過拳了"
    },
    "need_more_players": {
        "en": "More players are needed to start the game",
        "zh": "需要更多玩家參與遊戲"
    },
    "tie_players": {
        "en": "The following players are currently tied: ",
        "zh": "目前平手的玩家有 "
    },
    "current_winner": {
        "en": "The current winner is: ",
        "zh": "當前勝利者是 "
    },
    "game_ended_winner": {
        "en": "Game ended, the winner is: ",
        "zh": "遊戲結束，勝利者是 "
    },
    "game_ended_tie": {
        "en": "Game ended in a tie, the following players are tied: ",
        "zh": "遊戲結束，平手的玩家有 "
    },
    "game_ended_all_moves": {
        "en": "Game ended, all moves have been made, the winner is: ",
        "zh": "遊戲結束，三種拳都已經被出過了，最後一拳還未出時，勝利者是 "
    },
    "all_players_choices": {
        "en": "Everyone's choices are:",
        "zh": "所有人的選擇是："
    },
    "game_forced_end": {
        "en": "Game has been forcibly ended",
        "zh": "遊戲已被強制終止"
    },
    "rules": {
        "en": """
Welcome to the Rock Paper Scissors game! Here are the rules:

1. Use /start_game to start the game.
2. Use /play and choose your move (rock, paper, or scissors).
3. If there are more than one player in the game, the game will determine the winner.
4. If all three moves are chosen, the game will end.
5. Use /end_game to end the game at any time.

Enjoy the game!
        """,
        "zh": """
歡迎來到猜拳遊戲！以下是遊戲規則：

1. 使用 /start_game 開始遊戲。
2. 使用 /play 並選擇你的拳（石頭、剪刀或布）。
3. 如果遊戲中有超過一個玩家，遊戲將決定勝利者。
4. 如果所有三種拳都被選擇，遊戲將結束。
5. 使用 /end_game 可以在任何時候終止遊戲。

祝你遊戲愉快！
        """
    },
    "language_set": {
        "en": "Language has been set to {0}",
        "zh": "語言已設置為 {0}"
    },
}

DESCRIPTIONS = {
    "start_game": {
        "en": "Start the Rock Paper Scissors game",
        "zh": "開始猜拳遊戲"
    },
    "end_game": {
        "en": "End the game forcibly",
        "zh": "強制終止遊戲"
    },
    "play": {
        "en": "Make your move",
        "zh": "出拳"
    },
    "rules": {
        "en": "Show the game rules",
        "zh": "顯示遊戲規則"
    },
    "set_language": {
        "en": "Set the language",
        "zh": "設置語言"
    },
    "input_move": {
        "en": "Input your move",
        "zh": "輸入你的拳"
    },
}

CHOICES_DESCRIPTIONS = {
    "rock": {
        "en": "Rock",
        "zh": "石頭"
    },
    "scissors": {
        "en": "Scissors",
        "zh": "剪刀"
    },
    "paper": {
        "en": "Paper",
        "zh": "布"
    },
}

COLUMNS = {
    "player": {
        "en": "Player",
        "zh": "玩家"
    },
    "choice": {
        "en": "Choice",
        "zh": "選擇"
    },
}