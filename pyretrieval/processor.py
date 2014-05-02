import document
import re

class Processor(object):

    def __init__(self, filter_characters = 'a-zA-Z0-9 ', replace_characters = dict(),  stopwords = [], lemmas = dict()):
        self.stopwords = stopwords
        #replace characters is a dict of chars where the key marks the character to be replaced with the connected value
        self.replace_characters = replace_characters
        #filter_characters is a regex that triggers on allowed characters
        self.filter_characters = filter_characters
        self.lemmas = lemmas
                
    #lemmatize -> index                   
    def lemmatize(self,word):
        if word in self.lemmas:
            return self.lemmas[word]
        else:
            return word
                        
    #stopwords will be ignored when tokenized
    def load_stopwords(self,file_path):
        file = open(file_path)
        for line in file:
            line = line.decode('utf-8')
            if not line.startswith('#'):
                self.stopwords.append(line.strip('\n').strip('\r').lower())
    
    def load_lemmas(self,file_path):
        # load lemmas from file
        # a single lemma per line separated by a tabulator:
        # 'key'\t'value'
        # lines starting with # will be ignored
        file = open(file_path)
        for line in file:
            line = line.decode('utf-8')
            if not '#' in line:
                keys = line.strip('\n').strip('\r').lower().split('\t')
                self.lemmas[keys[0]] = keys[1]
                
    #tokenize -> stem
    def tokenize(self, string):
        result = []
        temp = string.lower()
        #replace characters
        for char in self.replace_characters.keys():
            temp = temp.replace(char, self.replace_characters[char])          
        #remove unwanted characters
        temp = re.sub(r'[^.{0}]'.format(self.filter_characters), '', temp)
        result = temp.split()
        return result
    
    #stem -> index    
    def stem(word):
        return word
    
    #index -> done
    def index(self, string, lemmatize = True):
        result = document.Document()
        result.metadata["original"] = string
        tokens = self.tokenize(string)
        for token in tokens:
            if lemmatize:
                token = self.lemmatize(token)
            else:
                token = stem(token)
            if token in result.vector:
                result.vector[token] += 1
            else:
                result.vector[token] = 1
        return result
