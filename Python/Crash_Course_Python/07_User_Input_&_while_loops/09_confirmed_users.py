# start with users that need to be verified
# and an empty list to hold the users
unconfirmed_users = ['alice', 'brian', 'candance']
confirmed_users = []

# Verify each user until there are no more unconfirmed users
# move each verified users into the list of confirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())