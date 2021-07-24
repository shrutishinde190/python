import random
n = random.randint(1,10)
player_name = input("Enter a name: ")
no_of_attempts = 0    
while True:
    if no_of_attempts != 3:
        no_of_attempts += 1
    else:
        break
    
    player_guess = int(input("Guess a number: "))
    
    if n > player_guess:
        print("You guess low number")
    elif n < player_guess:
        print("You guess high number")
    else:
        print("You guessed correct number")
    
    player_choice = input("Do you want to play this game(y/n): ")
    if player_choice != 'y':
        print("Game Stop!!")
        break

print("Your guess is wrong in 3 attempts")
    

