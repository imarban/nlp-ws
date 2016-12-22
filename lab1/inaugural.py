from nltk.corpus import inaugural

print("------Printing latest 10 file ids-----\n")
file_ids = list(inaugural.fileids())
start = len(file_ids) - 10
end = len(file_ids)
for file_id in file_ids[start:end]:
    print(file_id)

print("\n")

print("------Printing Obama Inaugural Discourse-----\n")

obama_file_id = "2009-Obama.txt"
print(inaugural.raw(obama_file_id)[:1000])
print("\n")

print("------Statistics-----\n")
words_size = len(inaugural.words(obama_file_id))
print("Number of words: %s" % len(inaugural.words(obama_file_id)))
vocabulary_size = words_size - len(set(inaugural.words(obama_file_id)))
print("Number of vocabulary: %s" % vocabulary_size)
print("\n")
