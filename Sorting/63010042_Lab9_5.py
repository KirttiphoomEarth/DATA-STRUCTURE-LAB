from typing import List


def printRecur(num, left, res, x=0, list=[]):
    sum = 0
    patten = 0
    for i in list:
        sum += i
    if left == 0:
        if res == sum:
            print(list)
            return 1
        return 0
    elif x >= len(num):
        return 0
    else:
        patten += printRecur(num, left-1, res, x + 1, list + [num[x]])
        patten += printRecur(num, left, res, x + 1, list)
    return patten


inp = input('Enter Input : ').split("/")
res = int(inp[0])
num = [int(x) for x in inp[1].split()]
for i in range(len(num)):
    for j in range(len(num)-1-i):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]
patten = 0
for j in range(len(num)):
    patten += printRecur(num, j+1, res)
if patten == 0:
    print('No Subset')