class Document(object):

    def __init__(self):
        self.vector = dict()
        self.metadata = dict()

    def __getitem__(self,index):
        return self.metadata[index]
        
    def __setitem__(self,index,value):
        self.metadata[index] = value
        
    def json(self):
        #transform object including metadata into json
        pass
       
    
