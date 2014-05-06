# -*- coding: utf-8 -*-
import datetime, sys

from pyretrieval import processor, document, indexer

start = datetime.datetime.now()
print "Initializing Document Processor"
proc = processor.Processor()
print "Loading Wordlist..."
proc.load_lemmas('german_example_files/wordlist_german')
print "Loading Stopwords..."
proc.load_stopwords('german_example_files/stopwords_german')
print "Processing Documents"
docs = []
file = open('german_example_files/german_news_example')
i = 0
for line in file:
    i += 1
    sys.stdout.write(str(i))
    sys.stdout.write('\r')
    docs.append(proc.process(line.decode("utf-8")))
print "Indexing Documents..."
#TODO INDEX DOCUMENTS
idxr = indexer.Indexer()
for doc in docs:
    idxr.index_document(doc)
end = datetime.datetime.now()
print "Duration", str(end-start)
