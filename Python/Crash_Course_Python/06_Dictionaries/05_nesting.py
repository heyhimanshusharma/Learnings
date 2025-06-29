# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
# 	print(alien

# three aliens with code that automatically generates each alien
# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens

for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['pints'] = 15

# Show the first 5 lines
for alien in aliens[:5]:
	print(alien)
print('...')

# show how many aliens have been created
print(f'Total number of aliens: {len(aliens)}')