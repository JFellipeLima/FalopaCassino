"""Lucky 7 - caça-níquel."""

from random import choices
from time import sleep

from src.wallet import Wallet
from src.bets import Bet


class Game:

    SYMBOLS = [
        "🍒",
        "🍋",
        "🔔",
        "7️⃣",
        "💎"
    ]

    MULTIPLIERS = {
        "💎": 20,
        "7️⃣": 15,
        "🔔": 8,
        "🍒": 5,
        "🍋": 3
    }

    def __init__(self, wallet):

        self.bet = Bet(wallet)

        self.jackpot = 1000

    def spin(self):

        return choices(
            self.SYMBOLS,
            k=3
        )

    def calculate_payout(self, result, amount):

        first, second, third = result

        # três iguais
        if first == second == third:

            multiplier = self.MULTIPLIERS[first]

            return amount * multiplier

        # dois iguais
        if (
            first == second
            or first == third
            or second == third
        ):

            return amount * 1.5

        return 0

    def display(self, result):

        print("\n╔══════════════════════╗")
        print(
            f"║  {result[0]}   {result[1]}   {result[2]}  ║"
        )
        print("╚══════════════════════╝")

    def run(self):

        print("\n\033[36m╔══════════════════════════╗")
        print("║       🎰 LUCKY 7 🎰       ║")
        print("╚══════════════════════════╝\033[0m")

        print("\nTabela de pagamentos:")

        for symbol, multiplier in self.MULTIPLIERS.items():

            print(
                f"{symbol} {symbol} {symbol}"
                f" → {multiplier}x"
            )

        print("Dois iguais → 1.5x")
        print("Nenhum igual → perde")

        while True:

            print(
                f"\n\033[33m"
                f"Jackpot: {self.jackpot:.2f}"
                f"\033[0m"
            )

            try:

                amount = float(
                    input(
                        "\n[?] Quanto deseja apostar?\n"
                        "player: "
                    )
                )

                if amount <= 0:

                    print(
                        "[!] A aposta deve ser maior que zero."
                    )

                    continue

            except ValueError:

                print(
                    "[!] Digite um número válido."
                )

                continue

            # tenta fazer a aposta
            if not self.bet.place_bet(amount):

                print(
                    "\033[31m"
                    "[!] Saldo insuficiente."
                    "\033[0m"
                )

                break

            # parte da aposta alimenta o jackpot
            self.jackpot += amount * 0.05

            print("\nGirando...")

            sleep(0.5)
            print("🎰 | ? | ?")

            sleep(0.5)
            print("🎰 | 🎰 | ?")

            sleep(0.5)

            result = self.spin()

            self.display(result)

            payout = self.calculate_payout(
                result,
                amount
            )

            # jackpot
            if result == ["💎", "💎", "💎"]:

                payout += self.jackpot

                print(
                    "\n\033[32m"
                    "💎 JACKPOT! 💎"
                    "\033[0m"
                )

                self.jackpot = 1000

            if payout > 0:

                self.bet.win_bet(payout)

                profit = payout - amount

                print(
                    f"\n\033[32m"
                    f"[!] Você ganhou!"
                    f"\n[+] Prêmio: {payout:.2f}"
                    f"\n[+] Lucro: {profit:.2f}"
                    f"\033[0m"
                )

            else:

                print(
                    "\n\033[31m"
                    "[!] Nada dessa vez."
                    "\033[0m"
                )

            # estado financeiro
            balance = self.bet.wallet.balance()

            print(
                f"\n💰 Saldo: {balance:.2f}"
            )

            # jogador quebrou
            if self.bet.wallet.is_broke():

                print(
                    "\n\033[31m"
                    "💀 Você está sem dinheiro."
                    "\nFim de jogo."
                    "\033[0m"
                )

                break

            again = input(
                "\n[?] Girar novamente? (s/n)\n"
                "player: "
            ).strip().lower()

            if again != "s":

                break

        return self.bet.wallet.balance()


if __name__ == "__main__":
    wallet = Wallet()
    game = Game(wallet)

    game.run()