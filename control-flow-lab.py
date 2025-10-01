
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
    dog_age = input("Enter your dog's age in human years: ").strip()
    if not dog_age.isdigit():
        print("Please enter a valid age.")
        return
    if int(dog_age) < 0:
        print("Age cannot be negative.")
        return
    if int(dog_age) == 2:
        human_years = int(dog_age) * 10
        print(f"Your dog is {human_years} years old in human years.")
    else:
        int(dog_age) > 2
        human_years = 20 + (int(dog_age) - 2) * 7
        print(f"Your dog is {human_years} years old in human years.")
    
# Call the function
calculate_dog_years()

def weather_advice():
    # Your control flow logic goes here
    cold = input("Enter (yes/no) if it is cold: ").strip().casefold()
    raining = input("Enter (yes/no) if it is raining: ").strip().casefold()
    if cold == "yes" and raining == "yes":
        print("Wear a waterproof coat.")
    elif cold =="yes" and raining == "no":
        print("Wear a warm coat.")
    elif cold =="no" and raining == "yes":
        print("Carry an umbrella")
    else:
        print("Wear light clothing.")
    
# Call the function
weather_advice()

def determine_season():
    # Your control flow logic goes here
    valid_months =["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    while True:
        month = input("Enter month (3 character, e.g Jan, Feb, Mar): ").strip().title()
        if month not in valid_months:
            print("Please enter a valid month abbreviation (e.g Jan, Feb, Mar)")
            continue

        day = input("Enter day of the month (1-31): ").strip()
        if not day.isdigit() or not (1 <= int(day) <= 31):
            print("Please enter a valid day (1-31).")
            continue
        if month == "Dec" and int(day) >= 21 or month in ["Jan", "Feb"] or month == "Mar" and int(day) <= 19:
            print("It is Winter.")
        elif month == "Mar" and int(day) >= 20 or month in ["Apr", "May"] or month == "Jun" and int(day) <= 20:
            print("it is Spring.")
        elif month == "Jun" and int(day) >= 21 or month in ["Jul", "Aug"] or month == "Sep" and int(day) <= 21:
            print("It is Summer.")
        else:
            print("It is Fall.")
        return
# Call the function
determine_season()