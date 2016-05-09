__author__ = 'Jacob Bieker'
import os, sys
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
    big_tagdict = []
    for item in tag_prefix_list:
        tagdict = findtags(item, tagged_text)
        for tag in sorted(tagdict):
            print(tag, tagdict[tag])
        big_tagdict.append(tagdict)
    return big_tagdict

dict_of_texts = {}
dict_of_freq = {}
total_words = 0
total_sentences = 0

#sys.stdout = open("print-outfile.txt", "w")
with open("outfile.txt", "w") as output:
    for filename in os.listdir(os.path.join("primary-sources")):
        with open(os.path.join("primary-sources", filename)) as nltk_text:
            print(filename)
            raw_data = nltk_text.read()
            # After removing stopwords and punctuation do analysis again
            processed_2 = nltk.sent_tokenize(raw_data)
            processed_1 = nltk.word_tokenize(raw_data)
            processed = nltk.pos_tag(processed_1)
            #text = nltk.Text(ie_preprocess(raw_data))
            #text_lower = nltk.Text(ie_preprocess([word.lower() for word in raw_data]))
            output.write(filename + "\n")
            output.write("Num Characters: " + str(len(raw_data)) + "\n")
            output.write("Num Words: " + str(len(processed)) + "\n")
            total_words += len(processed)
            output.write("Num Sentences: " + str(len(processed_2)) + "\n")
            total_sentences += len(processed_2)
            tag_fd = nltk.FreqDist(tag for (word, tag) in processed)
            fd = nltk.FreqDist(word for (word, tag) in processed)
            dict_of_freq[filename] = tag_fd
            dict_of_texts[filename] = processed
            output.write("\n\n")
            wanted_tags = ["NN", "JJ", "VB"]
            tag_list = find_multiple_tags(wanted_tags, processed)
            king_count = (raw_data.lower().count("king") + raw_data.lower().count("kings")) / len(processed)
            print("Ratio of King and kings to words: " + str(king_count))
            print("\n\n")

    output.write("Total words: " + str(total_words))
    output.write("Total Sentences: " + str(total_sentences))
