'''Lógica do mini-game de cara ou coroa'''

from time import sleep
from random import choice
from time import sleep
from random import choice
from interface.tools import Tools

class Game:
    def __init__(self, player):
        self.player = player

    def run(self):
        options = ["cara", "coroa"]
        print(f"\n\033[36m[!] Muito bem, {self.player['name']}, vamos nessa!\033[0m")

        while True:
            try:
                amount = float(input("\n[?] O quanto você quer apostar?\nplayer: "))
                Tools.verify_cash(self.player, amount)
            except ValueError as e:
                print(f"[!] {e}")
                sleep(1)
                continue

            pick = input("\n\033[36m[?] Qual sua aposta? (cara/coroa)\033[0m\nplayer: ").strip().lower()
            if pick not in options:
                print("[!] Insira um lado válido: cara ou coroa")
                sleep(1)
                continue

            if pick == choice(options):
                self.player["wins"] += 1
                self.player["cash"] += amount
                print(f"\n\033[32m[!] Você acertou! +{amount:.2f} cash\033[0m")
            else:
                self.player["cash"] -= amount
                print(f"\n\033[31m[!] Você perdeu! -{amount:.2f} cash\033[0m")

            self.player["total"] += 1
            Tools.save_player(self.player)

            if input("\n[?] Jogar novamente? (s/n)\nplayer: ").strip().lower() != "s":
                break

        return self.player

if __name__ == "__start__":
    s = Game()
    
    s.run()