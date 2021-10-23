print(" *** String count ***")
x = input("Enter message : ")
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cL = int(0)
cU = int(0)
sU = []
sL = []
for i in range(len(x)):
    if x[i] in upper:
        if x[i] not in sU:
           sU.append(x[i])
        cU += 1
    elif x[i] in lower:
        if x[i] not in sL:
            sL.append(x[i])
        cL += 1
SU = '  '
SL = '  '
print("No. of Upper case characters :",cU)
print("Unique Upper case characters :",SU.join(sorted(sU)))
print("No. of Lower case Characters :",cL)
print("Unique Lower case characters :",SL.join(sorted(sL)))

