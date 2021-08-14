from itertools import combinations, permutations
import math
# print("*** Fun with permute ***")
# newlist = [int(x) for x in input("input : ").split(',')]
# newlistLen = int(len(newlist))
# listpermut =[]
# permut = math.factorial(newlistLen)
# countn = int(0)

# print("Original Cofllection: ",end=' [')
# for i in newlist:
#     if i != len(newlist):
#      print(i,end=', ')
#     else:
#      print(i,end=']\n')

# #newlist.sort(reverse=True)
# #pre = permutations(newlist)
# #print(sum)
# # print("Collection of distinct numbers:",end='\n [')
# # for i in pre:
# #     countn += 1
# #     if countn < sum:
# #         print (list(i),end='')
# #         print(",",end=' ')
# #     else:
# #         print (list(i),end=']')
# print(permut)
# for i in range(permut):
o = []
def p(l):
    a = []
    c =  l.copy()
    o.append(c)
    t2 =  l.copy()
    for j in range(0,len(l)-1):
        b  = t2 [j]
        t2 [j] = t2 [j+1]
        t2 [j+1] = b
        c2 =  t2 .copy()
        o.append(c2)
def set(l):
    
    temp = l.copy()
    p(temp)
    for i in range(1,len(l)-1):
        for j in range(1,len(l)-1):
            b = temp[j]
            temp[j] = temp[j+1]
            temp[j+1] = b
            
            p(temp)
        b = temp[1]
        temp[1] = temp[len(l)-1]
        temp[len(l)-1] = b
        if i!=len(l)-2:
           
            p(temp)

print("*** Fun with permute ***")
x =[int(j) for j in input("input : ").split(",")]
print(f'Original Cofllection:  {x}')
xr = x[::-1]
set(xr)
print(f'Collection of distinct numbers:\n {o}')
    
    

 
 
