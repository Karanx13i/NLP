from nltk.tokenize import sent_tokenize, word_tokenize

# Input text
input_sentence = """Chinky is very naughty in the class. She is known for troubling her teacher.
One fine day her teacher decided to give her a punishment, so she gave her set of paragraphs
and told her to count the number of sentences, words and number of paragraphs that are there in the given book."""

# Tokenize words and sentences
number_of_words = word_tokenize(input_sentence)
number_of_sentences = sent_tokenize(input_sentence)

# Count paragraphs (split by double newlines)
number_of_paragraphs = input_sentence.strip().count("\n\n") + 1

# Print results
print("Number of words:", len(number_of_words))
print("Number of sentences:", len(number_of_sentences))
print("Number of paragraphs:", number_of_paragraphs)
