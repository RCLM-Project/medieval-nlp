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

dict_of_texts = {}
dict_of_freq = {}
with open("outfile.txt", "w") as output:
    for filename in os.listdir(os.path.join("primary-sources")):
        if filename == "Chronicle of Henry Huntingdon.txt" or "Anglo-Saxon Chronicle.txt":
            with open(os.path.join("primary-sources", filename)) as text:
                raw_data = text.read()
                #preprocessed = ie_preprocess(raw_data)
                processed_1 = nltk.word_tokenize(raw_data)
                processed = nltk.pos_tag(processed_1)
                print(filename)
                print(len(raw_data))
                print(len(processed))
                output.write(filename + "\n")
                tag_fd = nltk.FreqDist(tag for (word, tag) in processed)
                fd = nltk.FreqDist(word for (word, tag) in processed)
                print(tag_fd.tabulate())
                king_count = raw_data.count("king") / len(processed)
                army_count = raw_data.count("army") / len(processed)
                print("King Percentage: " + str(king_count))
                print("Army Percentage: " + str(army_count))
                died_count = raw_data.count("died") / len(processed)
                print("Died Percentage: " + str(died_count))
                year_count = raw_data.count("year") / len(processed)
                print("Year Percentage: " + str(year_count))
                cfd1 = nltk.ConditionalFreqDist(processed)
                print("King")
                print(cfd1['king'].most_common())
                print("Surrounding Text: ")
                king_index = processed.index(("king", "NN"))
                print(processed[king_index-4:king_index+4])
                test_file = nltk.FreqDist(processed)
                print([wt[0] for (wt, _) in test_file.most_common(10) if wt[1] == 'VB'])

                print("Following King")
                tags = [b[1] for (a, b) in nltk.bigrams(processed) if a[0] == 'king']
                fd = nltk.FreqDist(tags)
                print(fd.tabulate())

                #tag_fd.plot()
                tagdict_nn = findtags('NN', processed)
                for tag in sorted(tagdict_nn):
                    print(tag, tagdict_nn[tag])
                    output.write(str(tag) + " ".join(str(s) for s in tagdict_nn[tag]) + "\n")
                tagdict_pr = findtags('PR', processed)
                for tag in sorted(tagdict_pr):
                    print(tag, tagdict_pr[tag])
                    output.write(str(tag) + " ".join(str(s) for s in tagdict_pr[tag]) + "\n")
                tagdict_jj = findtags('JJ', processed)
                for tag in sorted(tagdict_jj):
                    print(tag, tagdict_jj[tag])
                    output.write(str(tag) + " ".join(str(s) for s in tagdict_jj[tag]) + "\n")
                    tagdict_vb = findtags('VB', processed)
                for tag in sorted(tagdict_vb):
                    print(tag, tagdict_vb[tag])
                    output.write(str(tag) + " ".join(str(s) for s in tagdict_vb[tag]) + "\n")
                dict_of_freq[filename] = tag_fd
                dict_of_texts[filename] = processed
                output.write("\n\n")


                # After removing stopwords and punctuation
                text1 = [w.lower() for w in processed_1 if w.isalpha() and not stopwords]
                processed_2 = nltk.pos_tag(text1)
                tag_fd = nltk.FreqDist(tag for (word, tag) in processed_2)
                print(tag_fd.tabulate())
                tagdict_nn = findtags('NN', processed_2)
                for tag in sorted(tagdict_nn):
                    output.write(str(tag) + " ".join(str(s) for s in tagdict_nn[tag]) + "\n")
                tagdict_pr = findtags('PR', processed_2)
                for tag in sorted(tagdict_pr):
                    output.write(str(tag) + " ".join(str(s) for s in tagdict_pr[tag]) + "\n")
                tagdict_jj = findtags('JJ', processed_2)
                for tag in sorted(tagdict_jj):
                    output.write(str(tag) + " ".join(str(s) for s in tagdict_jj[tag]) + "\n")



