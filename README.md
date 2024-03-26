# Generation-of-Ngram-Language-Model-for-Language-Detection
Generate an Ngram model and use the model for Language Detection for a list of sentences given as input data from a file. English, French and Italian languages are used here.

algorithm2a:
It basically creates the dictionary of unigram and bigram data that will be stored using pickle.

to execute: python3 algorithm2a.py

algorithm2b:
It reads the pickle dictionary for all 3 languages and uses the data to calculate the probability of a sentence belonging to a language.
It stores the language that has the maximum probability for that sentence.

Accuracy : 97.67%

to execute : python3 algorithm2b.py
