# -*- coding: utf-8 -*-
import datetime
import sys
import os
import optparse
from pyretrieval import processor, document, indexer

if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option("-s", "--stopwords", dest="stopwords")
    parser.add_option("-l", "--lemmas", dest="lemmas")
    parser.add_option("-d", "--documents", dest="documents")
    (options, args) = parser.parse_args()

    start = datetime.datetime.now()
    print "Initializing Document Processor"
    proc = processor.Processor()

    # LOAD STOPWORDS
    print "Loading Stopwords..."
    temp_time = datetime.datetime.now()
    proc.load_stopwords(options.stopwords, True)
    print "Finished after:", str(datetime.datetime.now() - temp_time)

    # LOAD LEMMAS
    print "Loading Lemmas..."
    temp_time = datetime.datetime.now()
    proc.load_lemmas(options.lemmas, True)
    print "Finished after:", str(datetime.datetime.now() - temp_time)

    # PROCESS DOCUMENTS
    print "Processing Documents"
    docs = []
    temp_time = datetime.datetime.now()
    with open(options.documents) as file:
        i = 0
        for line in file:
            i += 1
            sys.stdout.write(str(i) + '\r')
            doc = proc.process(line.decode("utf8"))
            docs.append(doc)
    print "Finished after:", str(datetime.datetime.now() - temp_time)

    # INDEX DOCUMENTS
    print "Indexing Documents..."
    idxr = indexer.Indexer()
    temp_time = datetime.datetime.now()
    for doc in docs:
        idxr.index(doc)
    print "Finished after:", str(datetime.datetime.now() - temp_time)

    # CALCULATE INVERSE DOCUMENT FREQUENCY
    # temp_time = datetime.datetime.now()
    # print "Calculating inverse document frequency"
    # idxr.calc_idfs()
    # print "Finished after:", str(datetime.datetime.now()-temp_time)
    # print "==================================="
    # print "Total Duration:", str(datetime.datetime.now()-start)

    # IR SYSTEM READY
    print "IR-SYSTEM READY ENTER QUERY AND PRESS ENTER:"
    string = ""
    while string != "quit":
        print "==============================================================="
        print "==============================================================="
        string = raw_input("Query: ").decode(sys.stdout.encoding)
        query = proc.process(string)
        result = idxr.search(query, 5)
        print query.to_json()
        for kv in result:
            print kv[1], kv[0].to_json()
            print kv[0].metadata["original"]
            print ""
