import random

while True:
    print("Rock-Paper-Scissor Game Started!!")
    choose_action = ["Rock", "Paper","Scissor"]
    user_input = input("Enter a choice(Rock,Paper,Scissor): ")
    select_computer_choice = random.choice(choose_action)
    if user_input not in choose_action or select_computer_choice not in choose_action:
        print("Choose only in between rock, paper, scissor")
    else:
        print(f"User choose {user_input} & Computer choose {select_computer_choice}")
    
#Determine the winner
    if (user_input == select_computer_choice):
        print("Both seleted same choice,match TIE!!")
        
    elif user_input == "Rock":
        if select_computer_choice == "Scissor":
            print("Rock hits Scissor")
            print("USER WINS!!")
        else:
            print("Paper Covers Rock")
            print("COMPUTER WIN!!")
            
    elif user_input  == "Paper":
        if select_computer_choice == "Rock":
            print("Paper Covers Rock")
            print("USER WINS!!")
        else:
            print("Scissor cuts Paper")
            print("COMPUTER WIN!!")
            
    elif user_input == "Scissor":
        if select_computer_choice == "Paper":
            print("Scissor cuts Paper")
            print("USER WINS!!")
        else:
            print("Rock hits Scissor")
            print("COMPUTER WIN!!")
            
    else:
        pass

    
    
    player_choice = input("Do You want to continue this game (y/n): ")
    if player_choice != 'y':
        print("GAME STOP!!!")
        break
    print("                                      ")
    
print("*********************************")
