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

# Question 3
# say More
h = 7
