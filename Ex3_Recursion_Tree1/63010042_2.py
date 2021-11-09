'''จงเขียนโปรแกรมแบบ Recursive เพื่อหาค่า Max ของข้อมูลที่ป้อนเข้ามา แล้วแสดงผลดังตัวอย่าง'''
def max(n):
    if len(n) == 1:
        return n[0]
    else:
        m = max(n[1:])
        return m if m > n[0] else n[0]
    
        
num = [int(i) for i in input("Enter Input : ").split()]
print("Max : {0}".format(max(num)))

