class notebook:
    def __init__(self):
        self.CPU = ""
        self.GPU = ""
        self.RAM = ""
        self.DISPLAY = ""
        self.STORAGE = ""
        self.OS = ""

    def notebook_info(self):
        print(f'name:{self.CPU} GPU:{self.GPU} RAM:{self.RAM} DISPLAY:{self.DISPLAY} STORAGE:{self.STORAGE} OS:{self.OS}')

nd = []

n = int(input('How many notebook? : '))
for i in range (n):
    s =  notebook()
    print((f"Please, enter notebook info {i+1}:"))
    s.name = input("Enter CPU:")
    s.name = input("Enter GPU")
    s.name = input("Enter RAM")
    s.name = input("Enter DISPLAY")
    s.name = input("Enter STORAGE")
    s.name = input("Enter OS")
    nd.append(s)

# display all notebook in list
for i in nd:
    i.notebook_info()
