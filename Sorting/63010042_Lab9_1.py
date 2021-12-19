def bubble_sort(l):
    if len(l) <= 1:
        return l
       
    if len(l) == 2:
        return l if l[0] < l[1] else [l[1], l[0]]
 
    a, b = l[0], l[1]
    bs = l[2:]
    res = []
     
    if a < b:
        res = [a] + bubble_sort([b] + bs)
    else:
        res = [b] + bubble_sort([a] + bs)
    return bubble_sort(res[:-1]) + res[-1:]
 

 
inp = [int(x) for x in input('Enter Input : ').split()]
res = bubble_sort(inp)
print(res)