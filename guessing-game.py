#guessing-game.py

def guessinggame():
    correct = "lion"
    print("I am thinking of an animal.")
    guess = input("Guess the name of the animal: ")
    guess = guess.lower()
    while correct is "lion":
            if guess == correct:
                print("Congratulations! You guessed correctly! The animal is lion")
                input("Do you like this animal? Enter y for yes. Enter n for no.")
                if "y":
                    print("Thats great!")
                if "n":
                    print("Well I am sorry to hear that.")
                break
            elif guess[0] == "q":
                guess = guess.lower()
                
                    
                print("Thanks for playing.")
                break
            else:
                print("Your guess was incorrect please try again.")
                guess = input("Guess the name of the animal: ")
                guess = guess.lower()
                

        
guessinggame()
