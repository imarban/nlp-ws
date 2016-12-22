from nltk.tokenize import word_tokenize

def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.read()

def write_file(file_name, content):
    with open(file_name, 'w') as f:
        f.write("\n".join(content))

def word_tokenizer(content):
    return word_tokenize(content)
