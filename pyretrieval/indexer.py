import document

class Indexer(object):

    def __init__(self):
        self.inv_index = dict()

    #Add a document to the inverted index
    def index_document(self, document):
        for word in document.vector:
            if self.inv_index.has_key(word):
                self.inv_index[word].append(document)
            else:
                self.inv_index[word] = [document]

    #Query the indexer for an ordered (limited) list of similar documents
    def search(query, limit = -1):
        pass
