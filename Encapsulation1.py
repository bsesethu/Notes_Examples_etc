class Person: # I dont understand it yet

    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    #@property # I've never seen @something before, I don't know what this is. Maybe its meant to be #. So Ive changed it from the original
    def Name(self):
        return self.__name
    
    #@Name.setter
    def Name(self, value):
        self.__name = value
        return self.__name

p1= Person('Mike', 30, 'm')
print(p1.Name('Mike')) # Since we have two methods of the same name being called, the second method will be the last implemented