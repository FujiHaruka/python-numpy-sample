import numpy as np
from sys import argv
from os import path

if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage:")
        print(
            f"  $ python {path.basename(__file__)} <input_file_name> <output_file_name>")
        exit()

    _, input_file, output_file = argv

    # numpy は csv ファイルから行列（ndarray）データを読み込み・書き込みできる
    # 参照 https://numpy.org/doc/stable/reference/routines.io.html#text-files
    matrix = np.genfromtxt(input_file, delimiter=",")

    # 逆行列を計算する
    # 行列固有の計算は linalg (Linear algebra) に関数がまとまっている
    # 参照 https://numpy.org/doc/stable/reference/routines.linalg.html
    inverse_matrix = np.linalg.inv(matrix)

    np.savetxt(output_file, inverse_matrix, delimiter=",")
