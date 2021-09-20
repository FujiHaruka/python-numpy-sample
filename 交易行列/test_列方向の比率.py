import unittest
import numpy as np
from 列方向の比率 import 地域の小行列, 行の和, mの値, グラビティ比


class TestStringMethods(unittest.TestCase):
    def test_地域の小行列(self):
        地域数 = 2
        部門数 = 2
        行列 = np.array([
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 2, 2],
            [0, 0, 2, 2],
        ])

        小行列 = 地域の小行列(行列, 地域数, 部門数, 0)
        np.testing.assert_array_equal(小行列, np.array([
            [1, 1],
            [1, 1],
        ]))

        小行列 = 地域の小行列(行列, 地域数, 部門数, 1)
        np.testing.assert_array_equal(小行列, np.array([
            [2, 2],
            [2, 2],
        ]))

    def test_行の和(self):
        行列 = np.array([
            [1, 1, 1, 1],
            [2, 2, 2, 2],
        ])
        self.assertEqual(行の和(行列, 0), 4)
        self.assertEqual(行の和(行列, 1), 8)

    def test_mの値(self):
        Mベクトル = np.array([
            1,
            2,
            3,
            4,
            5,
            6,
        ])
        部門数 = 3
        self.assertEqual(mの値(Mベクトル, 部門数, h=0, d=0), 1)
        self.assertEqual(mの値(Mベクトル, 部門数, h=0, d=1), 2)
        self.assertEqual(mの値(Mベクトル, 部門数, h=1, d=0), 4)
        self.assertEqual(mの値(Mベクトル, 部門数, h=1, d=1), 5)

    def test_グラビティ比(self):
        # 元行列, G2乗行列, 地域数, 部門数, h1, h2, d
        地域数 = 3
        部門数 = 1
        元行列 = np.array([
            [1, 0, 0],
            [0, 2, 0],
            [0, 0, 3],
        ])
        G2乗行列 = np.array([
            [0, 2, 2],
            [2, 0, 2],
            [2, 2, 0],
        ])
        self.assertEqual(
            グラビティ比(元行列, G2乗行列, 地域数, 部門数, h1=0, h2=0, d=0),
            0,
        )
        self.assertEqual(
            グラビティ比(元行列, G2乗行列, 地域数, 部門数, h1=0, h2=1, d=0),
            0.5,
        )


if __name__ == '__main__':
    unittest.main()
