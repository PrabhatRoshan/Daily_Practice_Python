# Write Python code that asks a user how many pizza slices they want.
# The pizzeria charges Rs 123.00 a slice. if user order even number of slices, 
# price per slice is Rs 120.00. Print the total price depending on how many slices user orders

user=int(input("How many pizza slices?? : "))
tot=0
if user % 2 == 0:
    tot= user*120.00
else:
    tot= user*123.00
print(tot)