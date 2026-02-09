import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    assert len(y_pred) == len(y_true)
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)
    mse = 1/len(y_pred) * np.sum(np.power(y_pred - y_true,2))
    # print(f"{mse=}")
    return mse
