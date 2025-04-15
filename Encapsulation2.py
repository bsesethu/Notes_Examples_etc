class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print('Selling Price:  {}'.format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

comp1 = Computer()
comp1.sell()
comp1.setMaxPrice(1000) # We are now changing the max price
comp1.sell()

a = ['app', 'ban']
b = a.append('org') # For some reason it doesnt want to be named something else
print(a)
print(a)
print(b) # Returns None!

c = []
c.append(1)
print(c)