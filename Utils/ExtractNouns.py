from Lib.Libraries import *

def extract_nouns(sentence):
    # Tokenize the sentence into words
    words = word_tokenize(sentence)  
    # Tag each word with a part-of-speech tag
    pos_tags = pos_tag(words)   
    # Extract nouns (NN, NNS, NNP, NNPS)
    nouns = [word for word, tag in pos_tags if tag in ('NN', 'NNS', 'NNP', 'NNPS')]   
    return ' '.join(nouns)