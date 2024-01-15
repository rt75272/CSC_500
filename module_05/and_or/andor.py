# Ask if the user knows the answer to the universe.
user_input = int(input("What is the answer to the universe? ")) 
answer = 42 # Set the answer to the universe.

# Simple AND example.
if user_input == answer and True:
    print("Correct")
else:
    print("Incorrect")

# Simple OR example.
if user_input == answer or False:
    print("Correct")
else:
    print("Incorrect")

# Simple AND example.
if True and True:
    print("True")

# Simple OR example.
if True or False:
    print("True")