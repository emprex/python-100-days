alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['point']) will show an error

# using get() to access values

point_value = alien_0.get('point', 'No point value assigned.')

print(point_value)

