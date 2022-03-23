import player_classes as pc
from nltk.corpus import names
import random
from time import sleep


# ~~GLOBAL DECLARATIONS ~~~
NAMES = names.words()
  
def typewrite(text, t=.03):
    for n in text:
        sleep(t)
        print(n, end="", flush=True) 
    
          
def intro():
    
    while True:
        name = input("Name: ").title().strip()
        # prevent user from entering empty string for their name
        if name == "":
            print("Please re-enter your name.")
        else:
        # fallout new vegas doc mitchel reference
        # for people who are "creative" with their names
        # (or just have a name not in the NLTK names corpus ¯\_(ツ)_/¯ )
            if name not in NAMES:
                typewrite(f"{name}? Well, that's not the name I'd pick for ya, but if that's your name, that's your name! Nice to meet ya.\n")
            break
    print("# of players: ", end="") # end="" will put the following input on the same line
    while True:
        try:
            num_players = int(input().strip())
            assert 0 < num_players < 7
        except ValueError:
            print("Input must be an integer: ", end="")
        except AssertionError:
            print("# must be between 0 and 7: ", end="")  
        else:
            return name, num_players

def get_PC_bet(player):
    typewrite("How much would you like to bet?")
    while True:
        try:
            bet = int(input().strip())
            assert player.wallet >= bet > 0
        except ValueError: 
            print("Bet must be an integer: ", end="")
        except AssertionError:
            print("Bet must be: 0 < bet >= wallet amount.")
        else:
            return bet
                     
def start_hand(players, dealer):
    
    # shuffle the order of all players
    order = list(players.keys())
    random.shuffle(order)

    # each hand be an iteration of while loop?
    while True:
        
        typewrite(f"{dealer.get_name()} deals the cards.\n")
        
        # cards get dealt to each player
        for player in order:
            players[player].hand = dealer.deal()

        break  
            
         
    
def main():
    
    dealer = pc.Dealer(name=random.choice(NAMES))
    #typewrite(f"Hello sir or madam. My name is {dealer.get_name()}. Welcome to my table. What is your name and how many players would you like to play with?\n")
    name, num_players = intro() 
    players = {"PC": pc.PC(name, wallet=50)} # num WIP
    
    for n in range (1, num_players+1):
        npc = pc.NPC(random.choice(NAMES), wallet=random.randint(50, 200)) # num WIP
        players[f"Player {n}"] = npc
    
    start_hand(players, dealer)
    
    
   
        

if __name__ == "__main__":
    main()