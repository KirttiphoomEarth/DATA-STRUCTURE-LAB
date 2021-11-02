'''  POWER! '''
def factorial(n,m):
    if m == 0:
        return 1
    elif n == 0:
        return 0
    else:
        return factorial(n,m-1) * n

x,y = input("Enter Input a b : ").split()
print(factorial(int(x),int(y)))