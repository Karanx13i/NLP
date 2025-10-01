import nltk
nltk.download('indian')
print(nltk.corpus.indian.words('hindi.pos'))
print("\n")
nltk.download('udhr')
from nltk.corpus import udhr
print(nltk.corpus.udhr.fileids())
languages = ['Chickasaw', 'English', 'German_Deutsch']
cfd = nltk.ConditionalFreqDist((lang, len(word)) for lang in languages for word in
udhr.words(lang + '-Latin1'))
cfd.plot(cumulative=True)
cfd.tabulate(conditions=['Chickasaw', 'English', 'German_Deutsch'], samples=range(10),
cumulative=True)
