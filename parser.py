__author__ = 'Jacob Bieker'
import os
import nltk, re, pprint
from nltk.corpus import stopwords
from nltk import word_tokenize
from multiprocessing import Pool
#nltk.download()

def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences


def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
                                   if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].most_common(10)) for tag in cfd.conditions())


def find_multiple_tags(tag_prefix_list, tagged_text):
    for item in tag_prefix_list:
        tagdict = findtags(item, tagged_text)
        for tag in sorted(tagdict):
            print(tag, tagdict[tag])

dict_of_texts = {}
dict_of_freq = {}
with open("outfile.txt", "w") as output:
    for filename in os.listdir(os.path.join("primary-sources")):
        if filename == "Chronicle of Henry Huntingdon.txt" or "Anglo-Saxon Chronicle.txt":
            with open(os.path.join("primary-sources", filename)) as text:
                raw_data = text.read()
                #preprocessed = ie_preprocess(raw_data)
                processed_2 = nltk.sent_tokenize(raw_data)
                processed_1 = nltk.word_tokenize(raw_data)
                processed = nltk.pos_tag(processed_1)
                print(filename)
                print(len(raw_data))
                print(len(processed))
                output.write(filename + "\n")
                output.write("Num Characters: " + str(len(raw_data)) + "\n")
                output.write("Num Words: " + str(len(processed)) + "\n")
                output.write("Num Sentences: " + str(len(processed_2)) + "\n")
                tag_fd = nltk.FreqDist(tag for (word, tag) in processed)
                fd = nltk.FreqDist(word for (word, tag) in processed)
                print(tag_fd.tabulate())
                cfd1 = nltk.ConditionalFreqDist(processed)
                print("King")
                print(cfd1['king'].most_common())
                print("Surrounding Text: ")
                king_index = processed.index(("king", "NN"))
                print(processed[king_index-4:king_index+4])
                test_file = nltk.FreqDist(processed)
                print([wt[0] for (wt, _) in test_file.most_common(10) if wt[1] == 'VB'])
                print("Following King")
                tags = [b[1] for (a, b, c) in nltk.trigrams(processed) if a[0] == 'king']
                fd = nltk.FreqDist(tags)
                print(fd.tabulate())
                dict_of_freq[filename] = tag_fd
                dict_of_texts[filename] = processed
                output.write("\n\n")


                # After removing stopwords and punctuation
                text1 = [w.lower() for w in processed_1 if w.isalpha() and not stopwords]
                processed_2 = nltk.pos_tag(text1)
                tag_fd = nltk.FreqDist(tag for (word, tag) in processed_2)
                print(tag_fd.tabulate())



