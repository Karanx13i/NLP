from nltk import pos_tag
input_sentence = "Government of India is taking all necessary steps to ensure that we are prepared well to face the challenge and threat posed by the growing pandemic of COVID-19 the Corona Virus."
tokens = nltk.word_tokenize(input_sentence)
tag = nltk.pos_tag(tokens)
print(tag, "\n")
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp =nltk.RegexpParser(grammar)
result = cp.parse(tag)
