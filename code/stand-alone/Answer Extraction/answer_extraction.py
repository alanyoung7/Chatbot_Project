#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 15:12:30 2020

@author: parth
"""

from nltk.corpus import wordnet 
import numpy as np
import nltk
from nltk.corpus import treebank
from nltk.corpus import wordnet as wn
try:
    abc = []    # Used for converting the tpye of elements from set to list
    filter1 = []  # Words with similarity greater than the threshold will be appended to it
    
    sentence ="Where do you want to go moon, india or usa"
    
    # Prepocess the given text by splitiing it into individual sentences, converting to lower case, remving extra spaces and special symbols
    lines = sentence.split(".")
    sentence = sentence.lower()
    sentence = sentence.strip()
    for letters in sentence:
    		if letters in "`~!@#$%^&*()_-+|{}[]<>?/\=\"\':,;.0123456789":
    			sentence = sentence.replace(letters," ")
    
    #Check for parts of speech for the remaining words
    tokens = nltk.word_tokenize(sentence) 
    tagged = nltk.pos_tag(tokens)
    entities = nltk.chunk.ne_chunk(tagged)
    
    # Remove stopwords from the list
    stop_filename = 'StopWords.txt'
    with open(stop_filename, 'r', encoding='unicode-escape') as stop_filename:
    	stop_file = [stop.rstrip('\n') for stop in stop_filename]
    
    print(sentence,"\n")
      
    tokens = set(tokens)-set(stop_file)
    print(tokens, "\n")
    for x in tokens:
        abc.append(x)
        
    '''
    
    for x in range(len(tokens)-1):
        
        syn1 = wordnet.synsets(x)[0] 
        syn2 = wordnet.synsets(x)[0] 
        #str1 = tokens[x]
        #str2 = tokens[x+1]
        #print(type(str1))
        
        #yn1 = wordnet.synsets(str1)
        #print(str1)
        #syn2 = wordnet.synsets(str2)
        #print(str2)
        
        #sim= syn1.wup_similarity(syn2)
        #print(sim)
        #print(syn1)
        #print(type(syn1.wup_similarity(syn2)))
        #print(syn1.wup_similarity(syn2))
    '''   
    
    
    #Use this block for testing (to check whether the word is supported by wordnet or not) 
    '''
    #print(tokens[10])
    syn1 = wordnet.synsets('drive')[0]
    syn2 = wordnet.synsets('go')[0] 
    print(type(syn1),type(syn2)) 
    #print ("hello name :  ", syn1.name()) 
    #print ("selling name :  ", syn2.name()) 
    print(syn1.wup_similarity(syn2))
    '''
    max_sim = 0
    ###################
    for x in range(0,len(abc)):
        syn1 = wordnet.synsets(abc[x])
        if((len(syn1))>0):
            syn1 = wordnet.synsets(abc[x])[0]
        elif(syn1==[]):
            file = open("StopWords.txt","a+")
            flag1 = 0
            for i in file:
                if(i==abc[x]):
                    flag1 = 1
                    break
            if flag1==1:
                abc[x] += "\n"
                file.write(abc[x])
            print(abc[x]," does not exist in wordnet")
            continue
        else:
            syn1 = wordnet.synsets(abc[x])
        for y in range(1,len(abc)):
            if(x!=y):
                syn2 = wordnet.synsets(abc[y])
                
                if((len(syn2))>0):
                    syn2 = wordnet.synsets(abc[y])[0]
                elif(syn2==[]):
                    file = open("StopWords.txt","a+")
                    flag2 = 0
                    for j in file:
                        if(j==abc[y]):
                            flag2 = 1
                            break
                    if flag2==1:
                        abc[y] += "\n"
                        file.write(abc[y])
                    print(abc[y]," does not exist in wordnet")
                    continue
                else:
                    syn2 = wordnet.synsets(abc[y])
                print(syn1,syn2)
                sim = syn1.wup_similarity(syn2)
                print(sim)
                
                if(sim==None):
                    sim = 0
                if (sim > max_sim):
                    max_sim = sim
                    word1 = abc[x]
                    word2 = abc[y]
                    print(word1,word2)
            else:
                continue
                    
    filter1.append(word1)
    filter1.append(word2)
                    
    print("\n",filter1)
    file.close()

except Exception as e:
    print("\n",e)
