# From Max Rohosky YouTube page. Intermediate Python programming... 2023
def proff(name, job_title):
    print(name +  ', '  + job_title)

# Keyword arguments
proff( job_title = 'Lawyer', name = 'Max') # It's all about keyword and positional arguments (line 9)

# Positional arguments
proff('Max', 'Lawyer')

# args --- Using/making sense of them
def addition_a(*args):
    sum1 = 0
    for i in args: # This is a new one for me
        sum1 += i # Interesting! i is each of the args respectfully
    print(sum1)

val_1 = addition_a(5, 8, 1, 7)

# kwargs --- allows us too pass keyword arguments, class being a dictionary
def kwargs_a(**kwargs):
    print(kwargs.items())

kwargs_a(keyword1 = 'sex', keysoo = 'dildo') # And you can add more 


# Map function
nums = (1, 2, 3, 4, 5, 6)
    # write a program that squares each of these literal values and store in a list
squares1 = []
for n in nums:
    sq = n * n
    squares1.append(sq)

print(squares1)

    # Now to do the same thing more efficiently using maps
def square(n):
    return n * n

num_squared = map(square, nums) # Executes the function, using the variable
print(list(num_squared)) # Must explicitly code in the return type
    # Beauty of map is that you can run many variables through the funtion 'square'


# map still, word example
words = ['How', 'are', 'you', 'doing', 'today']
word_len = list(map(len, words))
print(word_len) # Prints the number of charactors in each string literal
    # I love that I'm using the jargon


# Map with lambda function
result1 = map(lambda n: n * n, nums) # lambda has no formal definition
print(list(result1)) # Remember, must specify the type
                     # Also this is an even more simplified version of the above square 'method'


# Filter function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numm = []
for i in numbers:
    if i > 6:
        numm.append(i)
print('Num ', numm)
    # Now to do this same thing using the filter function 
def check_greater_6(number): # We waant to print numbers greater than 6
    if number > 6:
        return True
    else:
        False
print(list(filter(check_greater_6, numbers))) # Without 'list', it willl return a filter variable

    # We can do this using lambda also
print(list(filter(lambda x: x > 6, numbers)))

nums_list = [1, 2, 3, 4, 5, 6]
nums_tup = (1, 2, 3, 4, 5, 6)
nums_set = {1, 2, 3, 4, 5, 6}

def check_even(numss): # We want to filter out the even numbers
    if numss % 2 == 0: # Divides by 2 and checks if the remainder is equal to 2
        return True
    else:
        False
res_list = list(filter(check_even, nums_list))
res_tup = tuple(filter(check_even, nums_tup))
res_set = set(filter(check_even, nums_set))

print(res_list)
print(res_tup) 
print(res_set)
    # We can do this also just using the lambda and filter functions
print(list(filter(lambda y: y % 2 == 0, nums_list))) # Same with the other 2 prints

    # Using filter funtion with the parameter 'None'
a_list = [1, 'a', 0, False, True,  '0', 12, 'Hello']
result3 = filter(None, a_list) # Filters the Truthy literals/values 
print(list(result3))


# Reduce function
N__ = [1, 2, 3, 4, 5]
    # Find the sum of the values in the variable
tot = 0
for i in N__:
    tot += i
print(tot)
    # We can use 'reduce funtion
from functools import reduce

def sum(x, y):
    return x + y
print(reduce(sum, N__)) # for better understanding check @ 51 min
                        # Seems simpler and makes more sense to not use 'reduce'

