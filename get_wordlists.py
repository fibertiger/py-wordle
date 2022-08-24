# transforming raw .txts into items of a list that we can use later

oldanswers = open("rawwordlists/old_allowedanswers.txt","r") # allowed answers/"secret words"
allowedanswers = open("allowedanswers.json","w")

oldguesses = open("rawwordlists/old_allowedguesses.txt","r") # allowed guesses
allowedguesses = open ("allowedguesses.json","w")

def raw_to_list(oldfile, newfile, c, listname):
    # crudely creating a json file
    def transform_words():
        l = 6
        for i in range(c):
            if i == c-1: # last item in json shouldn't have a comma after it; annoying
                word = oldfile.readline(l)
                word = "  \"" + word
                word = word[:6] + "\"" + '\n'
                newfile.write(word)
                l = l + 5
            else: # if it's not the last item then we will also add a comma at the end
                word = oldfile.readline(l)
                word = "  \"" + word
                word = word[:6] + "\"" + ',\n'
                newfile.write(word)
                l = l + 5
    newfile.write("{ \n \"" + listname + "\": \n [\n")
    transform_words()
    newfile.write(" ]\n}")


def count_lines(file):
    # find out many lines/words are in a file
    # thanks to https://stackoverflow.com/questions/32607370/python-how-to-get-the-number-of-lines-in-a-text-file
    with open(file) as f: 
        for line in f:
            count = sum(1 for _ in f)
    return count

answers_count = count_lines("rawwordlists/old_allowedanswers.txt")
print(answers_count)
raw_to_list(oldanswers, allowedanswers, answers_count, "a_list") # Exception has occurred: NameError name 'count' is not defined

guesses_count = count_lines("rawwordlists/old_allowedguesses.txt")
print(guesses_count)
raw_to_list(oldguesses, allowedguesses, guesses_count, "g_list")