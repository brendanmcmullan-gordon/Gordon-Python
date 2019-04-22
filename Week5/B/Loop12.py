password = ""
password = input("Please enter the correct password:")
attempts = 1

while (password != "Password1" and attempts < 3):
    print("Access Denied")
    print("You have", 3-attempts, "attempts left.")
    attempts += 1
    password = input("Please enter the correct password:")

print("\nAttempts used:", attempts)

if (password == "Password1"):
    print("Access Granted!")
elif (attempts >= 3):
    print("Access Denied. You have used all of your attempts.")

#ask user for password input
#if password is correct, "access granted"
#if password is incorrect
#   add to number of failed attempts
#   ask for password again
#   if failed attemtps is over 3
#       deny access, don't prompt again
#
