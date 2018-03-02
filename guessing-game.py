#guessing-game.py

def guessinggame():
    correct = "lion"
    print("I am thinking of an animal.")
    guess = input("Guess the name of the animal: ")
    guess = guess.lower()
    while correct is "lion":
            if guess == correct:
                print("Congratulations! You guessed correctly! The animal is lion")
                break
            elif guess == "quit":
                guess = guess.lower()
                print("Thanks for playing.")
                break
            else:
                print("Your guess was incorrect please try again.")
                guess = input("Guess the name of the animal: ")
                guess = guess.lower()
                

        
guessinggame()
