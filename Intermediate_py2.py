# 'for else' loops__ check notes

# 'zip' and 'unzip'
    # 'zip' to combine lists
first_name = ['Albert', 'Boity', 'Cindy']
last_name = ['Am', 'Thulo', 'Mak']

first_and_last_name = list(zip(first_name, last_name))
print(first_and_last_name) # Returns a list with tuples

    # Unzip to split
full_name_list = [('Albert', 'Amt', 23),
                  ('Betty', 'bob', 54),
                  ('Cindy', 'Cam', 5) ]
f_name, l_name, age = list(zip(*full_name_list)) # To unzip: it's zip *
print(f'first name: {f_name} \n last name: {l_name} \n age: {age}')


# Python collections
set1 = {*()} # To create an empty set, remember sets aren't ordered, hence can't be indexed
    # Dictionaries
dict_1 = dict({1: 'apple', 2: 'cherry', 3: 'strawberry'})
print(dict_1[3]) # Access at key, with '3' being the key value not the index, returns the value corresponding to the key
print(dict_1.keys()) # keys
print(dict_1.values()) # values
print(dict_1.items()) # key value pairs
    # To add a value: in lists we 'append', in sets we 'add', in dicts we 'update'


# Lambda funtions
x = lambda a: a + 10

print(x(a = 5)) # keyword call
print(x(5)) # value call

y = lambda a, b: a + b
print(y(a = 5, b = 2))
print(y(5, 2))
    # We can even have 3 arguments

    # Lambda is frequently used with 'map', 'filter' and 'reduce'
    # lambda can be nested
nested_lambda = lambda i, j: i + j(i) # I'm not sure I understand this, but point is lambda can be nested
print(nested_lambda(10, lambda i: i*2)) 


# Objects and classes
class Student:
    pass

student_1 = Student()
student_1.first_name = 'Max'
student_1.last_name = 'Denoise'

print(student_1.first_name)
print(student_1.last_name)

    # Having the above as reference 
class Student1:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last 

student_1 = Student1('Ras', 'Thoyan')

print(student_1.first_name)
print(student_1.last_name)

    # We now add/change a major for students in the class
class Student1:
    def __init__(self, first, last, major):
        self.first_name = first
        self.last_name = last 
        self.major = major

    def change_major(self, new_major):
        self.major = new_major
        print(self.first_name, self.last_name, self.major)

student_1 = Student1('Ras', 'Thoyan', 'Computer Science')
student_1.change_major('Mechanocal Engineering')

student_2 = Student1('Da', 'Silver', 'Only Fans') # This is an add on, after student_1. Thereby showcasing the impotance
student_2.change_major('Stripper')                # of __init__ function and 'self'

print(student_1.first_name)
print(student_1.last_name)

print(student_2.first_name, student_2.last_name)

    
# Inheritances
class Student2:
    pass

class ExchangeStudent(Student2):
    pass

student_1 = Student()
print(student_1)
exchange_student_1 = ExchangeStudent()
print(exchange_student_1)       # Lines 92 - 102 is the staring point for these types of problems. We then
                                # add to them as neccessary, as illustrated below

class Student2:
    def __init__(self, first_name, surname, major):
        self.first_name = first_name
        self.surname = surname
        self.major = major

class ExchangeStudent(Student2): # Child class, it's called
    def __init__(self, first_name, surname, major, home_university):
        Student2.__init__(self, first_name, surname, major)
        self.home_university = home_university

student_1 = Student2('Ras', 'Thoyan', 'Chemistry')
print(student_1.first_name)
print(student_1.surname)
print(student_1.major)

exchange_student_1 = ExchangeStudent('Dan', 'Longe', 'Biology', 'Univ. of Pretoria')
print(exchange_student_1.first_name)
print(exchange_student_1.home_university) # We'll see it again when I need to do examples


# Decorators, doesn't seem important

