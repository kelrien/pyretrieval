# -*- coding: utf-8 -*-
import datetime, sys
from pyretrieval import processor, document, indexer

start = datetime.datetime.now()
print "Initializing Document Processor"
proc = processor.Processor()
#LOAD STOPWORDS
print "Loading Stopwords..."
temp_time = datetime.datetime.now()
proc.load_stopwords('german_example_files/stopwords_german', True)
print "Finished after:", str(datetime.datetime.now()-temp_time)
#LOAD LEMMAS
print "Loading Wordlist..."
temp_time = datetime.datetime.now()
proc.load_lemmas('german_example_files/wordlist_german', True)
print "Finished after:", str(datetime.datetime.now()-temp_time)
#PROCESS DOCUMENTS
print "Processing Documents"
docs = []
temp_time = datetime.datetime.now()
with open('german_example_files/german_news_example') as file:
    i = 0
    for line in file:
        i += 1
        sys.stdout.write(str(i)+'\r')
        docs.append(proc.process(line.decode("utf-8")))
print "Finished after:", str(datetime.datetime.now()-temp_time)
#INDEX DOCUMENTS
print "Indexing Documents..."
temp_time = datetime.datetime.now()
idxr = indexer.Indexer()
for doc in docs:
    idxr.index(doc)
print "Finished after:",str(datetime.datetime.now()-temp_time)
#CALCULATE INVERSE DOCUMENT FREQUENCY
temp_time = datetime.datetime.now()
print "Calculating inverse document frequency"
idxr.calculate_idfs()
print "Finished after:", str(datetime.datetime.now()-temp_time)
print "==================================="
print "Total Duration:", str(datetime.datetime.now()-start)
print "IR-SYSTEM READ ENTER QUERY AND PRESS ENTER:"
input = ""
while input is not "quit":
    string = raw_input("Query: ").decode(sys.stdout.encoding).encode("utf-8");
    query = proc.process(string)
    result = idxr.search(query)
