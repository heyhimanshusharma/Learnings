locations = ['Norway', 'Switzerland', 'Morocco']
print(locations)
print(sorted(locations))
print(locations) # still in original form
reverse_locations = sorted(locations, reverse=True)
print(reverse_locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)