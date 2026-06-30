# Test dictionary
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

# Print the dictionary
print("Test Dictionary:", test_dict)

# Take input from the user
value = input("Enter the value to check its frequency: ")

# Count the frequency of the value
frequency = list(test_dict.values()).count(int(value))

# Print the result
print("Frequency of", value, "is:", frequency)