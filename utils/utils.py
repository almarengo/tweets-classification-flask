from utils.contractions import *
import re

def decontracted(text):
    for word in text.split():
        if word.lower() in contractions:
            text = text.replace(word, contractions[word.lower()])
    return text

def sentence_cleaning(sentence):
    # Get rid of re-tweet
    if ': ' in sentence:
        sentence = sentence.split(': ')[1]
    # Substitute of apex quote with quote
    sentence = sentence.replace('’', '\'')
    # Remove usernames mentioned with @
    sentence = re.sub(r'(@)[^\s]+', '', sentence)
    # Get rid of web-site
    sentence = re.sub(r'(?:www|https?)[^\s]+', '', sentence)
    # Run decontraction
    sentence = decontracted(sentence.lower().strip())
    # Correct spelling of verbs ending with 'in'
    sentence = re.sub(r"in(')", "ing", sentence)
    # Get rid of double puntuation
    sentence = re.sub(r"([.!?]+)\1", r"\1", sentence)
    # Space punctiations from words for splitting
    sentence = re.sub('([.,!?()])', r' \1 ', sentence)
    # Get rid of multiple spaces
    sentence = re.sub('\s{2,}', ' ', sentence)
    # Get rid of non-letter character
    sentence = re.sub(r"[^a-zA-Z']+", r" ", sentence)
    return sentence