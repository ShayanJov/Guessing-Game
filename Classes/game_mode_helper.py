from .game_logic import play_game

class GameLogic:
    def play_classic_mode(player_name):
        play_game(player_name, num_questions=6, max_attempts=3, max_fails=6, game_mode="classic")

    def play_easy_mode(player_name):
        play_game(player_name, num_questions=None, max_attempts=3, max_fails=3, game_mode="easy")

    def play_normal_mode(player_name):
        play_game(player_name, num_questions=None, max_attempts=3, max_fails=1, game_mode="normal")

    def play_hard_mode(player_name):
        play_game(player_name, num_questions=None, max_attempts=1, max_fails=1, game_mode="hard")