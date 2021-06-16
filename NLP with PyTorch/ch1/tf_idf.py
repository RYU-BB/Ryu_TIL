"""
TF는 등장 횟수에 비례하여 단어에 가중치를 부여
IDF는 벡터 표현에서 흔한 토큰의 점수를 낮추고 드문 토큰의 점수를 높인다.

TF-IDF TF와 IDF를 곱한 값
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import seaborn as sns


corpus = ['Time flies like an arrow.',
          'Fruit flies like a banana.']

one_hot_vectorizer = CountVectorizer(binary=True)
one_hot = one_hot_vectorizer.fit_transform(corpus).toarray()
vocab = one_hot_vectorizer.get_feature_names()
tfidf_vectorizer = TfidfVectorizer()
tfidf = tfidf_vectorizer.fit_transform(corpus).toarray()

sns.heatmap(tfidf, annot=True, cbar=False, xticklabels=vocab,
            yticklabels=['Sentence 1', 'Sentence 2'])