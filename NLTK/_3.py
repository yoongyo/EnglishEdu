import nltk
from nltk.tokenize import PunktSentenceTokenizer

document = input()
sentences = nltk.sent_tokenize(document)
for sent in sentences:
    print(nltk.pos_tag(nltk.word_tokenize(sent)))
