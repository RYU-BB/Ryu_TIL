import numpy as np


def preprocess(text):
    """
    전처리 함수
    텍스트를 공백을 기준으로 id:word, word:id로 mapping
    :param text: input text
    :return: corpus : input text를 id 값으로 표현된 리스트
             word_to_id : input text를 word:id로 나타낸 dict
             id_to_word : input text를 id:word로 나타낸 dict
    """
    text = text.lower()
    text = text.replace('.', ' .')
    words = text.split(' ')

    word_to_id = {}
    id_to_word = {}

    for word in words:
        if word not in word_to_id:
            new_id = len(word_to_id)
            word_to_id[word] = new_id
            id_to_word[new_id] = word

    corpus = np.array([word_to_id[w] for w in words])

    return corpus, word_to_id, id_to_word


def create_co_matrix(corpus, vocab_size, window_size=1):
    """
    문장 속 단어를 벡터로 표현
    :param corpus: id로 표현된 문장
    :param vocab_size: 어휘 수
    :param window_size: 윈도우 크기
    :return: 각 단어를 벡터로 표현된 co-matrix
    """
    corpus_size = len(corpus)
    co_matrix = np.zeros((vocab_size, vocab_size), dtype=np.int32)

    for idx, word_id in enumerate(corpus):
        for i in range(1, window_size + 1):
            left_idx = idx - i
            right_idx = idx + i

            if left_idx >= 0:
                left_word_id = corpus[left_idx]
                co_matrix[word_id, left_word_id] += 1

            if right_idx < corpus_size:
                right_word_id = corpus[right_idx]
                co_matrix[word_id, right_word_id] += 1

    return co_matrix


def cos_similarity(x, y, eps=1e-8):
    """
    벡터간 유사도를 계산
    :param x: numpy array
    :param y: numpy array
    :return: cosine 유사도
    """
    nx = x / (np.sqrt(np.sum(x**2)) + eps)
    ny = y / (np.sqrt(np.sum(y**2)) + eps)
    return np.dot(nx, ny)

