# Python Naming Conventions
# Python uses snake case - every new word in the variable name is separated by an underscore
# cannot have spaces in variable names

name = "Ryan" #assigning a variable to a string
# string anything in double or single quotes

# snake case when more than one word is being used
my_dog = "Eyo"

# creating a user_name
user_name = "Johnny"

# snake case for function names
def add_nums():
    pass

# Pascal Case for class names
class ParkingGarage:
    pass

# UPPER CASE snake_case for constant variables
BE_CORE_WEEKS = 4 #constant variable is something that is not likely to change

# DONT USE CAMEL CASE - javascript uses camel case
myVar = "something"

# other naming convention conventions
# make sure our names make sense
name = 5 # that doesnt make sense
number = "Lando" # this also doesnt make sense
# DO THIS
name = "Lando"
number = 5

# code comment, # make lines invisible to the interpreter
# ctrl + / to comment and uncomment code

# INDENTATION
# indetantion is how define blocks of code
if 5 > 2: #first block 
    # nested, second block
    print("Five is greater than two") #indenting is one tab or 4 spaces
# blocks of code all the way to the left
# will always new and separate blocks from the previous lines
if 2 < 5:
    print("two is less than five")

# printing in python
# printing lets us send information to our terminal
print()
print("hello", "goodbye", 1, 2, 3)
print("hello", "1", "2.5")

my_name = "Ryan"
print(my_name)
print("hello", end=" ")
print("goodbye")

# Indentation Conutinue
# be careful with indentation errors
# while having a single space will let your code run
# we want to make sure we're tabbing or using 4 spaces so our code is readable
if 5 > 2:
 print("That is true")
    

if 2 < 5:
  print("this is also true")

# DONT DO THIS - indentation error
# if 5 > 2:
#   print("That is true")
#     print("hello")
    
# if True:
# print("Please indent me!")
# This gives an indentation error - the block below a colong must be indented

# highlight and tab to tab several lines of code
# highlight and shift tab to back space several lines of code
if 10 < 15:
    print("that is True")
    print("so totally super true")
    print("its very true and cool")

# MultiLine Statements in Python
my_statement = """
Using 3 quotes allows us to
write on several lines inside 
of a string. This is also known
as a docstring!
"""

print(my_statement)

# escaping a new line
my_escaped_new_line = "Hello there, I hope you're \
doing very well today!"

print(my_escaped_new_line)

# Python recognizes "" and '' as a string
# escape apostrophe in a single quote string
dog_sentence = 'My dog is very cute. My dog\'s name is Eyo'
print(dog_sentence)
# using single quotes within double quotes
dog_sentence = "My dog is very cute. My dog's name is Eyo."

# Use a multi-line string to write out your favorite quote
# even if it isn't that long, see if you can get it on at least two lines.

my_fav_quote = """
it is,
what it is.
"""

my_fav_quote2 = """“
“Watch your thoughts, they become your words; 
watch your words, they become your actions; 
watch your actions, they become your habits; 
watch your habits, they become your character; 
watch your character, it becomes your destiny.” 
-Lao Tzu
"""

my_fav_quote_3 = """Today I'm learning Python 
This is awesome
feeling smart"""

my_fav_quote4 = "They're taking the hobbits to isengard"

cool_quote = """Success is not final;
 failure is not fatal: 
 It is the courage to continue that counts."""

favorite_quote = """
The future belongs to those who believe 
in the beauty of their dreams. 
"""
print(favorite_quote)

my_fav_quote = """Whatever happens,
happens.
"""

my_fav_quote = """
when you control a mans thoughts
you do not have to worry 
about his actions
"""

my_first_quote = """Today Im learning Python 
This is awesome
feeling smart"""

# DEFINING VARIABLES IN PYTHON
# a variable in python is a container for a a specific value
cookies = 10 #cookies is the variable name, 10 is the value associated with cookies
print(cookies)

# We need variables because we reuse a lot of code
# and we need to be able to assign and reassign variables to hold on to scecific values

# printing a greeting
print("Hello there")
greeting = "Hello There"
print(greeting)
greeting = greeting + " Ryan" #string concatenation - adding two strings together
print(greeting)

# storing user input to a variable
# using that variable to print a message
# user_name = input("What is your name?")
# print("Hello " + user_name)

print("Hello please enter your username")
# username = input()
# print(username)

# variable names are case sensitive
user_name = "Krillin"
USER_NAME = "Mega Man"
print(user_name)
print(USER_NAME)

coffee = "Strong Dark Roast"
Coffee = "Light cold brew"

print(coffee)
print(Coffee)

# Assigning multiple variables on a single line
# unpacking a tuple - more on that later!
 
x, y, z = "apple", "banana", "cherry"
# 1 2 3 = V1 V2 V3
print(x)
print(y)
print(z)
# fruits = "apple", "banana", "cherry"
# print(fruits)

# PYTHON TYPING - dynamically typed
# we can assign any variable to any type
# we can reassign any variable to any new type

# STRING
beach = "Sunny Shore"
print(beach)
# use the type() to find out the type of a variable
print(type(beach))

# NUMBERS
# INTEGER - any whole number
waves_today = 5
print(type(waves_today))
# FLOAT - any decimal number
wave_height = 1.3
print(type(wave_height))

# reassigning wave_height to a string
wave_height = "1.3 ft"
print(wave_height)
print(type(wave_height))

# BOOLEAN - True and False
is_sunny = True
is_raining = False
print(type(is_sunny))
print(type(is_raining))

# TYPE CASTING - changing the type of data
# int() - change to a int type
# str() - changes to a string type
# float() - changes to a float type

