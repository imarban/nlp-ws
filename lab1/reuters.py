from nltk.corpus import reuters

print("------ Printing Reuters categories -----\n")
print(reuters.categories())
print("\n")

file_id = "training/9864"
print("------ Printing categories for %s file ------\n" % file_id)
print(reuters.categories(file_id))
print("\n")

print("------ Printing content of %s file ------\n" % file_id)
print(reuters.raw(file_id))
print("\n")

print("------ Printing files with corn category ------\n")
print(reuters.fileids('corn'))
print("\n")
