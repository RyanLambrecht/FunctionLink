# import gensim.downloader as api
# import nltk


# model = api.load("word2vec-google-news-300")
# nltk.download('punkt')
# from nltk.tokenize import word_tokenize

#loading the file and creating the sets

# there is 83 requierments

from collections import Counter    

import nltk
from nltk.corpus import wordnet as wn

def get_synset(word):
    synsets = wn.synsets(word)
    if synsets:
        return synsets[0]
    return None

# Function to calculate similarity between two words using Wu-Palmer Similarity
def calculate_similarity(word1, word2):
    synset1 = get_synset(word1)
    synset2 = get_synset(word2)
    if synset1 and synset2:
        return synset1.wup_similarity(synset2)
    return 0

# Function to group words by similarity threshold
def group_words_by_similarity(words, threshold=0.5):
    word_dict = {}
    used_words = set()
    
    for word in words:
        if word in used_words:
            continue
        
        # Initially, the word is its own group leader
        word_dict[word] = word
        used_words.add(word)
        
        for other_word in words:
            if other_word != word and other_word not in used_words:
                similarity = calculate_similarity(word, other_word)
                if similarity and similarity >= threshold:
                    word_dict[other_word] = word  # Grouping other_word with the current word
                    used_words.add(other_word)
    
    return word_dict


FILEPATH = r'FunctionLink\textFiles\requirements-3nfr-80fr.txt'
requirements = open(FILEPATH, 'r')

content = []
for line in requirements:  # Corrected the variable name
    # Strip whitespace and check if the line contains a colon
    if ':' in line:
       
        line = line.lower()
         # Split the line at the first colon and take the part after it, then removes the '.'s
        content.append(line.split(':', 1)[1].strip().replace('.', ''))

#creating a vocabulary with only words we deem significant by if they appear in <90% of the requirements
vocab = set()
req_slim = []
for x in content:
    temp = x.split()
    req_slim.append(temp)
    vocab.update(temp)

redundancy_counter = Counter()
for x in req_slim:
    y = set(x)
    redundancy_counter.update(y)

redundant_words = []
    
for x in redundancy_counter:
    if redundancy_counter.get(x) / len(req_slim) > .9:
        redundant_words.append(x)
        
for redundant in redundant_words:
    vocab.remove(redundant)
    


# End of redundant
#start of grouping

temp = group_words_by_similarity(vocab, .76)

for word, common_word in temp.items():
    print(f"'{word}' is grouped with '{common_word}'")
    
    














