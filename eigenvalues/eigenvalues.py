import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    try:
        matrix = np.array(matrix)
        # make sure square matrix
        if np.shape(matrix)[0] == np.shape(matrix)[1]:
            # now the eigen value
            e_val ,e_vec =  np.linalg.eig(matrix)
            # print(f"{e_val=}" )
            return e_val
    except Exception as e:
        return None