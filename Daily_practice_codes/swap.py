# Python program to swap two variables

x = input('Enter first number: ')
y = input('Enter second number: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))