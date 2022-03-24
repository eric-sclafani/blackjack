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
              
def start_game(PC, NPCS, dealer):
    
    # shuffle the order of all players
    order = NPCS
    order.append(PC)
    random.shuffle(order)

    # each hand be an iteration of while loop?
    while True:
        
        # all players place their bets 
        print()
        typewrite("~~~Place your bets!~~~\n")
        PC_bet = PC.place_bet()
        for player in NPCS:
            pass
        
        
        # cards get dealt to each player
        print()
        typewrite(f"{dealer.name} deals the cards.\n")
        for player in NPCS:
            player.hand = dealer.deal()
            
        
            
        

        break  # current safety net
            
         
    
def main():
    
    dealer = pc.Dealer(name=random.choice(NAMES))
    #typewrite(f"Hello sir or madam. My name is {dealer.get_name()}. Welcome to my table. What is your name and how many players would you like to play with?\n")
    name, num_players = intro() 
    PC = pc.PlayerCharacter(name, wallet=50) # wallet WIP
    
    NPCS = []
    for n in range (num_players):
        npc = pc.NonPlayerCharacter(random.choice(NAMES), wallet=random.randint(50, 200)) # num WIP
        NPCS.append(npc)
    
    start_game(PC, NPCS, dealer)
    
    
   
        

if __name__ == "__main__":
    main()