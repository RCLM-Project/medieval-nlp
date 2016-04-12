__author__ = 'Jacob Bieker'
import os
import nltk, re, pprint
from nltk import word_tokenize
from multiprocessing import Pool
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
        #processed = ie_preprocess(raw_data)
        processed_1 = nltk.word_tokenize(raw_data)
        processed = nltk.pos_tag(processed_1)
        print(processed[0])
        tag_fd = nltk.FreqDist(tag for (word, tag) in processed)
        print(tag_fd.most_common())
        tag_fd.plot(cumulative=True)
        dict_of_texts[filename] = processed

with open("outfile.txt", "w") as output:
    for item in dict_of_texts:
        print(item)
        output.write('\n'.join('%s %s' % x for x in dict_of_texts[item]))




