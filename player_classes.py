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
        # really wanted to use a higher order func for some reason
        return sum(map(lambda x: 10 if isinstance(x, str) else x, self.hand))

    def get_name(self):
        return self.name
    
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
    
# player character 
class PC(Player):
    # player decides their own bet, moves, etc...
    pass

# non-player character               
class NPC(Player):
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