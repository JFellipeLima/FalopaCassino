from .fileManager import Files

class Player:
    def __init__(self):
        self.file = Files()
        player = self._load()
        
        if player:
            self.name = player["name"]
            self.cash = player["cash"]
            self.total = player["total"]
            self.wins = player["wins"]

        else:
            self.name = ""
            self.cash = 0
            self.total = 0
            self.wins = 0

    def _load(self):
            return self.file.load()
    
    def save(self):
        self.file.save(self.player_info())
         
    def new(self, name):
        self.name = name
        self.cash = 100
        self.total = 0
        self.wins = 0
        self.save()
    
    def verify_cash(self, amount):
        if self.cash < amount or amount <= 0:
            return False
        return True
    
    def player_info(self):
        return {
            "name": self.name,
            "cash": self.cash,
            "total": self.total,
            "wins": self.wins
        }

if __name__ == "__main__":
    player = Player()
    print(player.player_info())