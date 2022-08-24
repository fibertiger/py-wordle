# py-wordle
Python wordle clone that plays in your terminal  
### How to play  
1. Clone this repository  
2. Open your local copy  
3. Run wordle.py: ```python3 wordle.py```
  
### Raw files  
Raw word lists folder and the script in it contain lists of words similar to the original game's lists of words. The py script in that folder converts those raw lists into the .pkl files in the root folder. We don't need to run that script every time, but it is still there in case we ever need to regenerate the .pkl files (for example, if the list of words changes).

### Known issues
 - If player's guess has two same letters in different spots, and neither of the spots are a correct spot, and the secret word only has one instance of that latter, the game will incorrectly mark both letters in the guess as "correct". The original game only marks as many letters as there are in the secret word to avoid confusion. (Ex. secret word = "place", guess = "jelly", both "l" will incorrectly be marked as "correct letter, wrong spot")
