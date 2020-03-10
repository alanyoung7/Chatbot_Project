import nltk
from nltk.corpus import wordnet as wn
from PyDictionary import PyDictionary
dictionary = PyDictionary()

from profanity_check import predict, predict_prob

# Enter your input here
words= input("Enter words: ")
a = words
single_words = a.split(' ')
print((single_words))

predict_prob(single_words)

# Threshold defined for profanity check
threshold =0.2
op = predict_prob(single_words)
print(op)

# Method 1: Check profanity using profanity checker
for i in range(len(op)):
    if op[i]>=threshold:
        print(single_words[i])

# Method 2: For better accuracy checking profanity words in profanity list
file = open("profanity_words.txt","r") 
file = file .readlines()
for i in range(len(file)):
    for j in range(len(single_words)):
        file[i] = file[i].strip()
        single_words[j] = single_words[j].strip()
        if(file[i] == single_words[j]):
            print("profanity exists in word: ",single_words[j])
    


        