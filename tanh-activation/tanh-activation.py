import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.array(x)
    ex = np.power(np.e,x)
    eix = np.power(np.e,-x)
    r = np.divide(np.subtract(ex,eix),np.add(ex,eix))
    return r