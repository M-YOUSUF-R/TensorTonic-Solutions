def text_chunking(tokens, chunk_size, overlap):
  """
  Split tokens into fixed-size chunks with optional overlap.
  """
  token_chunks = []
  first = 0
  last = chunk_size
  # Write code here
  if len(tokens) == 0:
    return []
  if len(tokens) <= chunk_size:
    token_chunks.append(tokens)
    return token_chunks
    
  while last <= len(tokens):
    token_chunks.append(tokens[first:last])
    first = last - overlap
    last = first + chunk_size
  return token_chunks