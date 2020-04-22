from nltk.corpus import wordnet as wn
import csv

# Read the contents of the file
with open('violation.csv', 'r') as csv_file:
    lines = csv.reader(csv_file, delimiter='\n')
    
    word_list = []
    for line in lines:
        line = line[0].lower()
        word_list.append(line)
    
    # Sentece fetched from alexa
    sentence = "I like beer"
    
    # Clean the text for matching purposes
    sentence = sentence.lower()
    
    # Remove any special symbols
    for letters in sentence:
        if letters in "`~!@#$%^&*()_-+|{}[]<>?/\=\"\':,;.0123456789":
            sentence = sentence.replace(letters,"")
    
    sent= []
    sent = sentence.split()
    arr = []
    
    # Check if the word from sentence exists in wordnet
    for word in sent:
        if(wn.synsets(word)==[]):
            continue
        word_syn = wn.synsets(word)
        word_syn = word_syn[0]
        
        # Fetch all the synonyms of that word
        word_lemma = word_syn.lemma_names()
        print("words in lemma for:",word," is ",word_lemma)
        for item in word_lemma:
            # Match the synonyms and check if they exists in our violation list
            for line in word_list:
                if(item==line):
                    print("violated:",item)
                else:
                    continue
                    
                    
                
    
    
