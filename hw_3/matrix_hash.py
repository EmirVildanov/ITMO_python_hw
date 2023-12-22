from hw_3.matrix import Matrix, write_matrix
import numpy as np

if __name__ == "__main__":
    save_path = "artifacts/3_3/"
    A_input_list = np.array([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ])
    A = Matrix(A_input_list)
    write_matrix(f'{save_path}A.txt', A)

    # Collision by definition of hash function.
    C_input_list = np.array([
        [9, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ])
    C = Matrix(C_input_list)
    write_matrix(f'{save_path}C.txt', C)

    BD_input_list = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])
    B = Matrix(BD_input_list)
    D = Matrix(BD_input_list)
    write_matrix(f'{save_path}B.txt', B)
    write_matrix(f'{save_path}D.txt', D)

    AB = A @ B
    CD = C @ D
    write_matrix(f'{save_path}AB.txt', AB)
    write_matrix(f'{save_path}CD.txt', CD)

    with open(f'{save_path}hash.txt', 'w') as f:
        f.write("AB hash: " + str(hash(AB)) + '\n')
        f.write("CD hash: " + str(hash(CD)))