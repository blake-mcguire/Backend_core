
# TASK 1: CODE DEBUGGING ADVENTURE GAME

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    action = input("Do you want to light a torch or proceed in the dark")
    if action == 'light a torch':
        print('you see a bear sleeping and run!')
    elif action == 'proceed in the dark':
        print('You wander into the cave and awake a sleeping bear...')
    else:
        pass
else: 
    pass

# TASK 2: EVENT PLANNER
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
food = input("Do you want vegetarian food? Yes/No")
catering = "A Vegetarian option" if food.lower() == 'yes' else "Gourmet meals"
print(f"I reccomend {catering}")