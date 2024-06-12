
# Task 1


number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
elif number < 0:
    print("The number is negative.")
    
# TASK 2

inp1 = int(input("Enter a number!: "))
inp2 = int(input("Enter a second number!: "))
inp3 = int(input("Enter a final number!"))

print(f"the largest number you entered was {max([inp1, inp2, inp3])}")
