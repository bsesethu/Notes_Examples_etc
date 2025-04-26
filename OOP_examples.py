# From webpage https://www.w3resource.com/python-exercises/oop/index.php#google_vignette
# Question 2
class Person:
    def determine_age(d_o_b, current_year):
        current_age = current_year - d_o_b
        return current_age

name = 'Sesethu'
country = 'South Africa'

curr_age = Person.determine_age(1994, 2025)
print(name, 'from ', country, ' is', curr_age, ' years old in the current year')

# Question 2 another approach
    # This approach is much better as we can add and remove data points in the init method, makes things easier in the long run
from datetime import date

class Person1:
    # Initialize the Person object with a name, country, d.o.b
    def __init__(self, name1, country1, d_o_b1):
        self.name1 = name1    # So 'self' is essentially 'Person1'
        self.country1 = country1
        self.d_o_b1 = d_o_b1 # I think this is encapsulation, this method
        
    def calculate_age(self):
        today = date.today()
        age1 = today.year - self.d_o_b1.year
        # To test if the birthday has already passed
        if today < date(today.year, self.d_o_b1.month, self.d_o_b1.day):
            age1 -= 1
        return age1
    
    # Example usage
personA = Person1('Sesethu Bango', 'South Africa', date(1994, 3, 1))
personB = Person1('Culolakhe Bango', 'South Africa', date(2023, 6, 22))

print(personA.country1, personA.calculate_age())
print(personB.name1)
print(personB.name1, 'was born on ', personB.d_o_b1, ' in ', personB.country1)
    # Can do much more

# Question 4
import math

class Shape:
    def __init__(self, length, breadth, side):
        self.length = length
        self.breadth = breadth
        self.side = side
        
    def circle_area(self):
        area = math.pi*(self.length/2)**2 # length being the diameter
        return area
    
    def circle_parameter(self):
        perameter = math.pi*self.length
        return perameter
    
    def triangle_area(self):
        area = 1/2*(self.length * self.breadth)
        return area
    
    def triangle_parameter(self):
        parameter = self.length + self.breadth + self.side
        return parameter
    
    def square_area(self):
        area = self.length * self.breadth
        return area
    
    def square_parameter(self):
        parameter = 2 * (self.length + self.breadth)
        return parameter
        
circle = Shape(5, 0, 0) # 0 beecause they're not relevant to the circle
triangle = Shape(5, 5, 5)
square = Shape(5, 5, 0)

print('Area of circle is ', circle.circle_area())
print('Parameter of the circle is ', circle.circle_parameter())
print('--------------------------------------------------------------')
print('Area of the triangle is ', triangle.triangle_area())
print('Parameter of the triangle is ', triangle.triangle_parameter())
print('---------------------------------------------------------------------')
print('Area of the square is ', square.square_area())
print('Parameter of the square is ', square.square_parameter())
    # This makes all the sense in the world to me, hence more understanding of encapsulation
    # My approaches seems more efficient than that of w3resource
    

# Question 8
class Shopping_cart:
    def __init__(self, shopping_list):
        self.shopping_list = shopping_list 
    
    def add_item(self): # Wow this 'self' thing is really important, it was giving errors without it
        self.shopping_list = []
        in_put = input('Input item name, press 0 if no item input: ')
        while in_put != '0': # It has to be a string 0, not an integer!!
            self.shopping_list.append(in_put)
            print('Current list: ', self.shopping_list)
            in_put = input('Input item name, press 0 if no item input: ')
            if in_put == '0':         
                print('No more items to input')
        print(self.shopping_list)
        
    def remove_item(self, shopping_list):
        susa = input('name of item to be removed from shopping list: ')
        self.shopping_list.remove(susa)
        print(shopping_list)
        
    def total_price(self, shopping_list_price):
        total_price = 0
        for k in shopping_list_price:
            total_price += k
        print('Total price = R', total_price)       
    
shopping_add = Shopping_cart(0) # 0 because there are no objects to input, but why the 'class' not the 'method
shopping_add.add_item()

list1 = ['apples', 'pears']
shopping_remove = Shopping_cart(list1) # For some reason we need to add 'list1' to both lines
shopping_remove.remove_item(list1)

list_prices = [20, 50, 20]
shopping_prices = Shopping_cart(list_prices)
shopping_prices.total_price(list_prices)
    # I'm not wrong, but their way makes more sense, especially the (item, price) thing

# Question 11
    # Lacks specificity, I did it while looking at the solution
class Bank:
    def __init__(self):
        self.client = {} # Initialize empty dictionary
    
    def create_account(self, account_number, initial_balance=0):
        if account_number in self.client:
            print('Account number already exists')
        else:
            self.client[account_number] = initial_balance
            print('Account created successfully')
        
    def make_deposit(self, account_number, amount):
        if account_number in self.client:
            self.client[account_number] += amount
            print('Deposit successful')
        else:
            print('Account number does not exist')
        
    def make_withdrawal_or_purchase(self, account_number, amount):
        if account_number in self.client:
            if self.client >= amount:
                self.client[account_number] -= amount
                print('Account debited')
            else:
                print('Insufficient funds')
        else:
            print('Account number does not exist')
            
    def check_balance(self, account_number):
        if account_number in self.client:
            balance = self.client[account_number]
            print(f'Account balance: {balance}')
        else:
            print('Account number does not exist')
            
banking = Bank()

banking.create_account(62662, 5000)
banking.make_deposit(62662, 10000)
banking.check_balance(62662)
    # Not difficult, its a good example