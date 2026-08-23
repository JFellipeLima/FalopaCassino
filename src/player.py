from fileManager import Files

class Player:
    def __init__(self):
        self.file = Files()
        self.player = self._load()

    def save(self):
        self.file.save(self.player)
        
        
    def new(self, name):
        self.player = {"name": name, "cash": 100, "total": 0, "wins": 0}
        self.save()
    
    def _load(self):
        return self.file.load()


if __name__ == "__main__":
    player = Player()
    print(player.player)