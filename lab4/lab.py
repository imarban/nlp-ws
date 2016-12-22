from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer

def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.read().splitlines()


def porter_stem(content):
    stemmer = PorterStemmer()
    stemmed = [stemmer.stem(word) for word in content]
    return stemmed

def snowball_stem(content, language):
    stemmer = SnowballStemmer(language)
    stemmed = [stemmer.stem(word) for word in content]
    return stemmed

def english_input():
    content = read_file("input_en.txt")
    print(snowball_stem(content, 'english'))

def spanish_input():
    content = read_file("input_es.txt")
    print(snowball_stem(content, 'spanish'))


# spanish_input()
