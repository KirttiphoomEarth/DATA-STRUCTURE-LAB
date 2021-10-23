class Mylnt:
    def __init__(self,s):
        self.s = s

    def toRoman(self):
        
        romen = ['1000','900','500','400','100','90','50','40','10','9','5',4,'1']
        def re(sr):
            if sr == '1000':
                return 'M'
            elif sr == '900':
                return 'CM'
            elif sr == '500':
                return 'D'
            elif sr == '400':
                return 'CD'
            elif sr == '100':
                return 'C'
            elif sr == '90':
                return 'XC'
            elif sr == '50':
                return 'L'
            elif sr == '40':
                return 'XL'
            elif sr == '10':
                return 'X'
            elif sr == '9':
                return 'IX'
            elif sr == '5':
                return 'V'
            elif sr == '4':
                return 'IV'
            elif sr == '1':
                return 'I'
            elif sr == '2000': return 'MM'
            elif sr == '3000': return 'MMM'
            elif sr == '4000': return 'MMMM'
            elif sr == '5000': return 'MMMMM'
            elif sr == '6000': return 'MMMMMM'
            elif sr == '7000': return 'MMMMMMM'
            elif sr == '8000': return 'MMMMMMMM'
            elif sr == '9000': return 'MMMMMMMMM'
            elif sr == '800': return 'DCCC'
            elif sr == '700': return 'DCC'
            elif sr == '600': return 'DC'
            elif sr == '300': return 'CCC'
            elif sr == '200': return 'CC'
            elif sr == '2': return 'II'
            elif sr == '3': return 'III'
            elif sr == '6': return 'IVII'
            elif sr == '7': return 'VII'
            elif sr == '8': return 'VIII'
        if self.s in romen:
            return re(self.s)
        else:
            str_1 = []
            n = int(self.s)
            cout = int(1)
            while n != 0:
                tmep = n % 10
                if cout == 1:
                    temp = tmep * 1
                    cout += 1
                elif cout == 2:
                    temp = tmep * 10
                    cout += 1
                elif cout == 3:
                    temp = tmep * 100
                    cout += 1
                elif cout == 4:
                    temp = tmep * 1000
                    cout += 1
                str_1.append(re(str(tmep)))
                n = int(n/10)
                
            return str_1
        
            
    def __add__(self,a,b):
        sum = a + b
        return int(sum + (sum/2))
x,y = input("Enter 2 number : ").split()
a = Mylnt(x)
b = Mylnt(y)
# print("{0} convert to Roman : {1}".format(x,a.toRoman()))
# print("{0} convert to Roman : {1}".format(x,b.toRoman()))
# print("{0} + {1} = {2} ".format(x,y,a.__add__(int(x),int(y))))
print(a.toRoman())