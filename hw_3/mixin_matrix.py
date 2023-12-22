import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin

from hw_3.matrix import do_matrix_work


class MixinMatrix(NDArrayOperatorsMixin, np.ndarray):
    def __new__(cls, init_list):
        if not all(len(row) == len(init_list[0]) for row in init_list):
            raise ValueError("Matrix rows must be of the same length")
        obj = np.asarray(init_list).view(cls)
        return obj

    @property
    def matrix(self):
        return self

    @matrix.setter
    def matrix(self, list_value):
        if not all(len(row) == len(list_value[0]) for row in list_value):
            raise ValueError("Matrix rows must be of the same length")
        self = np.array(list_value)

    def __str__(self):
        output = ""
        for row in self:
            output += (' '.join(map(str, row)) + '\n')
        return output

    def save_to_file(self, path):
        np.savetxt(path, self)


if __name__ == "__main__":
    first_init_list = np.random.randint(0, 10, (10, 10))
    second_init_list = np.random.randint(0, 10, (10, 10))
    first_matrix = MixinMatrix(first_init_list)
    second_matrix = MixinMatrix(second_init_list)

    save_path = "artifacts/3_2/"
    do_matrix_work(first_init_list, second_init_list, first_matrix, second_matrix, save_path, True)
