def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Get user input
user_input = input("Enter a year: ")

# Check if the input is a valid integer
try:
    year = int(user_input)
except ValueError:
    print("Please enter a valid integer for the year.")
    exit()

# Check if it's a leap year
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")