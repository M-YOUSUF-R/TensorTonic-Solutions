import numpy as np

def hinge_loss(y_true, y_score, margin=1.0, reduction="mean") -> float:
    """
    y_true: 1D array of {-1,+1}
    y_score: 1D array of real scores, same shape as y_true
    reduction: "mean" or "sum"
    Return: float
    """
    # Write code here
    y_true = np.array(y_true)
    y_score = np.array(y_score)
    total_loss = np.sum(np.maximum(margin - y_true*y_score,0))
    # print(f"{total_loss=}")
    if reduction.lower() == "mean":
      # print(f"mean: {float(total_loss / len(y_true))}")
      return float(total_loss / len(y_true))
    # print(f"sum: {total_loss}")
    return total_loss