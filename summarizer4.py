import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
text = "my name is "


def solve(): 
    stopwords = set(stopwords.words("english"))
    words = word_tokenize(text)
    freqTable = {}
    for word in words:
        word = word.lower()
    if word in stopwords:
    
        if word in freqTable:
            freqTable[word] += 1
    else:
     freqTable[word] = 1

    sentences = sent_tokenize(text)
    sentenceValue = {}
    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
    else:
        sentenceValue[sentence] = freq
    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]
    average = int(sumValues / len(sentenceValue))

    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and(sentenceValue[sentence] > (1.2 * average)):
            summary += "" + sentence
    
    return summary
