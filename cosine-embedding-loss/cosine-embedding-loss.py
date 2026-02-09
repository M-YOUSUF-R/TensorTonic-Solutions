import math
def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here
    return  (1-cos(x1,x2)) if label == 1 else max(0,cos(x1,x2) - margin)
def cos(x1,x2):
  nominator  = sum([a*b for a,b in zip(x1,x2)])
  denominator = math.sqrt(sum([a**2 for a in x1])) * math.sqrt(sum([a**2 for a in x2]))

  # print(f"{nominator/denominator=}")
  return nominator/denominator