# Check http://www.nltk.org/api/nltk.tokenize.html#module-nltk.tokenize.simple

from nltk.tokenize.simple import SpaceTokenizer

with open("input.txt") as f:
    content = f.read()

def space_tokenize(content):
    tokenizer = SpaceTokenizer()
    return tokenizer.tokenize(content)

def line_tokenizer(content):
    # TODO:  Write method to tokenize by lines and call it
    pass

tokenized = space_tokenize(content)
print(tokenized)
