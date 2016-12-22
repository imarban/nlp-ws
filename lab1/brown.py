from nltk.corpus import brown
import nltk

hobbies_category = "hobbies"
print("------ Printing some of the existent words in hobbies category ----- ")
print(brown.words(categories = hobbies_category))
print("\n")


print("------ Printing some of the existent words with POS tag -----")
print(brown.tagged_words(categories = hobbies_category))
print("\n")

print("------ Printing description for specific POS tag -----")
print(nltk.help.brown_tagset("RB"))

#print(brown.readme())
