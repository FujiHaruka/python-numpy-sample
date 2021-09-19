import numpy as np

地域数 = 47
部門数 = 77

def 地域の小行列(元行列, h):
    """
    元の行列から地域の小行列を取り出す
    """
    開始 = 部門数 * h
    終了 = 開始 + 部門数
    小行列 = 元行列[開始:終了, 開始:終了]
    return 小行列

def 行の和(行列, i):
    """
    行列のi行目の和
    """
    return 行列[i].sum()

def mの値(Mベクトル, h, d):
    """
    h地域d部門の値m
    """
    return Mベクトル[h * 部門数 + d]

def グラビティ比(元行列, G2乗ベクトル, h1, h2, d):
    if h1 == h2:
        # 0にしておくと都合が良い
        return 0
    h2地域 = 地域の小行列(元行列, h2)
    return 行の和(h2地域, d) / (G2乗ベクトル[h1, h2] ** 2)

def h地域のi部門におけるk地域への交易比率(元行列, Mベクトル, グラビティ比のリスト, h, k, i):
    h地域 = 地域の小行列(元行列, h)
    h地域i行の和 = 行の和(h地域, i)
    if h地域i行の和 == 0:
        # 意味のある値を出せないので0を返す
        return 0

    mの比 = mの値(Mベクトル, h, i) / h地域i行の和
    if h == k:
        return 1 - mの比
    else:
        グラビティ比の総和 = sum(グラビティ比のリスト)
        return mの比 * グラビティ比のリスト[k] / グラビティ比の総和

if __name__ == "__main__":
    # csvファイルを numpy array として読み込む
    元行列 = np.genfromtxt("交易行列/A_Determinant.csv", delimiter=",", encoding='utf_8_sig')
    G2乗ベクトル = np.genfromtxt("交易行列/G^2.csv", delimiter=",", encoding='utf_8_sig')
    Mベクトル = np.genfromtxt("交易行列/m4A.csv", encoding='utf_8_sig')

    # t^{kh}_i をまずは普通の行列として作る
    # 空の行列を作る
    t = np.empty((地域数, 地域数, 部門数))
    for h in range(地域数):
        for i in range(部門数):
            # こういうリストの書き方を python では「内包表記」という
            グラビティ比のリスト = [グラビティ比(元行列, G2乗ベクトル, h, k, i) for k in range(地域数)]
            for k in range(地域数):
                k地域 = 地域の小行列(元行列, k)
                t[h, k, i] = h地域のi部門におけるk地域への交易比率(元行列, Mベクトル, グラビティ比のリスト, h, k, i)

    # tから列方向の比率行列を計算する
    列方向の比率行列 = np.zeros((地域数 * 部門数, 地域数 * 部門数))
    for h in range(地域数):
        for i in range(部門数):
            for k in range(地域数):
                列方向の比率行列[k * 部門数 + i, h * 部門数 + i] = t[h, k, i]

    # 各列の和が1であることを確認
    for column in range(地域数 * 部門数):
        列の和 = 列方向の比率行列[:, column].sum()
        # 誤差込みで1に近いことを確認する
        if 列の和 < 0.9999 or 列の和 > 1.00001:
            print(f"[警告] 列方向の比率行列における列の和が1ではありません。 column={column} 列の和={列の和}")
