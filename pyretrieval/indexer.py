import document
import math

class Indexer(object):

    def __init__(self):
        self.inv_index = dict()
        self.doc_count = 0

    #Add a document to the inverted index
    def index(self, document):
        self.doc_count += 1
        for word in document.vector:
            if self.inv_index.has_key(word):
                self.inv_index[word].append(document)
            else:
                self.inv_index[word] = [document]

    #Query the indexer for an ordered (limited) list of similar documents
    def search(query, limit = -1):
        pass

    def calculate_idf(self):
        result = dict()
        for word in self.inv_index.keys():
            idf = math.log((self.doc_count / len(self.inv_index[word])))
            result[word] = idf
        return result
