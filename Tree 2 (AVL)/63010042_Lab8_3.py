def fineN(n):
    if i[n] != -1:
        return i[n]
    
    fineN(2*n+1)
    fineN(2*n+2)
    i[n] = min(i[2*n+1], i[2*n+2])
    i[2*n+1] -= i[n]
    i[2*n+2] -= i[n]

a, b = input('Enter Input : ').split('/')
a, b = int(a), list(map(int, b.split()))
if len(b) == a//2+1:
    i = [-1] * a
    for x in range(len(b)):
        i[a//2+x] = b[x]
    fineN(0)
    print(sum(i))
else:
    print('Incorrect Input')


   