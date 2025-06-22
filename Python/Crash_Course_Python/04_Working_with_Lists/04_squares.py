squares = [] # creates an empty list
for value in range(1,11):
	squares.append(value ** 2)
print(squares)

print(max(squares))
print(min(squares))
print(sum(squares))

# list comprehension
squares = [value ** 2 for value in range(1,11)]
print(squares)