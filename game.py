import numpy as np

num = np.random.randint(100, 1000, (1, 1))
##print(num)

print("Please input three place numbers.")
num_player = int (input())

if num_player==num:
    print("Your answer is correct. Congratulation!")

else:
    print("Your answer is incorret.")