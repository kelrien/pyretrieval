import document
import math

class Indexer(object):

    def __init__(self):
        self.inv_index = dict()
        self.doc_count = 0
        self.idfs = dict()

    #Add a document to the inverted index
    def index(self, document):
        self.doc_count += 1
        for word in document.vector:
            if self.inv_index.has_key(word):
                self.inv_index[word].append(document)
            else:
                self.inv_index[word] = [document]

    #Query the indexer for an ordered (limited) list of similar documents
    def search(self, query_document, limit = -1):
        result = dict()
        documents = []
        for word in query_document.vector.keys():
            documents += self.inv_index.get(word,[])
        documents = set(documents)
        for doc in documents:
            result[doc] = self.compare(query_document, doc)
        return result
    
    def compare(self, docx, docy):
        #merge document vector keys without duplicates
        words = set(docx.vector.keys() + docy.vector.keys())
        #if document vectors share no dimension(word) they cannot be similar
        if len(words) >= len(docx.vector.keys()) + len(docy.vector.keys()):
            return 1
        numerator = 0.0
        denominator = docx.magnitude() * docy.magnitude()
        print denominator
        for word in words:
            idf = self.idfs.get(word,1) 
            idf = idf * idf
            numerator += docx.vector.get(word, 0)*docy.vector.get(word,0)*idf
        result = numerator / denominator 
        return result
         
        
    def calculate_idfs(self):
        for word in self.inv_index.keys():
            idf = math.log((self.doc_count / len(self.inv_index[word])))
            self.idfs[word] = idf
