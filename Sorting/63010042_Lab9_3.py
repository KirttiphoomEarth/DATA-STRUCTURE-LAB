def sele(data):
    for last in range(len(data) - 1, -1, -1):
        big = data[0]
        big_index = 0
        for i in range(1, last +1 ):
            if data[i] > big:
                big = data[i]
                big_index = i
        data[last], data[big_index] = data[big_index], data[last]
    return data

inp = [int(a) for a in list(input('Enter Input : '))]
tmp = sele(inp.copy())
drom = ''
if inp[0] == inp[-1]:
    drom = 'Repdrome'
elif inp == tmp:
    drom = 'Metadrome'
    for i in range(len(inp) - 1):
        if inp[i] == inp[i + 1]:
            drom = 'Plaindrome'
            break
elif inp[0:] == tmp[len(tmp) -1:0:-1] + tmp[:1]:
    drom = 'Katadrome'
    for i in range(len(inp) - 1):
        if inp[i] == inp[i + 1]:
            drom = 'Nialpdrome'
            break
else:
        drom = 'Nondrome'

print(drom)