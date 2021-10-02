from numpy import ndarray

import numpy as np


def キャリブレートv2(元行列: ndarray, 移出ベクトル: ndarray, 小行列サイズ: int):
    # 引数のサイズ検証
    元行列の行数, 元行列の列数 = 元行列.shape
    移出ベクトルの行数, = 移出ベクトル.shape
    if 元行列の行数 != 移出ベクトルの行数:
        raise Exception("元行列の行数と移出ベクトルの行数が一致しません")
    if 元行列の行数 % 小行列サイズ != 0:
        raise Exception("元行列の行数が小行列サイズで割り切れません")

    # ステップ1 行の和を求め、移出ベクトルとの差をとる
    対角小行列を除外した元行列 = 対角小行列を除外する(元行列, 小行列サイズ)
    行の和ベクトル = 対角小行列を除外した元行列.sum(axis=1, dtype=float)
    移出ベクトルとの差 = 移出ベクトル - 行の和ベクトル

    # ステップ3
    # ある (行, 列) 成分が対角小行列の成分であるかどうかを確認するための行列を作る
    行方向の補正量分配行列 = 移出ベクトルとの差を行方向に分配する(
        対角小行列を除外した元行列, 移出ベクトル, 行の和ベクトル, 小行列サイズ)

    # ステップ3
    for 行 in range(元行列の行数):
        # 移出ベクトルとの差が負の行は「過多」、正の行は「過少」
        # 過多な行だけキャリブレーションの対象になるので過少な行は無視
        if 移出ベクトルとの差[行] >= 0:
            continue

        for 列 in range(元行列の列数):
            if 対角小行列の成分か[行, 列]:
                continue

            # 補正量 は (d - b) * a / b
            補正量 = 移出ベクトルとの差[行] * 元行列[行, 列] / Bベクトル[行]
            # 補正量は負の値だからここでは加算でいい
            # print(f"({行}, {列}) を補正量 {補正量} で補正する")
            元行列[行, 列] += 補正量

            # 下の列に対する調整
            # まずは下の列の和を計算する
            下の列ベクトル = np.where(
                # 移出ベクトルとの差が0以下または対角小行列の成分ならば0、そうでなければ元行列の値
                np.logical_or(
                    移出ベクトルとの差[行+1:] <= 0,
                    対角小行列の成分か[行+1:, 列]),
                0,
                元行列[行+1:, 列]
            )
            下の列の和 = 下の列ベクトル.sum()

            if 下の列の和 == 0:
                continue

            # 次に列方向の補正を行う
            下の行の補正ベクトル = np.where(
                np.logical_or(
                    移出ベクトルとの差[行+1:] <= 0,
                    対角小行列の成分か[行+1:, 列]),
                0,
                元行列[行+1:, 列] * 補正量 / 下の列の和
            )
            元行列[行+1:, 列] -= 下の行の補正ベクトル

    return 元行列


def 行の対角小行列成分の和(元行列, 小行列サイズ, 行):
    return 元行列[行, 小行列サイズ * (行 // 小行列サイズ):小行列サイズ * (行 // 小行列サイズ + 1)].sum()


def 対角小行列の成分かどうかを調べる行列(元行列サイズ: int, 小行列サイズ: int) -> ndarray:
    # 元行列と小行列が両方とも正方行列であると仮定している
    # こういうコードを書き始めるとすごく numpy っぽい
    列番号の行列 = np.tile(np.arange(元行列サイズ), 元行列サイズ).reshape((元行列サイズ, 元行列サイズ))
    行番号の行列 = 列番号の行列.T
    対角小行列の成分か = 行番号の行列 // 小行列サイズ == 列番号の行列 // 小行列サイズ
    return 対角小行列の成分か


def 対角小行列を除外する(元行列: ndarray, 小行列サイズ: int) -> ndarray:
    対角小行列の成分か = 対角小行列の成分かどうかを調べる行列(元行列.shape[0], 小行列サイズ)
    元行列から対角小行列を除外したもの = np.where(
        対角小行列の成分か,
        np.zeros(元行列.shape),
        元行列,
    )
    return 元行列から対角小行列を除外したもの


def 移出ベクトルとの差を行方向に分配する(元行列: ndarray, 移出ベクトル: ndarray, 行の和ベクトル: ndarray, 小行列サイズ: int) -> ndarray:
    移出ベクトル_縦ベクトル = 移出ベクトル.reshape((移出ベクトル.size, 1))
    行の和ベクトル_縦ベクトル = 行の和ベクトル.reshape((行の和ベクトル.size, 1))
    移出ベクトルとの差_縦ベクトル = 移出ベクトル_縦ベクトル - 行の和ベクトル_縦ベクトル
    対角小行列の成分か = 対角小行列の成分かどうかを調べる行列(元行列.shape[0], 小行列サイズ)
    行方向の補正量分配行列 = np.where(
        # 対角小行列の成分であるか、または移出ベクトルとの差が0以下（TODO: 要確認）だったら0にする
        np.logical_or(
            対角小行列の成分か,
            np.tile(移出ベクトルとの差_縦ベクトル <= 0, 移出ベクトル.size)
        ),
        np.zeros(元行列.shape),
        # 実は行列とベクトルとの四則演算が可能
        移出ベクトルとの差_縦ベクトル * 元行列 / 行の和ベクトル_縦ベクトル
    )
    return 行方向の補正量分配行列
