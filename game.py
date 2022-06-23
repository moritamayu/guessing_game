import numpy as np
import sys

def judgment(j, k):
    if j==k:
        print("正解です！")
        sys.exit()
    else:
        print("不正解です．")

def hint(i, j, k):
    if i==1:
        hint1(j, k)
    elif i==2:
        hint2(k)

def hint1(j, k):
    if j>k:
        print("もっと小さい数字です．")
    else:
        print("もっと大きい数字です．")

def hint2(k):
    if k%2==0:
        print("正解の数字は偶数です．")
    else:
        print("正解の数字は奇数です．")

num = np.random.randint(100, 1000, (1, 1))
print(num)

for i in range(1, 3):
    print("三桁の数字を入力してください．")
    num_player = int (input())

    judgment(num_player, num)

    print("ヒント%d : " %i, end="")
    hint(i, num_player, num)