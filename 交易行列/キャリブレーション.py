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


def CSVファイルの冗長な0表記をなくす(ファイルパス):
    with open(ファイルパス, encoding="utf_8_sig") as ファイル:
        CSVテキスト = ファイル.read()
    # 文字列置換
    CSVテキスト = CSVテキスト.replace("0.000000000000000000e+00", "0")
    # 同じファイル名で保存
    with open(ファイルパス, mode="w", encoding="utf_8_sig") as ファイル:
        ファイル.write(CSVテキスト)


if __name__ == "__main__":
    # 入出力のファイル名。適宜書き換えてください
    元行列ファイル = "列方向の比率行列_A.csv"
    出力ファイル = "交易行列.csv"

    # csvファイルを numpy array として読み込む
    元行列 = np.genfromtxt(元行列ファイル, delimiter=",",
                        encoding='utf_8_sig', dtype=np.float32)

    キャリブレーション済み行列 = キャリブレート(元行列)

    # 結果をファイルに書き込む
    # 元行列データを上書きしたので元行列を別ファイルに書き込めばよい
    np.savetxt(出力ファイル, 元行列, delimiter=",", encoding="utf_8_sig")
    CSVファイルの冗長な0表記をなくす(出力ファイル)
    print(f"完了！ {出力ファイル} に書き込みました。")
