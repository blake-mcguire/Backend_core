import random

# TASK 1 
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
# print(days_of_week[i] for i in range(len(days_of_week)) if i % 2 == 0)

for i in range(len(days_of_week)):
    if i % 2 == 0:
        print(days_of_week[i])
        
# TASK #2
counter = 0

while counter < 5:
    counter += 1
    print(f"You have looped {counter}x!")
    
# TASK #3

list_of_items = ['Tennis Ball', 'B-52 Bomber','Cup','Moldovan Flag', 'Sword of 1000 Truths']
computer_guess = random.choice(list_of_items)


while True:
    print(f"You have to guess which item in this list has been provided: {list_of_items}")
    user_inp = input("insert your guess here: ")
    
    if user_inp == computer_guess:
        print("Congratulations, You have guessed correctly")
        break
    else:
        print("incorrect Try again!")
    