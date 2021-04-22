my_list = [10, 20, 30, 40]
dict = current = {}
for name in my_list:
    current[name] = {}
    current = current[name]
print(dict)