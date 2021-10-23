print(" *** Wind classification ***")
x = input("Enter wind speed (km/h) : ")
l = float(x)
if l >= 209:
    print("Wind classification is Super Typhoon.")
elif l >= 102:
    print("Wind classification is Typhoon.")
elif l >= 56:
    print("Wind classification is Tropical Storm.")
elif l >= 52:
    print("Wind classification is Depression.")
elif l >= 0:
    print("Wind classification is Breeze.")
else :
    print("!!!Wrong value can't classify.")
