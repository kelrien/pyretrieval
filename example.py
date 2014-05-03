# -*- coding: utf-8 -*-
import datetime, sys

from pyretrieval import processor, document

print "Initializing Document Processor"
proc = processor.Processor()
print "Loading Wordlist..."
proc.load_lemmas('pyretrieval/wordlist_german')
print "Loading Stopwords..."
proc.load_stopwords('pyretrieval/stopwords_german')
print "Processing Documents"
docs = []
file = open('pyretrieval/german_news_example')
i = 0
for line in file:
    i += 1
    sys.stdout.write(str(i))
    sys.stdout.write('\r')
    docs.append(proc.process(line))
print "Indexing Documents..."
#TODO INDEX DOCUMENTS
