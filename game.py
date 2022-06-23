import numpy as np
import sys

def judgment(j, k):
    if j==k:
        print("正解です！")
        sys.exit()
    else:
        print("不正解です")

def hint(i, j, k):
    if i==1:
        hint1(j, k)
    elif i==2:
        hint2(k)
    elif i==3:
        hint3(k)

def hint1(j, k):
    if j>k:
        print("もっと小さい数字です")
    else:
        print("もっと大きい数字です")

def hint2(k):
    if k%2==0:
        print("正解の数字は偶数です")
    else:
        print("正解の数字は奇数です")

def hint3(k):
    if k%3==0:
        print("正解の数字は3の倍数です")
    elif k%4==0:
        print("正解の数字は4の倍数です")
    elif k%5==0:
        print("正解の数字は5の倍数です")
    elif k%7==0:
        print("正解の数字は7の倍数です")
    elif k%11==0:
        print("正解の数字は11の倍数です")
    elif k%13==0:
        print("正解の数字は13の倍数です")
    elif k%17==0:
        print("正解の数字は17の倍数です")
    elif k%19==0:
        print("正解の数字は19の倍数です")
    elif k%23==0:
        print("正解の数字は23の倍数です")
    elif k%29==0:
        print("正解の数字は29の倍数です")
    elif k%31==0:
        print("正解の数字は31の倍数です")
    else:
        print("正解の数字は素数です")

num = np.random.randint(100, 1000, (1, 1))
print(num)

for i in range(1, 4):
    print("三桁の数字を入力してください．")
    num_player = int (input())

    judgment(num_player, num)

    print("ヒント%d : " %i, end="")
    hint(i, num_player, num)