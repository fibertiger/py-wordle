# transforming raw .txts into items of a list that we can use later
import pickle as pkl

oldanswers = open("rawwordlists/old_allowedanswers.txt","r") # allowed answers/"secret words"
oldguesses = open("rawwordlists/old_allowedguesses.txt","r") # allowed guesses


def raw_to_list(oldfile, c):
    new_list = []
    # crudely creating a list
    l = 6
    for i in range(c):
        word = oldfile.readline(l)[:5]
        new_list.append(word)
        l = l + 5
    return new_list

def count_lines(file):
    # find out many lines/words are in a file; thanks to https://stackoverflow.com/questions/32607370/python-how-to-get-the-number-of-lines-in-a-text-file
    with open(file) as f: 
        for line in f:
            count = sum(1 for _ in f)
    return count

a_count = count_lines("rawwordlists/old_allowedanswers.txt")
a_list = raw_to_list(oldanswers, a_count)
a_file = open('allowed_answers.pkl', 'wb')
pkl.dump(a_list, a_file)
a_file.close()

g_count = count_lines("rawwordlists/old_allowedguesses.txt")
g_list = raw_to_list(oldguesses, g_count)
g_file = open('allowed_guesses.pkl', 'wb')
pkl.dump(g_list, g_file)
g_file.close()

i_count = a_count + g_count
i_list = a_list + g_list # creating a list to be able to check all inputs
i_file = open('allowed_input.pkl', 'wb')
pkl.dump(i_list, i_file)
i_file.close()