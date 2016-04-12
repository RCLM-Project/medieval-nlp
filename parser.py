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

dict_of_texts = {}
for filename in os.listdir(os.path.join("primary-sources")):
    with open(os.path.join("primary-sources", filename)) as text:
        raw_data = text.read()
        processed = ie_preprocess(raw_data)
        dict_of_texts[filename] = processed






