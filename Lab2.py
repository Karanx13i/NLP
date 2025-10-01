

from nltk.tokenize import word_tokenize
# Input sentence
sentence = "Chinnu is the one who protect lilly."
# Tokenize
tokens = word_tokenize(sentence)

# Remove punctuation and make lowercase
words = [word.lower() for word in tokens if word.isalpha()]
# Print results
print(words)
print("Count;", len(words))

# Post Lab

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
# Read sentence
sentence = "There is a change in a medium."
# Load stopwords (connectors + prepositions)
stop_words = set(stopwords.words('english'))
# Tokenize
tokens = word_tokenize(sentence)
# Remove stopwords but keep punctuation
filtered = [word.lower() for word in tokens if word.lower() not in stop_words or word in string.punctuation]
print("Before")
print(sentence)
print("After")
print(filtered)
