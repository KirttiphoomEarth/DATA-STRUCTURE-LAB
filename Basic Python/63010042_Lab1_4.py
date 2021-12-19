print('*** Fun with Drawing ***')
print('Enter input : ',end='')
rows = int(input())
downrows = 2 * rows - 2
downc = (downrows*2) - 1 
mid = downrows*2 + 1
donf = 1
donb = 1
tryag1 = 1
tryag2 = 1
topfronDon = topmidDon = topbackDon = rows - 1

for i in range(rows-1, 0, -1):
    for j in range(0, topfronDon):
        print(end=".")
    topfronDon -= 1

    for j in range(0, tryag1):
        if j == 0 or j == tryag1-1:
          print("*",end="")
        else:
          print("+",end="")
    tryag1 += 2

    for j in range(0, topmidDon*2-1):
        print(end=".")
    topmidDon -= 1

    for j in range(0, tryag2):
        if j == 0 or j == tryag2-1:
          print("*",end="")
        else:
          print("+",end="")
    tryag2 += 2

    for j in range(0, topbackDon):
        print(end=".")
    topbackDon -= 1

    print("")
   
for i in range(0, mid):
    if i == 0 or i == mid-1 or i == mid//2:
     print("*", end='')
    else:
     print("+", end='')

print("")

for i in range(downrows, 0, -1):
    for j in range(0, donf):
        print(end=".")
    donf += 1

    for j in range(0, downc):
        if j == 0 or j == downc-1:
         print("*",end="")
        else:
         print("+",end="")
    downc-=2

    for j in range(0, donb):
        print(".",end="")
    donb += 1

    print("")
