from nltk.tokenize.punkt import PunktSentenceTokenizer
import nltk.data

with open("input.txt") as f:
    content = f.read()

def default_tokenize(content):
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    return sent_detector.tokenize(content)

def sentence_tokenizer(content):
    tokenizer = PunktSentenceTokenizer()
    # TODO: Complete method
    pass

tokenized = default_tokenize(content)
print("\n".join(tokenized))
