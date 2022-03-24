import random

class Player:
    
    def __init__(self, name, wallet=0):
        
        self.name = name
        self.wallet = wallet
        
        self.hand = []
        self.bet = 0
        
    def get_hand_total(self):
    
        # converts face cards into their value 10
        # important not to mutate self.hand
        return sum(map(lambda x: 10 if isinstance(x, str) else x, self.hand))
    
    def place_bet(self, n):
        pass

    def hit(self):
        pass
    
    def double_down(self):
        pass
    
    def fold(self):
        pass
    
    def stand(self):
        pass
    
    def lose_hand(self):
        pass
    
    def win_hand(self):
        pass
    

class PlayerCharacter(Player):
    # player decides their own bet, moves, etc...
    
    def __init__(self, name, wallet=0):
        super().__init__(name, wallet)
        
    def place_bet(self):
        
        while True:
            try:
                print(f"Current wallet amount: {self.wallet}")
                bet = int(input("Bet: ").strip())
                assert self.wallet >= bet > 0
            except ValueError: 
                print("Bet must be an integer: ", end="")
            except AssertionError:
                print("Bet must be greater than 0 and less than or equal to your wallet amount.")
            else:
                return bet

              
class NonPlayerCharacter(Player):
    # add rules that will decide what decisions the NPCs make
    pass


class Dealer(Player):

    def __init__(self, name, wallet=0):
        super().__init__(name, wallet)

        # according to https://bicyclecards.com/how-to-play/blackjack/, 
        # most decks in casinos are comprised of multiple decks shuffled together
        self.deck =([2,3,4,5,6,7,8,9,10, "Ace", "Jack", "King", "Queen"]*4) * 6 # scale the decks
        for _ in range(5): # make sure it's REALLY shuffled
            random.shuffle(self.deck)


    def deal(self):
        return [random.choice(self.deck), random.choice(self.deck)]