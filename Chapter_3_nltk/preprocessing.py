# Preprocessing Example
# Karen Mazidi
# September 2018

import nltk
from nltk import word_tokenize
from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
import re


def preprocess(raw_text):
    """
        Preprocess raw tex.
        Arguments: a raw text string
        Output:
            text - raw_text with punctuation and numbers removed, lower cased
            tokens - tokens
            stemmed - stemmed words
            lemmas - lemmas
            content - tokens with stop words removed
    """

    # remove punctuation and numbers with a regular expression
    text = re.sub(r'[.?!,:;()\-\n\d]',' ', raw_text.lower())

    # tokenizing extracts words, not white space
    tokens = nltk.word_tokenize(text)

    # stemming removes affixes from words.
    stemmer = PorterStemmer()
    stemmed = [stemmer.stem(t) for t in tokens]

    # lemmatization finds the root words
    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(t) for t in tokens]

    # removing stopwords
    stop_words = set(stopwords.words('english'))
    content = [t for t in tokens if not t in stop_words]
    return text, tokens, stemmed, lemmas, content


def driver():
    raw_text = """ I teach at the University of Texas at Dallas. I
     started teaching there in 2016. As of Summer 2018, UTD is
     the fourth largest computer science department in the country.!"""

    text, tokens, stemmed, lemmas, content = preprocess(raw_text)
    print('\nUnprocessed text:\n\t', raw_text)
    print('\nPunctuation and numbers removed:\n\t', text)
    print('\nTokens:\n\t', tokens)
    print('\nStems:\n\t', stemmed)
    print('\nLemmas:\n\t', lemmas)
    print('\nStopwords removed:\n\t', content)

if __name__ == "__main__":
    driver()


