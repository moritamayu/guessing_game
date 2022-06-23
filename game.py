import random
import sys

def hitandblow(j, k):
    hit = 0
    blow = 0

    for n in range (3):
        if k[n] == j[n]:
            hit += 1
        else:
            if k[n] in j:
                blow += 1
    
    if hit == 3:
        print("正解です!")
        sys.exit()
    else:
        print("ヒット：%d, ブロー：%d" %(hit,blow))

def hint(i, j, k, m):
    if i==1:
        hint1(j, k)
    elif i==2:
        hint2(k)
    elif i==3:
        hint3(k)
    elif i==4:
        hint4(m)

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
    elif k%2==0:
        a = k / 2
        print("正解の数字は%dの倍数です" %a)
    else:
        print("正解の数字は素数です")

def hint4(m):
    sum = m[0] + m[1] + m[2]
    print("3つの数字の合計は%dです" %sum)

num = random.randint(100, 999)
num_list = [int(i) for i in str(num)]
num_list = [int(i) for i in num_list]
##print(num)
##print(num_list[0])
##print(num_list[1])
##print(num_list[2])

print("三桁の数字を入力すると，ヒット数字の数，ブローの数字の数，ヒントが表示されます．これらの情報から三桁の数字を推理しましょう．")
print("チャレンジできる回数は5回です")
print("ヒット：数字と桁位置の両方があっている")
print("ブロー：数字はあっているが桁位置が違う")

for i in range(1, 6):
    print("三桁の数字を入力してください")
    num_player = int (input())
    num_player_list = [int(i) for i in str(num_player)]
    num_player_list = [int(i) for i in num_player_list]

    hitandblow(num_player_list, num_list)

    if i==5:
        break

    print("ヒント%d : " %i, end="")
    hint(i, num_player, num, num_list)

print("正解は%dです" %num)