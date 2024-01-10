# User Input from 1 to 5
# user_input_accepted = False
# numbers = ['One', 'Two', 'Three', 'Four', 'Five']

# while not user_input_accepted:
#     user_input = int(input("Enter a number between 1 and 5 inclusive >>> "))
#     if user_input >= 1 and user_input <= 5:
#         print(f"Well done, you have entered {user_input}")
#         print(f"Spelt {numbers[user_input-1]}")
#         user_input_accepted = True
#     else:
#         print("Try again...")

# User Input One two etc 
# user_input_accepted = False
# numbers = ['One', 'Two', 'Three', 'Four', 'Five']
# while not user_input_accepted:
#     user_input = input('Enter the text of the number you want: ')
#     index = 0
#     for curIndex in range(0, len(numbers)):
#         if numbers[curIndex].lower() == user_input.lower():
#             print(f"{user_input} is {curIndex+1}")
#             user_input_accepted = True
#             break
    
#     if not user_input_accepted:
#         print("I don't understand, try again...")

# not_so_random_number = 4
# user_input = input("Guess a number between 1-10 inclusive >>> ")
# if user_input.isdigit():
#     input_number = int(user_input)
#     if input_number == not_so_random_number:
#         print("You guessed right")
#     elif input_number > not_so_random_number and input_number <= 10:
#         print("Your guess is on the bigger side")
#     elif input_number < not_so_random_number and input_number >= 1:
#         print("Your guess is on the lower side")
#     else:
#         print("Your guess is not in range")
# else:
#     print("Aint a number.")

# user_input = input("What's your name >>> ")
# if len(user_input) > 5:
#     print(f"Your name has {len(user_input)} characters")
# else:
#     print(f"Hello {user_input}, your names a bit short ha..")

def get_number(range_start, range_end):
    user_input_accepted = False
    user_num = 0
    while not user_input_accepted:
        user_input_num = input(f"Enter an number between {range_start} and {range_end} inclusive >>> ")
        if not user_input_num.isdigit():
            print("That's not a number.. Try again..")
            continue
        
        user_num = int(user_input_num)
        if user_num < range_start or user_num > range_end:
            print("Number is not in range.. Try again..")
            continue
        
        user_input_accepted = True
    
    return user_num

# num1 = get_number(1, 20)
# num2 = get_number(1, 20)

# if num1 > 15 and num2 > 15:
#     print(f"Product = {num1 * num2}")
# elif num1 > 15 or num2 > 15:
#     print(f"Sum = {num1 + num2}")
# else:
#     print("..Zero..")


num1 = get_number(1, 20)
num2 = get_number(1, 20)

print(num1, num2)
num1,num2 = num2, num1
print(num1, num2)