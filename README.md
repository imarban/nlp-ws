# Natural Language Processing and NLTK Workshop

## Slides
[Slides link](https://goo.gl/EahEfv)


## Install required tools
- Run ```pip install nltk```. If you don't have installed ```pip``` (why?) then run ```easy_install nltk```
- Run ```pip install numpy```. This will install ```numpy``` package

## Install NLTK data
1. Open an interactive shell for Python. Run ```python```
2. Write ```import nltk``` and press ENTER
3. Write ```nltk.download()``` and press ENTER
4. An interactive installer will open. Select the corpus that you want to work with (Book).

## Lab 1. Explore data sets in NLTK

1. Open lab1 folder
2. Run each file existing there.
  - For movies file you will have to download Movie Reviews Corpora
3. Explore some of the following functions in each corpus
  - words
  - raw
  - fileids
  - categories
  - tagged_words
  - readme

## Lab 2. Tokenize
1. Open lab2/simple.py file and complete ```line_tokenizer``` method
2. Open lab2/tweet.py file, write a tweet and tokenize it preserving hashtags and emoticons
2. Open lab2/math_tokenizer.py file, write an algebraic expression and separate into individual components
3. In each file play with some edge cases

## Lab 3. Removing stop words
1. Review the stop words list for English. Include ```from nltk.corpus import stopwords``` and ```stopwords.words('english')``` in a Python program and execute it.
2. Review the stop words list for Spanish language
3. Write a program from scratch that will remove the stop words from input.txt file in lab3 folder. Include in the stop words list the following punctuation symbols: [',','.',';',':']
4. Write the output of the program to an output.txt file located in the same directory
5. Modify the previous program to delete duplicated words as well.

## Lab 4. Stemming and lemmatizing
1. Run and see the output for English and Spanish files
2. Write a method to lemmatize english input. Use ```WordNetLemmatizer``` class from ```nltk.stem.wordnet``` module
3. Print only those words that were lemmatized. Compare the results with the stemming operation

## Lab 5. POS Tagging
1. Write a program which prints to standard output the count for each tag found in input.txt file.
  - You will have to tokenize the content from input.txt file
  - You will have to tag the words list. Use ```pos_tag``` method from ```nltk``` module
