import pickle as pkl
import random as rnd
from get_wordlists import a_count

a_file = open('allowed_answers.pkl', 'rb')
a_list = pkl.load(a_file)
a_file.close()

r = rnd.randrange(0, a_count)
secret_word = a_list[r]