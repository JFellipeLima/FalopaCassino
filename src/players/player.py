from economy.fileManager import Files
from economy.wallet import Wallet

class Player:
    def __init__(self):
        self.file = Files()
        self.wallet = Wallet()
        player = self._load()

        if player:
            self.name = player["name"]
            self.total = player["total"]
            self.wins = player["wins"]

        else:
            self.name = ""
            self.total = 0
            self.wins = 0

    def _load(self):
            return self.file.load()

    def save(self):
        self.file.save(self.player_info())

    def new(self, name):
        self.name = name
        self.wallet.credit(1000)
        self.total = 0
        self.wins = 0
        self.save()

    def player_info(self):
        return {
            "name": self.name,
            "cash": self.wallet.balance(),
            "total": self.total,
            "wins": self.wins
        }

if __name__ == "__main__":
    player = Player()
    print(player.player_info())