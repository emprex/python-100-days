guest_list = ['maman', 'papa', 'simon', 'zuzana']

for name in guest_list:
    print(f"Dear {name.title()}, I would like to invite you for dinner")

print("Zuzana will not be able to come")

guest_list.remove('zuzana')
guest_list.append('lea')

for name in guest_list:
    print(f"Dear {name.title()}, I would like to invite you for dinner")

print("I have found a bigger Table")

guest_list.insert(0, 'joni')
guest_list.insert(3, 'joyce')
guest_list.append('olivier')

for name in guest_list:
    print(f"Dear {name.title()}, I would like to invite you for dinner")

print("My big table won't arrive on time")

while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Sorry {removed_guest}, but I have to cancel our dinner invitation.")

for name in guest_list:
    print(f"Dear {name.title()}, you are still invited for dinner")

print("Let's empty our list")

while len(guest_list) > 0:
    del guest_list[0]

print(guest_list)




