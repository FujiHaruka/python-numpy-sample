import unittest
import numpy as np
from キャリブレーション import キャリブレート

class TestStringMethods(unittest.TestCase):

    def test_キャリブレート(self):
        行列 = np.array([
            [0.1, 0.0, 0.2, 0.0],
            [0.0, 0.3, 0.0, 0.4],
            [0.9, 0.0, 0.8, 0.0],
            [0.0, 0.7, 0.0, 0.6],
        ])
        キャリブレーション結果 = キャリブレート(行列)

        # キャリブレーション結果を検証
        np.testing.assert_array_almost_equal(キャリブレーション結果, np.array([
            [0.333333, 0.0, 0.666667, 0.0],
            [0.0, 0.428571, 0.0, 0.571429],
            [0.639035, 0.0, 0.505263, 0.0],
            [0.0, 0.571429, 0.0, 0.512195],
        ]))

if __name__ == '__main__':
    unittest.main()
