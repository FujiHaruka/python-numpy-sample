import numpy as np
from time import time

if __name__ == "__main__":
    """
    非常に大きな行列の逆行列を計算するのにかかる時間を計測する
    """

    size = 3000
    # size x size の正方行列を乱数で作成
    matrix = np.random.rand(size, size)

    start_at = time()
    np.linalg.inv(matrix)
    end_at = time()

    duration = end_at - start_at
    print(f"It tooks {duration} seconds to calculate invert matrix of size {size}.")
