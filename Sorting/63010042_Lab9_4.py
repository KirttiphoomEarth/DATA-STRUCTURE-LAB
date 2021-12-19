inp = [e for e in input('Enter Input : ').split()]
def Median(data, x, t):
    c = False
    for i in range(len(data)):
        if data[i] > t:
            data.insert(i, t)
            c = True
            break
    if not c:
        data.insert(len(data), t)
    if len(data)%2 == 0 and len(data) > 0:
        a = (data[len(data)//2] + data[(len(data)//2)-1])/2
        print(f'list = {x} : median = {a:.1f}')
    elif len(data)%2 == 1:
        a = data[len(data)//2]
        print(f'list = {x} : median = {a:.1f}')

if inp[0] == 'EX':
    Ans = "minHeap and maxHeap"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    inp = list(map(int, inp))
    data = []
    x = []
    for i in range(len(inp)):
        temp = inp[i]
        x.append(inp[i])
        Median(data, x, temp)