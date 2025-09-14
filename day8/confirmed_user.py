# Start with users that need to be confirmed,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# verify each user until there are no more unconfirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    print(f"Confirmed user: {current_user.title()}")    

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())   
# This code verifies users and confirms them, demonstrating a while loop
# that processes a list until it's empty, and then displays the confirmed users.