x = 123
print(type(x))

y = str(x)
print(type(y))

# changing type and reassigning variable to new type
number = "567"
print(type(number))
number = int(number)
print(type(number))

my_num = "123.456"
print(type(my_num))

my_num = float(my_num)
print(type(my_num))

# changing an integer to a float changes it from a whole number to a number.0
my_int = 4
print(my_int) # 4
print(type(my_int))
my_float = float(my_int)
print(my_float) # 4.0
print(type(my_float))

# changing float to an integer rounds down to the nearest whole number
my_float = 5.7
print(my_float)
my_int = int(my_float)
print(my_int)

# type casting with user input
# number = int(input("Enter a number to be added to 10")) #input will always return a string type
# # using the int function on the input to make sure the number being entered 
# # is an integer type so that we can add below
# new_number = 10 + number
# print(new_number)

# possible errors when type casting
# ValueError - cannot convert letter charactesr to a number
# name = "Charizard"
# name = int(name)

# Python is Dynamically Typed
# we dont need to tell the variable what type is
# its going to figure it out when we assign it
# allows us to reassign variables to any other type
my_variable = "Hello, World!" # this is a string
# python knows its a string because of the way it is
print(my_variable)

my_variable = 12345 # dynamic typing allows reassignment to any other type
print(my_variable)

# PYTHON ARITHMETIC OPERATORS +,-,*,/,<,>
# Addition +
strawberries = 10
blueberries = 15
mixed_fruits = strawberries + blueberries
print(mixed_fruits) # 25
print(10 + 15)

# Subtraction - 
pizza_slices = 8
slices_taken = 3
leftover_pizza = pizza_slices - slices_taken
print(leftover_pizza) # 5
print(8 - 3)

# Multiplication *
cupcakes_per_person = 2
party_guests = 15
total_cupcakes = cupcakes_per_person * party_guests
print(total_cupcakes) # 30
print(2 * 15)

# Division /
pie_slices = 8
people = 4
slice_per_person = pie_slices / people
print(slice_per_person)
print(8 / 4)

# Modulo, Floor Division, Exponent
# Module % - returns the remainder of a division problem
cookies = 14
cookies_per_plate = 3
leftover_cookies = cookies % cookies_per_plate
print(leftover_cookies) # 2 - remainder of 14/3 

# checking if somethign is even
# do i have an even number of cookies?
if cookies % 2 == 0: # is there a remainder when i divide 14 by 2, no just 7
   print("You have an even number of cookies")

# Floor Division // - round down the result of a division to the nearest whole number
total_sandwiches = 7
people = 3
sandwiches_each = total_sandwiches // people
print(sandwiches_each) #2

# Exponents **
# raise a number to the power of the second number
# 4 ** 2 raise 4 to the power of 2
# 4 squared
tea_strength = 2
cups_of_tea = tea_strength ** 2
print(cups_of_tea)

# squaring a number
num = 4
print(num**2)

# Compound assignment operator
treasure = 5
# incrementing a varaiable
treasure += 3 # same as this: treasure = treasure + 3
# taking treasure variable and reassigning to itself and adding 3
print(treasure)

knights = 10
# decrementing a variable
knights -= 3
print(knights)

dragons = 3
dragons *= 2 #dragons - dragons * 2
print(dragons)

archers = 12
archers /= 4 # archers = archers / 4
print(archers)

# Comparison Operators <, >, >=, <=, ==, !=

# equal to, is this thing equal to that thing
# == - checking for equality -> double equals
shirt_a = "striped"
shirt_b = "striped"
identical_shirts = shirt_a == shirt_b
print(identical_shirts)
print(shirt_a == shirt_b)

# not equal !=
# this thing is not equal to that thing
hat_a = "fedora"
hat_b = "beanie"
different_hats = hat_a != hat_b
print(different_hats) #this true that hat_a is not equal to hat_b
print(hat_a != hat_b)

# > greater than, 
my_pokemon_cards = 100
your_pokemon_cards = 95
more_cards = my_pokemon_cards > your_pokemon_cards
print(more_cards)

# < less than
my_yugioh_cards = 500
your_yugioh_cards = 600
less_cards = my_yugioh_cards < your_yugioh_cards
print(less_cards)

vintage_years = 20
old_shirt_age = 20

# >= greater than or equal to
is_shirt_vintage = old_shirt_age >= vintage_years #for checking at least a certain amount
print(is_shirt_vintage)

# <= less than or equal to
hp = 100
attack = 100
is_dead = hp <= attack
print(is_dead)

# Logical Operator True and False vs True or False
has_burger = True
has_fries = False
is_combo_meal = has_burger and has_fries
# and needs both things to be true
print(is_combo_meal)

# or needs only one thing to be true, one or the other can be true
had_snack = has_burger or has_fries
print(had_snack)

# Math operators will follow order of operations
result = 2 + 3 * 2 ** 2
print(result)
# PEMDAS Please Excuse My Dear Aunt Sally

new_result = 2 + 3 - 1
print(new_result)

name = "Boba Fett"
print(name)

# Common Exceptions
# ZeroDivisionError
# when trying to divide by zero
num1 = 10
num2 = 0
# print(num1/num2)

# TypeError
# any time an operation or function is applied to an object of an inappropriate type
# adding incompatible types
# sum = 5 + "10"

# ValueError
# When a function receives an argument of the correct type but the wrong value
# number = int("Yolo")

# NameError
# when the variable is not found - undefined
print(nonexistent_variable)

# lambda - anonymous function
def add_nums(num):
    return num + 5
print(add_nums(10))


# Lambda is an anonymous function, can be used to iterate items through a quick function spin up