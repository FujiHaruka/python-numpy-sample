import unittest
import numpy as np
from キャリブレーション import キャリブレート, 行の和


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
            [0.0, 0.42857143, 0.0, 0.57142857],
            [0.58024691, 0.0, 0.41975309, 0.0],
            [0.0, 0.57142857, 0.0, 0.42857143],
        ]))
        for 行 in range(4):
            self.assertAlmostEqual(行の和(キャリブレーション結果, 行), 1.0)


if __name__ == '__main__':
    unittest.main()
