print("*** Rabbit & Turtle ***")
d, vr, vt, vf = input("Enter Input : ").split()
d, vr, vt, vf = [int(d), int(vr), int(vt), int(vf)]
x = "{:.2f}".format(d/(vt - vr) * vf)
print(x)