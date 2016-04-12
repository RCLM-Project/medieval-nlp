__author__ = 'Jacob Bieker'
import os
import nltk, re, pprint
from nltk import word_tokenize
#nltk.download()


def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences

annals_of_roger = open(os.path.join("primary-sources", "annalsofrogerdeh01hoveuoft_djvu.txt"))
raw_rogers = annals_of_roger.read()

itinerary_through_ireland = open(os.path.join("primary-sources", "itinerarythroug00girauoft_djvu.txt"))
raw_ireland = itinerary_through_ireland.read()

# NLTK testing
processed_roger = ie_preprocess(raw_rogers)
processed_ireland = ie_preprocess(raw_ireland)



