#guessing-game.py

def guessinggame():
    correct = "lion"
    print("I am thinking of an animal.")
    guess = input("Guess the name of the animal: ")
    while correct is "lion":
            if guess == correct:
                print("Congratulations! You guessed correctly! The animal is lion")
                break
            else:
                print("Your guess was incorrect please try again.")
                guess = input("Guess the name of the animal: ")
                
                

        
guessinggame()
