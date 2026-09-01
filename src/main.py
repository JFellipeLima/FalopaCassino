from sys import argv, exit
from os import listdir, path
from importlib import import_module
from economy.wallet import Wallet
from players.player import Player

dirgame = path.join(path.dirname(__file__), "games")

def arg_verify(args):
    prefix = "-"
    options = {
        "P": {run_game, 1},
        "L": {list_games, 0}
    }
    arg1 = args[1]
    if not prefix in arg1 or arg1[-1:] not in options:
        return help()

    arg2 = args[2:]
    slots, op = options[arg1[-1:]]

    if len(arg2) != slots:
        return help()

    op(*arg2)

def help():
    return print("""
Help:
    Usage: flops --<flag> <arg>

-P <game_name> play a game
-L List all game loaded
          """)

def load_game():
    games = [game for game in listdir(dirgame) if
            path.isdir(path.join(dirgame, game))]

    return games

def run_game(game_name):
    games = load_game()
    if game_name in games:

        module_path = f"games.{game_name}.game"
        game = import_module(module_path)

        wallet = Wallet()
        player = Player()

        start = game.Game(player, wallet)
        return start.run()
    
    else:
        print("Game not found. Run -L to lis all games")

def list_games():
    games = load_game()
    return print(games)




if __name__ == "__main__":
    arg_verify(argv)