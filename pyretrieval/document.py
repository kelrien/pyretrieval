import json
import math


class Document(object):

    def __init__(self):
        self.vector = dict()
        self.metadata = dict()

    def __getitem__(self, key):
        return self.vector.get(key, 0)

    def __setitem__(self, key, value):
        self.vector[key] = value

    def __iter__(self):
        return self.vector.itervalues()

    # calculate magnitude of document-vector
    def magnitude(self):
        temp = 0
        for value in self.vector.values():
            temp += value*value
        return math.sqrt(temp)

    # get JSON representation of the document
    def to_json(self):
        result = str(self.vector)
        return result
