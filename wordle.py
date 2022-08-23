import sys

def compare(compare_with, compare_this):
    for i in range(5):
        if compare_this[i] == compare_with[i]: # if letter matched perfectly
            guessing_stat[i] = "+"
        else:
            try: # trying if a letter is just in a different spot of the word
                different_spot = compare_this.index(compare_with[i])
            except ValueError:
                continue
            else:
                guessing_stat[i] = "="
    return(guessing_stat)

secret_word = "slate"
secret_list = tuple(secret_word)

print("Enter your guess:")

guesses = 5
while guesses > 0: # game process
    player_guess = input()
    if len(player_guess) == 5:
        if player_guess == secret_word:
            guessing_stat = ["+", "+", "+", "+", "+"]
            print(f"{guessing_stat[0]}{guessing_stat[1]}{guessing_stat[2]}{guessing_stat[3]}{guessing_stat[4]}") # ungracious way of printing the current guess' score to fit under the letters
            print("The word was: " + secret_word + ". You won!")
            sys.exit()
        else:
            guesses -= 1

            guessing_stat = ["-", "-", "-", "-", "-"] # reverting the current guess' score to default before every next guess

            player_guess = list(player_guess) # https://stackoverflow.com/questions/113655/is-there-a-function-in-python-to-split-a-word-into-a-list

            compare(player_guess, secret_list)

            print(f"{guessing_stat[0]}{guessing_stat[1]}{guessing_stat[2]}{guessing_stat[3]}{guessing_stat[4]}") # ungracious way of printing the current guess' score to fit under the letters
            print(f"{guesses} tries left")
    else:
        print("The word should be 5 letters long!")

