import nltk
from nltk.corpus import wordnet as wn



def get_hypernym(word):
    # Get synsets for the given word
    synsets = wn.synsets(word)
    
    # If no synsets are found, return None
    if not synsets:
        return None
    
    # Get the hypernyms of the first synset
    hypernyms = synsets[0].hypernyms()
    
    # Return the hypernym names
    return [hypernym.name().split('.')[0] for hypernym in hypernyms]

# Example usage
car_hypernyms = get_hypernym('area')
print(car_hypernyms)
