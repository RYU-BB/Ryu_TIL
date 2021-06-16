"""
문서의 TF표현은 소석 단어의 one-hot 표현을 합해 생성
TF표현의 각 원소는 해당 단어가 문장(말뭉치)에 등장하는 횟수다.
"""
from sklearn.feature_extraction.text import CountVectorizer
import seaborn as sns


corpus = ['Time flies like an arrow.',
          'Fruit flies like a banana.']

one_hot_vectorizer = CountVectorizer(binary=True)
one_hot = one_hot_vectorizer.fit_transform(corpus).toarray()
vocab = one_hot_vectorizer.get_feature_names()
sns.heatmap(one_hot, annot=True,
            cbar=False, xticklabels=vocab,
            yticklabels=['Sentence 1', 'Sentence 2'])
