import sys
from word_gen import secret_word
import pickle as pkl

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

i_file = open('allowed_input.pkl', 'rb')
i_list = pkl.load(i_file)
i_file.close()

secret_list = list(secret_word)

# FOR DEBUGGING: 
#print(secret_word)

print("Enter your guess:")

guess_count = 5
while guess_count > 0: # game process
    player_guess = input()
    real_word = player_guess in i_list
    if real_word == True:
        if len(player_guess) == 5:
            if player_guess == secret_word:
                guessing_stat = ["+", "+", "+", "+", "+"]
                print(f"{guessing_stat[0]}{guessing_stat[1]}{guessing_stat[2]}{guessing_stat[3]}{guessing_stat[4]}") # ungracious way of printing the current guess' score to fit under the letters
                print("The word was: " + secret_word + ". You won!")
                sys.exit()
            else:
                guess_count -= 1

                guessing_stat = ["-", "-", "-", "-", "-"] # reverting the current guess' score to default before every next guess

                player_guess = list(player_guess) # https://stackoverflow.com/questions/113655/is-there-a-function-in-python-to-split-a-word-into-a-list
                
                compare(player_guess, secret_list)

                print(f"{guessing_stat[0]}{guessing_stat[1]}{guessing_stat[2]}{guessing_stat[3]}{guessing_stat[4]}") # ungracious way of printing the current guess' score to fit under the letters
                print(f"{guess_count} tries left")
        else:
            print("The word should be 5 letters long!")
    else:
        print("Not a real word")
if guess_count == 0:
    print(f"The word was {secret_word}")