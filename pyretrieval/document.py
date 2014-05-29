import json
import math


class Document(object):

    def __init__(self):
        self.vector = dict()
        self.metadata = dict()

    def __getitem__(self, key):
        if key in self.vector.keys():
            return self.vector[key]
        else:
            return 0

    def __setitem__(self, key, value):
        self.vector[key] = value

    def __iter__(self):
        return self.vector.itervalues()

    def magnitude(self):
        temp = 0
        for value in self.vector.values():
            temp += value*value
        return math.sqrt(temp)

    def json(self):
        # transform object including metadata into json
        pass
