print(" *** Wind classification ***")
x = float(input("Enter wind speed (km/h) : "))
if x >= 209 :
    print("Wind classification is Super Typhoon.")
elif x >= 102.00:
    print("Wind classification is Typhoon.")
elif x >= 56.00:
    print("Wind classification is Tropical Storm.")
elif x >= 52.00:
    print("Wind classification is Depression.")
else:
    print("Wind classification is Breeze.")