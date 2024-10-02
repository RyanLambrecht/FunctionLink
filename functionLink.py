# import gensim.downloader as api
# import nltk


# model = api.load("word2vec-google-news-300")
# nltk.download('punkt')
# from nltk.tokenize import word_tokenize

#loading the file and creating the sets

def tokenize() ->:
    

FILEPATH = r'textFiles\requirements-3nfr-80fr.txt'
requirements = open(FILEPATH, 'r')

content = []
for line in requirements:  # Corrected the variable name
    # Strip whitespace and check if the line contains a colon
    if ':' in line:
        # Split the line at the first colon and take the part after it, then removes the '.'s
        content.append(line.split(':', 1)[1].strip().replace('.', ''))

vocab = set()

for x in content:
    vocab.update(x.split())  
    



