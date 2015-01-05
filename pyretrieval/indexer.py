import document
import math
import operator


class Indexer(object):

    def __init__(self):
        self.inv_index = dict()
        self.doc_count = 0
        self.idfs = dict()

    # Add a document to the inverted index
    def index(self, document, adjust_idf=True):
        self.doc_count += 1

        for word in document.vector:
            if word in self.inv_index:
                self.inv_index[word].append(document)
            else:
                self.inv_index[word] = [document]

        if adjust_idf:
            pass

    # Query the indexer for an ordered (limited) list of similar
    # documents
    def search(self, query_document, limit=0):
        
        result = dict()
        documents = []

        for word in query_document.vector.keys():
            documents += self.inv_index.get(word, [])
        documents = set(documents)
        for doc in documents:
            result[doc] = self.compare(query_document, doc)

        # Sort the documentlist
        result = sorted(result.iteritems(), key=operator.itemgetter(1),
               reverse=False)
        
        # return the limited output
        if limit > 0:
            result=result[0:limit]
        return result

    # Compare two documents and return the similarity by angle
    def compare(self, docx, docy):
        # merge document vector keys without duplicates
        words = set(docx.vector.keys() + docy.vector.keys())
        # if document vectors share no dimension(word) they cannot be similar
        if len(words) >= len(docx.vector.keys()) + len(docy.vector.keys()):
            return 90

        numerator = 0.0
        for word in words:
            numerator += docx.vector.get(word, 0) * docy.vector.get(word, 0)

        denominator = docx.magnitude() * docy.magnitude()

        result = numerator / denominator

        # remove problable computational errors
        result = min(1, max(result, -1))

        # get the angle in radians
        result = math.acos(result)

        # convert radians to degrees
        result = math.degrees(result)
        return result

    # Set current (calculated) idf values in documents
    def set_idfs(self):
        for index in self.inv_index.keys():
            for doc in self.inv_index[index]:
                doc.vector[index] = doc.vector[x] * self.idfs.get(ind, 1)

    # Calculate inverse document frequency for every word in the inverted index
    def calc_idfs(self):
        for word, documents in self.inv_index.iteritems():
            idf = math.log((self.doc_count / len(documents)))
            self.idfs[word] = idf
