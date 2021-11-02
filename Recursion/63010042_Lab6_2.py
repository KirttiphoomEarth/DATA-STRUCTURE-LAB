'''  Reverse Sort List '''
list_int = []
def sort(i, j , n, ls):
    if ls[i] < ls[j]:
        x = ls[i]
        ls[i] = ls[j]
        ls[j] = x
    if j < n:
        sort(i,j+1,n,ls)
    else:
        if i < n-1:
            sort(i+1, i+2, n, ls)
        else:
            return print(ls)

def con_int(i,n,l):
    if i < n :
        list_int.append(int(l[i]))
        con_int(i+1,n,l)
    

x = input("Enter your List : ").split(',')
l = len(x)
print("List after Sorted : ",end='')
con_int(0,l,x)
sort(0, 1 , l-1, list_int)


