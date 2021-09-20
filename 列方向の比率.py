import numpy as np

地域数 = 47
部門数 = 77

def 地域の小行列(元行列, h):
    """
    元の行列からh地域の小行列を取り出す
    """
    行開始 = 部門数 * h
    行終了 = 部門数 * (h + 1)
    # 列数は実際には 1 or 部門数
    行数, 列数 = 元行列.shape
    小行列の列数 = int(列数 / 地域数)
    列開始 = 小行列の列数 * h
    列終了 = 小行列の列数 * (h + 1)
    小行列 = 元行列[行開始:行終了, 列開始:列終了]
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

def グラビティ比(元行列, G2乗行列, h1, h2, d):
    if h1 == h2:
        # 0にしておくと都合が良い
        return 0
    h2地域 = 地域の小行列(元行列, h2)
    return 行の和(h2地域, d) / (G2乗行列[h1, h2] ** 2)

def 各地域のグラビティ比のリスト(元行列, G2乗行列, h, i):
    """
    地域数個のグラビティ比のリスト
    h - 自地域
    i - 部門
    """
    # pythonの内包表記でリストを定義
    # k番目の要素が、h地域とk地域のi部門におけるグラビティ比 G^{hk}_i を表す
    グラビティ比のリスト = [グラビティ比(元行列, G2乗行列, h, k, i) for k in range(地域数)]
    return グラビティ比のリスト

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

def 交易比率の3次元行列を作る(元行列, G2乗行列):
    """
    t^{hk}_i に 行列[h, k, i] でアクセスできるような行列を作る
    """
    # 空の行列を作ってから要素をセットする
    行列 = np.empty((地域数, 地域数, 部門数), dtype=np.float32)
    for h in range(地域数):
        for i in range(部門数):
            グラビティ比のリスト = 各地域のグラビティ比のリスト(元行列, G2乗行列, h, i)
            for k in range(地域数):
                行列[h, k, i] = h地域のi部門におけるk地域への交易比率(元行列, Mベクトル, グラビティ比のリスト, h, k, i)
    return 行列

def CSVファイルの冗長な0表記をなくす(ファイルパス):
    with open(ファイルパス, encoding="utf_8_sig") as ファイル:
        CSVテキスト = ファイル.read()
    # 文字列置換
    CSVテキスト = CSVテキスト.replace("0.000000000000000000e+00", "0")
    # 同じファイル名で保存
    with open(ファイルパス, mode="w", encoding="utf_8_sig") as ファイル:
        ファイル.write(CSVテキスト)

if __name__ == "__main__":
    # 入出力ファイル名
    # A用
    元行列ファイル = "交易行列/A_Determinant.csv"
    Mベクトルファイル = "交易行列/m4A.csv"
    G2乗行列ファイル = "交易行列/G^2.csv"
    出力ファイル = "交易行列/列方向の比率行列_A.csv"

    # # CG用
    # 元行列ファイル = "交易行列/CG.csv"
    # Mベクトルファイル = "交易行列/m4CG.csv"
    # G2乗行列ファイル = "交易行列/G^2.csv"
    # 出力ファイル = "交易行列/列方向の比率行列_CG.csv"

    # csvファイルを numpy array として読み込む
    元行列 = np.genfromtxt(元行列ファイル, delimiter=",", encoding='utf_8_sig', dtype=np.float32)
    Mベクトル = np.genfromtxt(Mベクトルファイル, encoding='utf_8_sig', dtype=np.float32)
    G2乗行列 = np.genfromtxt(G2乗行列ファイル, delimiter=",", encoding='utf_8_sig', dtype=np.float32)

    # 入力の行列サイズを検証
    if 元行列.shape != (地域数 * 部門数, 地域数 * 部門数) and 元行列.shape != (地域数 * 部門数, 地域数):
        raise Exception(f"入力ファイルの行列サイズが正しくありません。 {元行列ファイル}: {元行列.shape}")
    if Mベクトル.shape != (地域数 * 部門数,):
        raise Exception(f"入力ファイルの行列サイズが正しくありません。 {Mベクトルファイル}: {Mベクトル.shape}")
    if G2乗行列.shape != (地域数, 地域数):
        raise Exception(f"入力ファイルの行列サイズが正しくありません。 {G2乗行列ファイル}: {G2乗行列.shape}")

    # t^{hk}_i をまずは普通の行列として作る
    t = 交易比率の3次元行列を作る(元行列, G2乗行列)

    # tをもとに列方向の比率行列を計算する
    # ゼロ埋めした行列を作ってから値をセットする
    列方向の比率行列 = np.zeros((地域数 * 部門数, 地域数 * 部門数))
    for h in range(地域数):
        for i in range(部門数):
            for k in range(地域数):
                # t^{kh}_i を適切な位置に代入する
                列方向の比率行列[k * 部門数 + i, h * 部門数 + i] = t[h, k, i]

    # 各列の和が1であることを確認する
    for column in range(地域数 * 部門数):
        列の和 = 列方向の比率行列[:, column].sum()
        # 誤差込みで1に近いことを確認する
        if 列の和 < 0.9999 or 列の和 > 1.00001:
            # ただし0になるケースは除外
            if 列の和 == 0.0:
                continue
            print(f"[警告] 列方向の比率行列における列の和が1ではありません。 column={column} 列の和={列の和}")

    # 結果をファイルに書き込む
    np.savetxt(出力ファイル, 列方向の比率行列, delimiter=",", encoding="utf_8_sig")
    CSVファイルの冗長な0表記をなくす(出力ファイル)
    print(f"完了！ {出力ファイル} に書き込みました。")
