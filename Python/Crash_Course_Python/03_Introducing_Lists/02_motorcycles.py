motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'kawasaki' # modifiyed 1st ele.
print(motorcycles)

motorcycles.append('ducati') # appends (adds) new ele. to the end
print(motorcycles)

# Appending an empty list
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# Inserting elements in the list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing from list
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

# Removing an Item Using the pop() Method
motorcycles = ['honda', 'yamaha', 'suzuki', 'pulsar']
owned_motorcycle = motorcycles.pop(-1)
print(f'The first motorcycle I owned is {owned_motorcycle}')

# Removing an item by value
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.remove('yamaha')
print(motorcycles)

# Remove
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(f'\nA {too_expensive.title()} is too expensive for me.')