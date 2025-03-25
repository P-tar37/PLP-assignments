my_list = [10, 20, 30, 40]

my_list.insert(1, 15)

my_List1 = [50, 60, 70]
my_list.extend(my_List1)

#printing the output after extending the list
print(my_list)

# removing the last element from my_list
my_list.pop(-1)
print(my_list)

# sorting list
my_list.sort()
print(my_list)

# index of value 30 in my_list
value = 30
index = my_list.index(value)
print(index)