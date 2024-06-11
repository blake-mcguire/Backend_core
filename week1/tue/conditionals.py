# Conditionals
# setting a variable to treu

torch_lit = True

if torch_lit:
    print("venture forth")
    

weather = "Sunny"
# checking for equality in a conditional
if weather == "Sunny":
    print("lets go on a picnic")
    
# if something is not equal
if weather != "rainy":
    print("cool we can play outside today")
    
# Combining conditionals

gold_coins = 10
silver_coins = 50

if gold_coins > 5 and silver_coins > 30:
    print("we have enough to buy the magic potion!")
    
if gold_coins > 5 and gold_coins < 15:
    print("we should keep these coins for now.")


# With "and" both conditions need to be true

# != not equal 
enemy = "goblin"

if enemy != "dragon":
    print("charge forward")
    
# <= less than or equal to 
player_health = 75
if player_health <= 100:
    print("Drink a health potion for full strength")
    
# >= greater than or equal to

player_health = 130

if player_health >= 100:
    print('lookin good')
    
magic_stones = 12
if 10 <= magic_stones <= 20:
    print("You have just the right amount of stones!")

# negative checks using not
is_daytime = False
drgn_asleep = True

if not is_daytime and drgn_asleep:
    print("Try sneaking into the drgaons lair for some dank lootz")

# ELIF STATEMENTS

moon_phase = "full moon"

if moon_phase == "full moon":
    print("beware of warewolves")
elif moon_phase == "new moon":
    print("vampires will sparkle")    

# checking dsome potion strength

potion_strength = 15

if potion_strength > 20:
    print("Very powerful potion")
elif potion_strength > 10:
    print("Its a moderately powerful potion")
    
# Chaining together several elifs in a single condition chain

weather == "rainy"

if weather == "sunny":
    print("go outside")
elif weather == "rainy":
    print("carry an umbrella")
elif weather == "snowy":
    print('build a snowman')
    
sword_material = "silver"

if sword_material == "gold":
    print('The sword shines brightly')
elif sword_material == 'silver':
    print('that sword is great for killing werewolves')
elif sword_material == 'bronze':
    print('THat sword sucksssss')
    
# using comparison operatorsd and a range w
player_lvl = 12
if player_lvl < 5:
    print("You may enter the weenie hut junior dungeon")
elif 5 <= player_lvl:
    print('you may enter the advanced dungeon')
elif 10 <= player_lvl <= 20:
    print('you may enter the advanced dungeon')
else:
    print('you are ready to advance to the ringed city') 
    
# ELSE - cover any confition not accounted for

# using else with a user input to makes sure the correct response is collected

is_dragon_present = True
has_treasure = False

if is_dragon_present and not has_treasure:
    print('not worth your time')
elif not is_dragon_present and has_treasure:
    print('free loot')
elif is_dragon_present and has_treasure:
    print('the dragon guards his hoard')
else:
    print('empty cave')


# cowmbining potions
red_potion = True
blue_potion = False

if red_potion and not blue_potion:
    print('you got a potion of strngth')
elif not red_potion and blue_potion:
    print('you got a potion of speed')
elif red_potion and blue_potion:
    print('dont mix your potions they explode')
else:
    print('you have no potions')
    
is_daytime = False
is_raining = False

if is_daytime:
    print('Take the sunny path through the meadow')
elif is_raining:
    print('Take the dank path through the swamp')
else:
    print('neither path is suitable right now go back home')
    
# checking user input 
light_color = input("input a color; red, green or yellow")
if light_color == 'red':
    print('stop')
elif light_color == 'yellow':
    print('floor it through the intersection')
elif light_color == 'green':
    print('GO!')
else:
    print('call the dot the lights are messed up!')
    
# collecting user input to check what movie rating they would like to see
# and collecitng age to see if they are
# old enough fo that movie
# age = int(input("enter your age:"))
# rating = input('Enter a movie rating: (G, PG, PG-13, R): ')
# if rating == "G":
#     print('You can watch that movie')
# elif rating == 'PG' and age >= 7:
#     print('you can watch that movie')
# elif rating == 'PG-13' and age >= 13:
#     print 

# checking how people take their coffee

days_overdue = int(input("How many days is the book overdue? "))
fine = 0

if days_overdue <= 5:
    fine = days_overdue * 1
elif days_overdue <= 10:
    fine = days_overdue * 2
else:
    fine = days_overdue * 5
print(f"your fine is {fine}")

# NESTED CONDITIONALS

# CHECKING AGE RESTRICTIONS

age = 18
if age >= 18:
    if age >= 21:
        print('you can drive vote and drink')
    else:
        print('you can drive and vote')
else:
    print('You are too young to drive or vote')

# weekend activities
day = 'Saturday'
time = 'Morning'
if day == 'Saturday':
    if time == 'Morning':
        print('watch some cartoons')
    elif time == 'Afternoon':
        print('Get some wings')
    elif time == 'Evening':
        print('Doing some Yoga')
    else:
        print('kickin it')
        
genre = "Fantasy"
author = "JRR Tolkien"

if genre == "Fantasy":
    if author == 'JK Rowling':
        print('Harry Potter')
    elif author == 'JRR Tolkien':
        print('Lord of the rings')
    else:
        print('thats a book by another author')


# super nested list 
fruit = 'Apple'
is_ripe = True
has_spots = True

if fruit == 'Apple':
    if is_ripe and not has_spots:
        print("Oh baby, a perfect apple")
    elif not is_ripe and not has_spots:
        print('Let it ripen a bit more')
    else:
        print('this is a great apple for pie')
elif fruit == 'Banana':
    if is_ripe and not has_spots:
        print('This banana is ready to eat!')
    elif not is_ripe:
        print('This banana is green!')
    else:
        print('this is a great banana for bread!')
        
        
# Checking some movie release dates 

movie = 'Lord of the Rings: The Two Towers'
release_year = 2002
duration_minutes =220

if movie == 'Inception':
    if 2000 <= release_year <= 2020 and duration_minutes > 120:
        print('A modern calssic with a runtime of over 2 hours')
    elif release_year < 2000:
        print('A gem from the past')
    else:
        print("a recent masterpiece")
elif movie == "Lord of the Rings: The Two Towers":
    if 2000 <= release_year <= 2020 and duration_minutes > 180:
        print('an absolutely wonderful movie')
    elif release_year < 2000:
        print('A pretty cool movie')
    else:
        print('A very recent film')
else:
    print('Im sure that is also a great movie')
    
# SHORTHAND CONMFITIONAL - Ternary
# shorthand is best used when the outcomes and the conditions can be
# expressed on a single line
x, y = 5, 10

# what is being executed if this case esle exeuter this
print('x is greater') if x > y else print('y is greater')
# set a variable with the shorthand
weather = "sunny"
activity = 'beach' if weather == 'sunny' else 'video games'

# using a range within the shorthand -> with parentheses

hour_of_day = 7
energy_lvl = 3

beverage = "coffee" if 6 <= hour_of_day < 12 and energy_lvl < 4 else "tea"

# PASS - allows us to skip over a block of code and come back to it later
# defining functions and you dont know what you want it to do yet
if beverage == "coffee":
    pass
elif beverage == "tea":
    print('enjoy your tea with some nice crumpets')
    
# you can apply the pass to conditionals, functions, loops