import unittest
import numpy as np
from キャリブレーションv3 import 対角小行列の成分かどうかを調べる行列, 対角小行列を除外する, 移出ベクトルとの差を行方向に分配する, 移出ベクトルとの差が正になる行を抜き出す


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

    def test_対角小行列を除外する(self):
        元行列 = np.array([
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
        ], dtype=float)
        np.testing.assert_equal(
            対角小行列を除外する(元行列, 小行列サイズ=2),
            np.array([
                [0, 0, 1, 1, 1, 1],
                [0, 0, 1, 1, 1, 1],
                [1, 1, 0, 0, 1, 1],
                [1, 1, 0, 0, 1, 1],
                [1, 1, 1, 1, 0, 0],
                [1, 1, 1, 1, 0, 0],
            ], dtype=float)
        )

    def test_移出ベクトルとの差を行方向に分配する(self):
        元行列 = np.array([
            [0, 0, 1, 2, 1, 2],
            [0, 0, 3, 4, 3, 1],
            [1, 2, 0, 0, 1, 1],
            [4, 4, 0, 0, 3, 4],
            [1, 2, 5, 2, 0, 0],
            [3, 4, 2, 4, 0, 0],
        ], dtype=float)
        移出ベクトル = np.array([10, 10, 10, 10, 10, 10], dtype=float)
        行の和ベクトル = np.array([6, 11, 5, 15, 10, 13], dtype=float)
        移出ベクトルとの差 = 移出ベクトル - 行の和ベクトル
        行方向の補正量分配行列 = 移出ベクトルとの差を行方向に分配する(元行列, 移出ベクトルとの差, 行の和ベクトル, 小行列サイズ=2)
        np.testing.assert_almost_equal(
            行方向の補正量分配行列,
            np.array([
                [0, 0, 0.66666667, 1.33333333, 0.66666667, 1.33333333],
                [0, 0, 0, 0, 0, 0],
                [1, 2, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]
            ])
        )

    def test_移出ベクトルとの差が正になる行を抜き出す(self):
        元行列 = np.array([
            [0, 0, 1, 2, 1, 2],
            [0, 0, 3, 4, 3, 1],
            [1, 2, 0, 0, 1, 1],
            [4, 4, 0, 0, 3, 4],
            [1, 2, 5, 2, 0, 0],
            [3, 4, 2, 4, 0, 0],
        ])
        移出ベクトルとの差 = np.array([1, -1, 1, -1, -1, 1])
        np.testing.assert_equal(
            移出ベクトルとの差が正になる行を抜き出す(元行列, 移出ベクトルとの差),
            np.array([
                [0, 0, 1, 2, 1, 2],
                [0, 0, 0, 0, 0, 0],
                [1, 2, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [3, 4, 2, 4, 0, 0],
            ])
        )


if __name__ == '__main__':
    unittest.main()
