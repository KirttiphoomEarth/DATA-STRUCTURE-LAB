class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class Hash:
    def __init__(self, tb):
        self.table_size, self.max_colision = map(int, tb.split())
        self.table = [None] * self.table_size
    
    def hashing(self, data):
        data = data.split()
        asci = 0
        for alphabet in list(data[0]):
            asci += ord(alphabet)    
        asci %= self.table_size       
        count = 0                   
        while True:
            index = (asci + count ** 2) % self.table_size    
            if count == self.max_colision:                  
                print('Max of collisionChain')
                return False
            if self.table[index] is None:                       
                self.table[index] = Data(data[0], data[1])
                if None not in self.table:                  
                    return True
                return False
            count += 1
            print(f"collision number {count} at {index}")

    def print_table(self):
        for i, data in enumerate(self.table):
            print(f'#{i + 1}\t{data}')
        print('---------------------------')


print(" ***** Fun with hashing *****")
tb, data = input("Enter Input : ").split('/')
table = Hash(tb)
for d in data.split(','):
    check = table.hashing(d)
    table.print_table()
    if check:
        print('This table is full !!!!!!')
        quit()
        