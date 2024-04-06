my_list = ["apple", "banana", "cherry"]
# Convert the list into a single string with elements separated by comma and space
list_as_string = ", ".join(my_list)

print(list_as_string)

# output
# apple, banana, cherry

string_as_list=list(list_as_string)
print(string_as_list)

# output
# apple, banana, cherry
# ['a', 'p', 'p', 'l', 'e', ',', ' ', 'b', 'a', 'n', 'a', 'n', 'a', ',', ' ', 'c', 'h', 'e', 'r', 'r', 'y']