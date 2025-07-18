motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# add a new element at the end of the list

motorcycles.append('bmw')
print(motorcycles)

# empty list

names = []

names.append('lea')
names.append('guillaume')
names.append('zuzana')
print(names)

# insert elements in the list

names.insert(0,'razvan')
print(names)

# remove elements from a list 

del names[0]
print(names)

# removing using the pop() method

print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)


