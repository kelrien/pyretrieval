# -*- coding: utf-8 -*-
import document
import re
from nltk.stem.snowball import SnowballStemmer


class Processor(object):

    def __init__(self, filter_characters='a-zA-Z0-9 ',
                 replace_characters={
                     u'\xe4': 'ae', u'\xf6': 'oe',
                     u'\xfc': 'ue', u'\xdf': 'ss'},
                 stopwords=[], lemmas=dict(), language="german"):
        self.stopwords = stopwords
        # replace characters is a dict of chars where the key
        # marks the character to be replaced with the connected value
        self.replace_characters = replace_characters
        # filter_characters is a regex that triggers on allowed characters
        self.filter_characters = filter_characters
        self.lemmas = lemmas
        if language in SnowballStemmer.languages:
            self.stemmer = SnowballStemmer(language)

    # lemmatize -> index
    def lemmatize(self, word):
        if word in self.lemmas:
            return self.lemmas[word]
        else:
            return word

    # stopwords will be ignored when tokenized
    def load_stopwords(self, file_path, do_clean=False):
        with open(file_path) as file:
            for line in file:
                line = line.decode('utf-8')
                if not line.startswith('#'):
                    if do_clean:
                        self.stopwords.append(self.clean(line))
                    else:
                        self.stopwords.append(
                            line.strip('\r').strip('\n').lower())

    # load lemmas from file
    def load_lemmas(self, file_path, do_clean=False):
        # load lemmas from file
        # a single lemma per line separated by a tabulator:
        # 'key'\t'value'
        # lines starting with # will be ignored
        file = open(file_path)
        for line in file:
            line = line.decode('utf-8')
            if '#' not in line:
                if do_clean:
                    keys = self.clean(line).split('\t')
                else:
                    keys = line.strip('\n').strip('\r').lower()
                self.lemmas[keys[0]] = keys[1]

    def clean(self, string):
        result = string.strip('\n').strip('\r').lower()
        for char in self.replace_characters.keys():
            result = result.replace(char, self.replace_characters[char])

        return result

    # tokenize -> stem
    def tokenize(self, string):
        temp = string.lower()

        # clean string
        temp = self.clean(temp)

        # FIND A SMART WAY TO INCORPORATE THIS IN THE CLEAN FUNCTION
        # remove unwanted characters
        temp = re.sub(r'[^{0}]'.format(self.filter_characters), ' ', temp)

        result = temp.split()
        return result

    # stem -> index
    def stem(self, word):
        result = self.stemmer.stem(word)
        return result

    # index -> done
    def process(self, string, lemmatize=True):
        ''' instead of a flag use the stemmer 
        whenever the lemmas dict is empty? '''
        result = document.Document()
        result.metadata["original"] = string
        tokens = self.tokenize(string)
        for token in tokens:
            if lemmatize:
                token = self.lemmatize(token)
            else:
                token = self.stem(token)
            if token not in self.stopwords:
                if token in result.vector:
                    result.vector[token] += 1
                else:
                    result.vector[token] = 1
        return result
