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


def most_similar(query, word_to_id, id_to_word, word_matrix, top=5):
    """
    유사 단어의 랭킹 표시
    :param query: 검색어(단어)
    :param word_to_id: 단어에서 단어 ID로의 딕셔너리
    :param id_to_word: 단어 ID에서 단어로의 딕셔너리
    :param word_matrix: 단어 벡터들을 한데 모은 행렬. 각 행에는 대응하는 단어의 벡터가 저장되어있다고 가정
    :param top: 상위 몇 개까지 출력할지 설정
    :return: 유사도가 높은 순으로 출력
    """
    if query not in word_to_id:
        print('%s(을)를 찾을 수 없습니다.' % query)
        return
    
    print('\n[query] ' + query)
    query_id = word_to_id[query]
    query_vec = word_matrix[query_id]
    
    vocab_size = len(id_to_word)
    similarity = np.zeros(vocab_size)
    for i in range(vocab_size):
        similarity[i] = cos_similarity(word_matrix[i], query_vec)
        
    count = 0
    for i in (-1 * similarity).argsort():
        if id_to_word[i] == query:
            continue
        print(' %s: %s' % (id_to_word[i], similarity[i]))
        
        count += 1
        if count >= top:
            return


def ppmi(C, verbose=False, eps=1e-8):
    """
    PMI를 사용한 두 단어의 관련성
    :param C: 동시발생행렬
    :param verbose: 진행상황 출력 여부 flag
    :return: PPMI
    """
    M = np.zeros_like(C, dtype=np.float32)
    N = np.sum(C)
    S = np.sum(C, axis=0)
    total = C.shape[0] * C.shape[1]
    cnt = 0

    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
            pmi = np.log2(C[i, j] * N / (S[j]*S[i]) + eps)
            M[i, j] = max(0, pmi)

            if verbose:
                cnt += 1
                if cnt % (total//100) == 0:
                    print('%.1f%% 완료' % (100*cnt/total))

    return M
