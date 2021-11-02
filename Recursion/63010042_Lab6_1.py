'''  Factorial '''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return factorial(n-1) * n

x = input("Enter Number : ")
print(x + "! = ",end='')
print(factorial(int(x)))
