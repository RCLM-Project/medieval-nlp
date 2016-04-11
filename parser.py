__author__ = 'Jacob Bieker'
import os
import nltk, re, pprint
from nltk import word_tokenize
nltk.download()

source = open(os.path.join("primary-sources", "annalsofrogerdeh01hoveuoft_djvu.txt"))
raw = source.read()

# NLTK testing
tokens = word_tokenize(raw)
tagged = nltk.pos_tag(raw)