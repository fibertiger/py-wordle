import pickle

pickle_answer = open('old_allowedanswers.txt', 'rb')
emp = pickle.load(pickle_answer)
print(emp)