def remove_stopwords(tokens:list, stopwords:list):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    fresh_token = []
    for token in tokens:
      if token not in stopwords:
        fresh_token.append(token)
    return fresh_token  