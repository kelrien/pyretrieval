import document
import re

class Processor(object):

    def __init__(self, filter_characters = 'a-zA-Z0-9', stopwords = [], lemmas = dict()):
        self.stopwords = stopwords
        #filter_characters is a regex that triggers on allowed characters
        self.filter_characters = filter_characters
        self.lemmas = lemmas
                
    #lemmatize -> index                   
    def lemmatize(self,word):
        if word in self.lemmas:
            return self.lemmas[word]
        else:
            return None
                        
    #stopwords will be ignored when tokenized
    def load_stopwords(self,file_path):
        file = open(file_path)
        for line in file:
            if not line.startswith('#'):
                stopwords.append(line.strip('\n').lower())
    
    def load_lemmas(self,file_path):
        # load lemmas from file
        # a single lemma per line separated by a tabulator:
        # 'key'\t'value'
        # lines starting with # will be ignored
        file = open(file_path)
        for line in file:
            line = line.decode('utf-8')
            if not line.startswith(u'#'):
                keys = line.strip('\n').lower().split('\t')
                self.lemmas[keys[0]] = keys[1]
                
    #tokenize -> stem
    def tokenize(string):
        result = []
        #replace every character that is not allowed
        result = re.sub(r'[^.{0}]'.format(filter_characters), ' ', string).split()
        return result
    
    #stem -> index    
    def stem(word):
        pass
    
    #index -> done
    def index(tokens):
        result = document.Document()
        for token in tokens:
            if token in result.vector:
                result.vector[token] += 1
            else:
                result.vector[token] = 0
