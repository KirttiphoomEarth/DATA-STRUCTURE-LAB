class Rehash:

    def __init__(self, data):
        self.table_size     = int(data.split()[0])
        self.max_colision   = int(data.split()[1])
        self.trashold       = int(data.split()[2])
        self.table = [None] * self.table_size
        self.data = []

        print('Initial Table :') 
        self.print_table()

    def hashing(self, data):
        if data not in self.data: 
            print(f'Add : {data}')
            self.data += [data]
        count = 0 
        while count <= self.max_colision:                       
            index = (data + (count ** 2)) % self.table_size     
            if self.table[index] is None:                       
                self.table[index] = data                        
                if ((self.table_size - self.table.count(None)) / self.table_size * 100 > self.trashold): 
                    print('****** Data over threshold - Rehash !!! ******')
                    self.rehashing()
                return
            count += 1
            print(f"collision number {count} at {index}") 
            if count == self.max_colision: 
                print('****** Max collision - Rehash !!! ******')
                self.rehashing()
                return

    def rehashing(self):
        tmp = self.table_size * 2 
        while True:
            divide = 2
            check = False 
            while  divide < tmp ** 0.5: 
                if tmp % divide == 0: 
                    check = True
                    break
                divide += 1
            if not check:
                break
            tmp += 1 

        self.table = [None] * tmp 
        self.table_size = tmp 

        for data in self.data: 
            self.hashing(data) 

    def print_table(self):
        for i, data in enumerate(self.table):
            print(f'#{i + 1}\t{data}')
        print('----------------------------------------')


print(' ***** Rehashing *****')
tb, data = input('Enter Input : ').split('/')
table = Rehash(tb)
for d in data.split():
    table.hashing(int(d))
    table.print_table()