from .wallet import Wallet

class Bet:
    def __init__(self, wallet):
        self.wallet = wallet
    
    def place_bet(self, amount):
        if self.wallet.debit(amount):
            return True
        return False
    
    def win_bet(self, amount):
        self.wallet.credit(amount)





if __name__ == "__main__":
    wallet  = Wallet()
    bet = Bet(wallet)
    bet.win_bet(500)
    print(bet.wallet.balance())