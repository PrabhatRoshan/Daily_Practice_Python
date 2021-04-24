# Write a python program to check if the input number is
# -real number
# -float number
# -string
# -complex number
# -Zero (0)

n =int(input("Enter any number: "))

if type(n) == type(1):
    print("Entered number is a Real Number...")
elif type(nr) == type(1.0):
    print("Entered number is a Float Number...")
elif type(n) == type("Abc"):
    print("Entered number is a String...")
elif type(n) == type(1 + 2j):
    print("Entered number is a complex number...")
elif n == 0:
    print("Entered number is 0...")
else:
    print("unknown type...")

