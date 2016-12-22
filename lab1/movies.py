from nltk.corpus import movie_reviews

#print("------ Printing Movies file ids -----\n")
#print(movie_reviews.fileids())
#print("\n")

file_id = "pos/cv999_13106.txt"
print("------ Printing sentiment category for %s file ------\n" % file_id)
print(movie_reviews.categories(file_id))
print("\n")
#
print("------ Printing content of %s file ------\n" % file_id)
print(movie_reviews.raw(file_id))
print("\n")
