# IMPORTS #
import string

from lxml import etree
from nltk import pos_tag, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer


# FUNCTIONS #
def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)

    wnl = WordNetLemmatizer()
    tokens = [wnl.lemmatize(token) for token in tokens]
    tokens = [token for token in tokens if token not in stopwords.words('english')]
    tokens = [token for token in tokens if token not in string.punctuation]
    tokens = [token for token in tokens if pos_tag([token])[0][1] == 'NN']

    return tokens


def get_vectorizer_data(documents):
    for idx, document in enumerate(documents):
        tokens = preprocess(document)
        documents[idx] = ' '.join(tokens)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    vocab = vectorizer.get_feature_names_out()
    return tfidf_matrix, vocab


# MAIN #
tree = etree.parse('news.xml')
root = tree.getroot()
corpus = root[0]

articles = {news[0].text: news[1].text for news in corpus}
headers = list(articles.keys())

tfidf_matrix, vocab = get_vectorizer_data(list(articles.values()))

for doc_idx, tfidf_vector in enumerate(tfidf_matrix.toarray()):
    words_tfidf = zip(vocab, tfidf_vector)
    top_five_tokens = dict(sorted(words_tfidf, key=lambda x: (x[1], x[0]), reverse=True)[:5]).keys()

    header = headers[doc_idx]
    print(f'{header}:')
    print(*top_five_tokens)
    print()
