import numpy as np

地域数 = 47
部門数 = 77

def 行の和(行列, i):
    """
    行列のi行目の和
    """
    return 行列[i].sum()

def キャリブレート(元行列):
    行列 = 元行列.copy()
    行数, 列数 = 行列.shape
    for r in range(行数):
        print(f"キャリブレート中... 行: {r}")
        r行の和 = 行の和(行列, r)
        # r行目の要素のうち、値が非0の列のインデックスを取得
        非0の列, = 行列[r].nonzero()
        for c in 非0の列:
            # t^{hk}_i
            t = 行列[r, c]

            # t^{hk}_i を書き換える
            補正値 = t * (1 - r行の和) / r行の和
            行列[r, c] = t + 補正値

            # t^{hk}_i の下にある要素を書き換える
            for 下の行 in range(c + 1, 列数):
                # 0になっている箇所は無視
                if 行列[下の行, c] == 0:
                    continue

                行列[下の行, c] = 行列[下の行, c] - 補正値 / (行数 - 下の行)
    return 行列

if __name__ == "__main__":
    # csvファイルを numpy array として読み込む
    元行列 = np.genfromtxt("交易行列/列方向の比率行列.csv", delimiter=",", encoding='utf_8_sig', dtype=np.float32)

    キャリブレーション済み行列 = キャリブレート(元行列)

    # 結果をファイルに書き込む
    # 元行列データを上書きしたので元行列を別ファイルに書き込めばよい
    np.savetxt("交易行列.csv", 元行列, delimiter=",", fmt="%.10f")
