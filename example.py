import datetime

from pyretrieval import processor, document

print "Initializing Document Processor"
proc = processor.Processor()
print "Loading Wordlist..."
proc.load_lemmas('pyretrieval/wordlist_german')
print "Loading Stopwords..."
proc.load_stopwords('pyretrieval/stopwords_german')
testdoc = proc.index(u"Ein erster Test der zeigen soll, wie das indexieren dieser Bibliotheken funktioneren koennte")
