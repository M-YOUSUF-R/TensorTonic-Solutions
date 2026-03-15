import math
def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here
    sum_p = 0
    for i in range(len(prob_distributions)):
      p = prob_distributions[i][actual_tokens[i]]
      log_p = math.log(p)
      sum_p += log_p
    return math.exp((-1/len(prob_distributions))*sum_p)