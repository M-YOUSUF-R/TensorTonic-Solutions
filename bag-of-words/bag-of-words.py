import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    # vocab_dict = {v:i for i,v in enumerate(vocab)}
    token_count = np.zeros(shape=len(vocab),dtype=int)
    for w in tokens:
      if w in vocab:
        token_count[vocab.index(w)] += 1
    return token_count