import nltk
nltk.download('stopwords')
import nltk
nltk.download('averaged_perceptron_tagger')
import gensim
from gensim import corpora, models
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from nltk import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk # Import nltk here to ensure download works in this cell
nltk.download('punkt', quiet=True) # Download punkt here

doc_a = "Brocolli is good to eat. My brother likes to eat good brocolli, but not my mother."
doc_b = "My mother spends a lot of time driving my brother around to baseball practice."
doc_c = "Some health experts suggest that driving may cause increased tension and blood pressure."
doc_d = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
doc_e = "Health professionals say that brocolli is good for your health."
doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]
texts = []
for i in doc_set:
    raw = i.lower()
    tokens = word_tokenize(raw)
    stopped_tokens = [i for i in tokens if not i in stop_words]
    stemmed_tokens = [PorterStemmer().stem(i) for i in stopped_tokens]
    texts.append(stemmed_tokens)
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=3, id2word = dictionary, passes=3)
print(ldamodel)
