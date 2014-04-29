import document

class Indexer(object):

    def __init__(self):
        self.inv_index = dict()
        pass

    def index_documents(self, documents):
        for document in documents:
            for word in document:
                if self.inv_index.has_key(word):
                    self.inv_index[word].append(document)
                else:
                    self.inv_index[word] = [document]