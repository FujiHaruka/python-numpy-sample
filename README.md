# numpy のスニペット

前回 https://github.com/FujiHaruka/python-csv-convert-sample

## 環境

- Python v3 以上
- numpy 1.20.3

## 例

CSV ファイルで行列データを読み込んで何か行列計算をしてまた CSV ファイルとして出力する。

- [invert.py](./invert.py)

```bash
$ python invert.py input.csv output.csv
```

その他、numpy の行列計算の例。

- [snippets.py](./snippets.py)

```bash
$ python snippets.py
```

numpy がいかに高速か。 3000x3000の行列の逆行列を計算してみる。

```bash
$ python invert_large_matrix.py
It tooks 0.6150388717651367 seconds to calculate invert matrix of size 3000.
```
