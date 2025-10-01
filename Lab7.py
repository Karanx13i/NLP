
import nltk
nltk.download('brown')
print("\n")
from nltk.corpus import brown
print("All the genres are :", brown.categories())
print("\nEditorialgenere in Sorted order:")
editorial_genre_sort = sorted(set(brown.words(categories='editorial')))
print(editorial_genre_sort)
whwords = editorial_genre_sort[3493:3499]
print(whwords)
