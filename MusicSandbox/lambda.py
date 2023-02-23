add = lambda x, y: x + y #  x and y are the parameters and x + y is the expression
result = add(2, 3)
print(result) # Output: 5

# is the same as

def add(x, y):
    return x + y

result = add(2, 3)
print(result) # Output: 5


numbers = [1, 2, 3, 4, 5] # list of numbers
squared_numbers = map(lambda x: x ** 2, numbers) # map() applies the lambda function to each element in the list
print(list(squared_numbers)) # Output: [1, 4, 9, 16, 25]


# which is the same as

numbers = [1, 2, 3, 4, 5]
def square(x):
    return x ** 2

squared_numbers = []
for number in numbers:
    squared_numbers.append(square(number))

print(squared_numbers) # Output: [1, 4, 9, 16, 25]


