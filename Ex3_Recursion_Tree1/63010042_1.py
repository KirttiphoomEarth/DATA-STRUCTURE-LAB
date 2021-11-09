'''จงเขียนโปรแกรมแบบ Recursive เพื่อรับค่าจำนวนเทอม ของ Harmonic แล้วหาค่าผลรวม 
โดยในโปรแกรมห้ามใช้คำสั่งการวนซ้ำ(while, for) และให้แสดงผลดังตัวอย่าง
Harmonic sum = 1 + 1/2 + 1/3 + 1/4 + ... 
สามารถพิมพ์เลขทศนิยมตามจำนวนจุดทศนิยมที่ต้องการได้จากคำสั่ง
print("%.5f" %(3.1428571428))'''

def harmonic_sum(n):
    if n == 1:
        print(n,end=' ')
        return 1
    s = harmonic_sum(n-1) + 1 / n
    print("+ 1/"+str(n),end=' ')
    return s
             
print(' *** Harmonic sum ***')
num = int(input("Enter number of terms : ")) 
print("= %.8f" %(harmonic_sum(num)))
