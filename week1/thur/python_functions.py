# TASK 1 BLAKES COOLEST CALCULATOR
def calculator():
    while True:
        print("""Welcome to Blake's Coolest Command Line Calculator!
                
        Enter: '1' if you would like to add.
        Enter: '2' if you would like to subtract.
        Enter: '3' if you would like to multiply.
        Enter: '4' if you would like to divide.
        Enter: '5' TO QUIT 
        """)
        
        menu_choice = input("What would you like to do?: ")
        
        if menu_choice in {'1', '2', '3', '4', '5'}:
            if menu_choice == '5':
                break
            
            num1 = int(input("Enter Your first number: "))
            num2 = int(input("Enter Your second number: "))
            
            if menu_choice == '1':
                result = num1 + num2
            elif menu_choice == '2':
                result = num1 - num2
            elif menu_choice == '3':
                result = num1 * num2
            elif menu_choice == '4':
                result = num1 / num2
            
            print(f"Your result is: {result}")
        else:
            print("Please input a valid integer!")
            
            
    # TASK #2 GROCERY BAGGIN
    # May not run properly on the first run -- not sure if its my code runner extension but it should run well on the second run!

def postmates_competitor():
    customer_cart = {}
    available_groceries = {"Eggs": 12, "Milk": 7, "Vegetables": 13, "Chicken": 8, "Ice Cream": 6, "Bread": 8, "The Ark Of The Covenant": 12}
    while True:
        print("""
                        
                        Howdy Shopper!
                        
              Press 1 to view the grocery selection
              Press 2 to view your cart
              Press 3 to remove an item from your cart
              Press 4 to add an item to your cart
              Press 5 to checkout
              Press literally anything else to quit!
              """)
        menu_choice = input("What can I do ya for?: ")
        if int(menu_choice) == 1:
            for grocery, price in available_groceries.items():
                print(f"""{grocery} ${price}""", end=' ~ ')
                
        elif int(menu_choice) == 2:
            if customer_cart:
                print("Your Cart Contains:")
                for item, price in customer_cart.items():
                    print(f"{item}: {price}")
            else:
                print("You do not have any items in your cart at the moment!")
        
        elif int(menu_choice) == 3:
            print("Your cart contains:")
            items = list(customer_cart)
            for idx, item in enumerate(items, start=0):
                print(f"{idx}. {item}")
                
            item_to_remove = int(input("Enter the number of the item you want to remove: ")) 
            if 0 <= item_to_remove < len(customer_cart):
                    removed_item = items[item_to_remove]
                    customer_cart.pop(removed_item)
                    print(f"Removed {removed_item} from your cart.")
            else:
                    print("Invalid selection.")
            print(customer_cart)
        elif int(menu_choice) == 4:
            for grocery, price in available_groceries.items():
                print(f"""{grocery} ${price}""", end=' ~ ')
            user_add = input("""
                             Enter what item you would like to add to your cart!: 
                             """)
            if user_add in available_groceries:
                customer_cart[user_add] = available_groceries[user_add]
                print(f"Added {user_add} to your cart")
            else:
                print("Item Not Available.")
        elif int(menu_choice) == 5:
            if customer_cart:
                total = sum(customer_cart.values())
                print(f"Your total is ${total}, Thank you for shopping with us!")
                break
            else:
                print('You have nothing to checkout!')
        else:
            break
                
postmates_competitor()