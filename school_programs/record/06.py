# Demonstrating exception handling.

# Write a function that calculates the number of weeks from a given number of days, with proper error handling.

def calculate_weeks():
    try:
        days = int(input("Number of days: "))
        weeks = days // 7
    except ValueError:
        print("Enter integers only.")
    else:
        print(f"Number of weeks in {days} days: {weeks}")
    finally:
        print("Thank you.")

calculate_weeks()
