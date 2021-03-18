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

    :param corpus:
    :param vocab_size:
    :param window_size:
    :return:
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


def