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

genres = ['fiction', 'lore', 'belles_lettres', 'government', 'learned']
for i in range(0,len(genres)):
    genre = genres[i]
    print()
    print("Analysing '"+ genre + "' wh words")
    genre_text = brown.words(categories = genre)
    fdist = nltk.FreqDist(genre_text)
    for wh in whwords:
        print(wh + ':', fdist[wh], end=' ')
