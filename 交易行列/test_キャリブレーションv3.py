import unittest
import numpy as np
from キャリブレーションv3 import 対角小行列の成分かどうかを調べる行列, 元行列から対角小行列を除外する


class TestStringMethods(unittest.TestCase):

    def test_対角小行列の成分かどうかを調べる行列(self):
        np.testing.assert_equal(
            対角小行列の成分かどうかを調べる行列(元行列サイズ=6, 小行列サイズ=2),
            np.array([
                [True, True, False, False, False, False],
                [True, True, False, False, False, False],
                [False, False, True, True, False, False],
                [False, False, True, True, False, False],
                [False, False, False, False, True, True],
                [False, False, False, False, True, True],
            ])
        )

    def test_元行列から対角小行列を除外する(self):
        元行列 = np.array([
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
        ], dtype=float)
        対角小行列の成分か = 対角小行列の成分かどうかを調べる行列(元行列サイズ=6, 小行列サイズ=2)
        np.testing.assert_equal(
            元行列から対角小行列を除外する(元行列, 対角小行列の成分か),
            np.array([
                [0, 0, 1, 1, 1, 1],
                [0, 0, 1, 1, 1, 1],
                [1, 1, 0, 0, 1, 1],
                [1, 1, 0, 0, 1, 1],
                [1, 1, 1, 1, 0, 0],
                [1, 1, 1, 1, 0, 0],
            ], dtype=float)
        )


if __name__ == '__main__':
    unittest.main()
