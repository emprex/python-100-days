"""Make a list called sandwich_orders and fill it with the names of vari-
ous sandwiches. Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made."""
sandwich_orders = ['tuna', 'club', 'veggie', 'pastrami', 'pastrami', 'blt']
finished_sandwiches = []
print("The deli has run out of pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')  # Remove all occurrences of 'pastrami'
    print("Sorry, we are out of pastrami sandwiches.")  
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  # Get the first sandwich order
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)        
# Display all finished sandwiches.
print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich.title())
# This code processes a list of sandwich orders, simulating the making of each sandwich
# and moving it to a finished list, then displays the completed sandwiches.