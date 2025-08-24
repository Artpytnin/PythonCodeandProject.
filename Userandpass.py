# Define stored username and password

stored_username = "artpytnin"
stored_password = "0840867826"

# Prompt user for username and password

input_username = input("Enter username: ")
input_password = input("Enter password: ")



# Check credentials

if input_username == stored_username and input_password == stored_password:
    print("Login successful!")
else:
    print("Invalid username or password.")
