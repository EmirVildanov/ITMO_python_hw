import numpy as np


# For task 3_3.
class MatrixHash:
    def __hash__(self):
        """
        Matrix hash = sum of all of its values.
        """
        res = int(sum(sum(row) for row in self.matrix))
        return res


class Matrix(MatrixHash):
    # For task 3_3.
    # Map of { (hash(matrix_a, matrix_b)) -> multiplication_res }.
    cache = dict()

    def __init__(self, init_list):
        if not all(len(row) == len(init_list[0]) for row in init_list):
            raise ValueError("Matrix rows must be of the same length")
        self.matrix = init_list

    def compare_for_element_by_element_operation(self, other):
        if len(self.matrix) != len(other.matrix):
            raise ValueError("Matrices must contain the same number of rows")
        if len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Matrices must contain the same number of columns")

    def __add__(self, other):
        self.compare_for_element_by_element_operation(other)

        init_list = []
        for i in range(len(self.matrix)):
            init_list.append([self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))])
        return Matrix(init_list)

    def __mul__(self, other):
        self.compare_for_element_by_element_operation(other)
        init_list = []
        for i in range(len(self.matrix)):
            init_list.append([self.matrix[i][j] * other.matrix[i][j] for j in range(len(self.matrix[0]))])
        return Matrix(init_list)

    def __matmul__(self, other):
        # For task 3_3.
        pair_hash = hash((self, other))
        if pair_hash in self.cache:
            return self.cache[pair_hash]

        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("Columns number of the first matrix must be equal to the rows number of the second")

        init_list = []
        for i in range(len(self.matrix)):
            current_row = []
            for j in range(len(other.matrix[0])):
                current_row.append(sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0]))))
            init_list.append(current_row)

        # For task 3_3.
        res = Matrix(init_list)
        self.cache[pair_hash] = res

        return res


def compare_np_custom(np_matrix, custom_matrix, is_mixine=False):
    if not is_mixine:
        np.testing.assert_array_equal(np_matrix, custom_matrix.matrix)
    else:
        np.testing.assert_array_equal(np_matrix, custom_matrix)


def write_matrix(save_path, matrix: Matrix, is_mixine=False):
    if not is_mixine:
        with open(save_path, 'w') as f:
            for row in matrix.matrix:
                f.write(' '.join(map(str, row)) + '\n')
    else:
        matrix.save_to_file(save_path)


def do_matrix_work(first_init_list, second_init_list, first_matrix, second_matrix, save_path, is_mixine=False):
    """
    Logic common for tasks 3_1, 3_2:
    * Create matrices
    * Check operations are correct
    * Save results into files
    """
    add_res_expected = first_init_list + second_init_list
    add_res_actual = first_matrix + second_matrix
    compare_np_custom(add_res_expected, add_res_actual, is_mixine)

    mul_res_expected = first_init_list * second_init_list
    mul_res_actual = first_matrix * second_matrix
    compare_np_custom(mul_res_expected, mul_res_actual, is_mixine)

    matmul_res_expected = first_init_list @ second_init_list
    matmul_res_actual = first_matrix @ second_matrix
    compare_np_custom(matmul_res_expected, matmul_res_actual, is_mixine)

    write_matrix(f'{save_path}matrix+.txt', add_res_actual, is_mixine)
    write_matrix(f'{save_path}matrix*.txt', mul_res_actual, is_mixine)
    write_matrix(f'{save_path}matrix@.txt', matmul_res_actual, is_mixine)


if __name__ == "__main__":
    first_init_list = np.random.randint(0, 10, (10, 10))
    second_init_list = np.random.randint(0, 10, (10, 10))
    first_matrix = Matrix(first_init_list)
    second_matrix = Matrix(second_init_list)

    save_path = "artifacts/3_1/"
    do_matrix_work(first_init_list, second_init_list, first_matrix, second_matrix, save_path)
