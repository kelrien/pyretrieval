from pyretrieval import processor, document

proc = processor.Processor()
proc.load_lemmas('pyretrieval/wordlist_german')
for lemma in proc.lemmas:
    print lemma