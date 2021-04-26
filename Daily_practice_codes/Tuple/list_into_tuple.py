# Write a Python program to convert a list of tuples into a dictionary

def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di


tups = [("Prabhat", 22), ("Shuvam", 21), ("Vishal", 21),
        ("Soujeet", 20), ("Satyam", 25), ("Rishav", 23),
        ("Vicky", 21), ("Karan", 50)]
dictionary = {}
print(Convert(tups, dictionary))