from .fileManager import Files

class Wallet:
    def __init__(self):
        self.file = Files()
        self.player_data = self.file.load()
        
    def balance(self):
        return self.player_data["cash"]

    def credit(self, amount):
        self.player_data["cash"] += amount
        self.file.save(self.player_data)

    def debit(self, amount):
        if self.player_data["cash"] < amount:
            return False
        
        self.player_data["cash"] -= amount
        self.file.save(self.player_data)
        return True

    def is_broke(self):
        return self.player_data["cash"] <= 0




if __name__ == "__main__":
    wallet = Wallet()
    wallet.credit(1000)
    wallet.debit(500)
    print(wallet.balance())