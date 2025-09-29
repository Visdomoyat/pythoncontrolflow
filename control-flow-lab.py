
def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()

def check_letter():
    # Your control flow logic goes here
    letter = input("Enter a letter: ").strip().casefold()
    if letter in "aeiou":
        print(f"{letter} is a vowel.")
    elif letter in "bcdfghjklmnpqrstvwxyz":
        print(f"{letter} is a consonant.")
    else:
        print(f"{letter} is not a letter, please enter a letter.")
        
# Call the function
check_letter()

def check_voting_eligibility():
    # Your control flow logic goes here
    age = input("Enter your age: ").strip()
    if not age.isdigit():
        print("Please enter a valid age.")
        return
    if int(age) >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
    
# Call the function
check_voting_eligibility()

def calculate_dog_years():
    # Your control flow logic goes here

# Call the function
calculate_dog_years()