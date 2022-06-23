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

def hint2(i, j):
    if j%2==0:
        print("正解の数字は偶数です．")
    else:
        print("正解の数字は奇数です．")

num = np.random.randint(100, 1000, (1, 1))
print(num)

print("三桁の数字を入力してください．")
num_player = int (input())

judgment(num_player, num)

print("ヒント２：", end="")
hint2(num_player, num)