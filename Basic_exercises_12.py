class Sesethu:
    def sese(tall):
        t = print('tall')
        return t
    
    def mthunzi(dark):
        return print('dark')
    
for name in Sesethu.__dict__:
    print(name)

mthu= Sesethu()
mthu.mthunzi()


# Question 4 from w3resource
import builtins

help(builtins.abs) # Dissplaying the documentation of the function
val = builtins.abs(-155)
print(val)

# Question 5
def student(name1, age, sex):
    return f'Student name: {name1} Student age: {age} Sexually active: {sex}'

print(student('Cal', 18, 'Active'))




        