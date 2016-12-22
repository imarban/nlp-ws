from nltk.tokenize import SExprTokenizer

expression = "(3 * 4) + ((12x * 3) * (6x + 3)) = 124"

# TODO: Complete this file to get the following output
# ['(3 * 4)', '+', '(12x * 3)', '*', '(6x + 3)', ' = 124']

def math_tokenize(expression):
    tokenizer = SExprTokenizer()
    return tokenizer.tokenize(expression)

tokenized = math_tokenize(expression)
print(tokenized)
