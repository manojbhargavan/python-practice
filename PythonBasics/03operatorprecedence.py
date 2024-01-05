# Run this snippet in shell: python Basics/03operatorprecedence.py
# Operator Precedence
print("2 + 3 * 5 - 7 / 11")
print("2 + (3 * 5) - (7 / 11)")
print("2 + 15 - 0.6363636363636364")
print("17 - 0.6363636363636364")
print("16.363636363636363")
print(2 + 3 * 5 - 7 / 11)

# Guess the output of each answer before you click RUN
# Try to write down your answer before and see how you do... keep it mind I made it a little tricky for you :)

print((5 + 4) * 10 / 2) # (9) * (10/2) = 9 * 5 = 45

print(((5 + 4) * 10) / 2) # ((9) * 10) / 2 = (90) / 2 = 45

print((5 + 4) * (10 / 2)) # (9) * (5) = 45

print(5 + (4 * 10) / 2) # 5 + 40 /2 = 5 + (40/2) = 5 + 20 = 25

print(5 + 4 * 10 // 2) # 5 + 40 // 2 = 5 + 20 = 25
