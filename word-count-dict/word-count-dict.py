def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    global_dic = {}
    # Your code here
    for sentence in sentences:
      for w in sentence:
        if w in global_dic:
          global_dic[w] += 1
        else: 
          global_dic[w] = 1
    return global_dic