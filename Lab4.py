from nltk import pos_tag
input_sentence  = "The little mouse ate the fresh cheeze"
tokens = nltk.word_tokenize(input_sentence)
tag = nltk.pos_tag(tokens)
#print(tag, "\n")
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp =nltk.RegexpParser(grammar)
result = cp.parse(tag)
print("Parse tree for 'The little mouse ate the fresh cheeze' with grammar NP: {<DT>?<JJ>*<NN>}:\n", result, "\n")


import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag, word_tokenize, RegexpParser
# Example text
sample_text = "The quick brown fox jumps over the lazy dog"
# Find all parts of speech in above sentence
tagged = pos_tag(word_tokenize(sample_text))
#Extract all parts of speech from any text
chunker = RegexpParser("""
NP: {<DT>?<JJ>*<NN>} # To extract Noun Phrases
P: {<IN>} # To extract Prepositions
V: {<V.*>} # To extract Verbs
PP: {<P> <NP>} # To extract Prepositional Phrases
VP: {<V> <NP|PP>*} # To extract Verb Phrases
""")
# Parse the tagged sentence
output = chunker.parse(tagged)
# Print all parts of speech in above sentence
print("Parse tree for 'The quick brown fox jumps over the lazy dog' with more detailed grammar:\n", output)
#To draw the synt
