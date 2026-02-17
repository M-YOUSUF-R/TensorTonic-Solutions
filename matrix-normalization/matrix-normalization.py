import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    try:
        matrix = np.array(matrix, dtype=float)

        if matrix.ndim > 2:
            return None
        elif norm_type.lower() == 'l2':
            divisor = np.linalg.norm(matrix, axis=axis, keepdims=True)
            print(f"{divisor=}")

        elif norm_type.lower() == 'l1':
            divisor = np.sum(np.abs(matrix), axis=axis, keepdims=True)
            print(f"{divisor=}")

        elif norm_type.lower() == 'max':
            divisor = np.max(np.abs(matrix), axis=axis, keepdims=True)
            print(f"{divisor=}")

        else:
            return None

        # avoid divide by zero
        divisor[divisor == 0] = 1

        return matrix / divisor

    except:
        return None
