# transforming raw .txts into items of a list that we can use later

oldanswers = open("rawwordlists/old_allowedanswers.txt","r") # allowed answers/"secret words"
allowedanswers = open("allowedanswers.py","w")

oldguesses = open("rawwordlists/old_allowedguesses.txt","r") # allowed guesses
allowedguesses = open ("allowedguesses.py","w")

def raw_to_list(oldfile, newfile, c):
    l = 6
    for i in range(c):
        word = oldfile.readline(l)
        word = "\'" + word
        word = word[:6] + "\'" + ','
        newfile.write(word)
        l = l + 5

def count_lines(file): # find out many lines/words are in a file
    with open(file) as f: 
        for line in f:
            count = sum(1 for _ in f)
    return count

raw_to_list(oldanswers, allowedanswers, count_lines("rawwordlists/old_allowedanswers.txt")) # Exception has occurred: NameError name 'count' is not defined

raw_to_list(oldguesses, allowedguesses, count_lines("rawwordlists/old_allowedguesses.txt"))