import numpy as np
import sys

def judgment(i, j):
    if i==j:
        print("正解です！")
        sys.exit()
    else:
        print("不正解です．")

def hint1(i, j):
    if i>j:
        print("もっと小さい数字です．")
    else:
        print("もっと大きい数字です．")

num = np.random.randint(100, 1000, (1, 1))
print(num)

print("三桁の数字を入力してください．")
num_player = int (input())

judgment(num_player, num)

print("ヒント１：", end="")
hint1(num_player, num)