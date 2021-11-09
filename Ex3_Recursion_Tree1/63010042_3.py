'''จงเขียนโปรแกรมแบบ Recursive สำหรับหา หรม. ของเลข 2 ตัว แล้วให้แสดงผลดังตัวอย่าง
หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 2 ตัว'''

def gcd(n1, n2):
    if n2 == 0:
        return n1
    else:
        return gcd(n2,n1%n2)
        
num = [int(i) for i in input("Enter Input : ").split()]
x = abs(num[0])
y = abs(num[1])
ans = gcd(x, y)
if x == 0 and y == 0:
    print('Error! must be not all zero.')
elif x == 0 and y != 0:
    print("The gcd of {0} and {1} is : {2}".format(num[0], num[1], ans))
elif x > y:
    print("The gcd of {0} and {1} is : {2}".format(num[0], num[1], ans))
else:
    print("The gcd of {0} and {1} is : {2}".format(num[1], num[0], ans))