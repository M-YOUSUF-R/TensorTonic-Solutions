import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # seqs = np.array(seqs)
    
    # Your code here
    if len(seqs) == 0:
      return np.empty((0,0))

    if  max_len is None:
      max_len = max(len(seq) for seq in seqs )
    res = []
    for seq in seqs:
      if len(seq) < max_len:
        seq = seq + [pad_value] * (max_len - len(seq))
      res.append(seq[:max_len])
    res = np.array(res)
    return res