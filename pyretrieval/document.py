import json

class Document(object):

    def __init__(self):
        self.vector = dict()
        self.text  = ''
        self.metadata = dict()

    def __getitem__(self,key):
        if self.vector.has_key(key):
            return self.vector[key]
        else:
            return 0
        
    def __setitem__(self,key,value):
        self.vector[key] = value
        
    def __iter__(self):
        return self.vector.itervalues()    
    
    def json(self):
        #transform object including metadata into json
        pass
