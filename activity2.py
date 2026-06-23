#Removing elements from a dictionary

# create a dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6:36, 7: 49}

# remove a particular item, returns its value
# Output: 16
print(squares.pop(4))


print(squares)



print(squares.popitem())


print(squares)