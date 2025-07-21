# a simple dictinary
alien_O = {'color' : 'greem', 'points' : 5}
print(alien_O['color'])
print(alien_O['points'])

# Accessing values in a dictionary
new_points = alien_O['points']
print(f"You just earned {new_points} points!")

# Adding new key-value pairs

alien_O['x_position'] = 0
alien_O['y_position'] = 25

print(alien_O)

# Starting with an empty Dictionary

alien_O = {}

alien_O['color'] = 'green'
alien_O['points'] = 5

print(alien_O)

# Modifying values in a dictionary

print(f"The alien is {alien_O['color']}.")
alien_O['color'] = 'yellow'
print(f"The alien is now {alien_O['color']}.")




alien_O = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

print(f"Original position: {alien_O['x_position']}")

# move the alien to the right
# determine how far to move the alien based on its curremt speed.

if alien_O['speed'] == 'slow':
    x_increment = 1
elif alien_O['speed'] == 'medium':
    x_increment = 2
else:
    # this must be a fast alien
    x_increment = 3

# the new position is the old position plus the increment

alien_O['x_position'] = alien_O['x_position'] + x_increment

print(f"New position: {alien_O['x_position']}")

# removing key-value pairs

alien_O = {'color': 'green', 'points': 5}
print(alien_O)

del alien_O['points']
print(alien_O)

# nesting 

print("#################################")

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print("#################################")

# make an empty list for storing aliens.

aliens = [] # list []

#makes 30 green aliens
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
        alien['points'] = 15

# show the first aliens
for alien in aliens[:25]:
    print(alien)

print("...")

print(f"Total number of aliens: {len(aliens)}")

