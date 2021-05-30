import numpy as np

if __name__ == "__main__":
    print("# 行列の足し算は + を使う")
    m1 = np.array([[1.0, 2.0], [3.0, 4.0]])
    m2 = np.array([[5.0, 6.0], [7.0, 8.0]])
    m3 = m1 + m2
    print("")
    print(m3)
    print("")

    print("# 行列のかけ算は * を使う")
    m4 = m1 * m2
    print("")
    print(m4)
    print("")

    print("# 対角行列を生成")
    d1 = 1.5 * np.identity(3)
    print("")
    print(d1)
    print("")

    print("# 対角行列かどうかをチェックする")
    # Remove the diagonal and count the non zero elements
    is_d1_diagonal = np.count_nonzero(d1 - np.diag(np.diagonal(d1))) == 0
    is_m1_diagonal = np.count_nonzero(m1 - np.diag(np.diagonal(m1))) == 0
    print("")
    print(f"- d1 is diagonal?: {is_d1_diagonal}")
    print(f"- m1 is diagonal?: {is_m1_diagonal}")
    print("")

    print("# 複数の行列を結合")
    a1 = np.full([2, 2], 1.0)
    a2 = np.full([2, 2], 2.0)
    a3 = np.full([2, 2], 3.0)
    a4 = np.full([2, 2], 4.0)
    block = np.block([[a1, a2], [a3, a4]])
    print("")
    print(block)
    print("")

    print("# 行列の各行・列の和でベクトルを作る")
    print("")
    print("行の和")
    print(np.sum(m1, axis=1))
    print("")
    print("列の和")
    print(np.sum(m1, axis=0))
    print("")
