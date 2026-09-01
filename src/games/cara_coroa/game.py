'''Lógica do mini-game de cara ou coroa'''

from time import sleep
from os import system
from random import choice
from time import sleep
from random import choice
from players.player import Player
from economy.wallet import Wallet

class Game:
    def __init__(self, player=None, wallet=None):
        self.player = player
        self.wallet = wallet
        if not self.player:
            name = input("\n[?] Qual o seu nome?\nplayer: ")
            self.player = Player()
            self.player.new(name)
            
    def run(self):
        options = ["cara", "coroa"]

        while True:
            if self.player.wallet.is_broke():
                if input("Voce faliu! Deseja reiniciar?[s/n]") == "s":
                    username = str(input("Digite o nome de usuario:"))
                    self.player.new(username)
                
                else:
                    exit()

            system("clear")
            print(f'''
              \n\033[36m[!] Muito bem, {self.player.name}, vamos nessa!\033[0m
              
              \n\033[36m[!] Você tem {self.player.wallet.balance():.2f} cash para apostar.\033[0m'''
              )

            try:
                amount = float(input("\n[?] O quanto você quer apostar?\nplayer: "))
                if not self.player.wallet.debit(amount):
                    print("[!] Você não tem dinheiro suficiente.")
                    sleep(1)
                    continue
            except ValueError as e:
                print(f"[!] {e}")
                sleep(1)
                continue

            pick = input("\n\033[36m[?] Qual sua aposta? (cara/coroa)\033[0m\nplayer: ").strip().lower()
            if pick not in options:
                print("[!] Insira um lado válido: cara ou coroa")
                sleep(1)
                break

            if pick == choice(options):
                self.player.wins += 1
                cash = amount*2
                self.player.wallet.credit(cash)
                print(f"\n\033[32m[!] Você acertou! +{amount:.2f} cash\033[0m")
            else:
                self.player.wallet.debit(amount)
                print(f"\n\033[31m[!] Você perdeu! -{amount:.2f} cash\033[0m")

            self.player.total += 1
            self.player.save()

            if input("\n[?] Jogar novamente? (s/n)\nplayer: ").strip().lower() != "s":
                break

        return self.player

if __name__ == "__main__":
    player = Player()
    wallet = Wallet()
    s = Game(player, wallet)
    print(s.player.player_info())
    try:
        s.run()
    except KeyboardInterrupt:
        print("Ate mais!")