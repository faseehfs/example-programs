# Demonstrating exception handling.

def calculateWeeks():
    try:
        days = int(input("Number of days: "))
        weeks = days // 7

    except ValueError:
        print("Enter integers only.")

    else:
        print(f"Number of weeks in {days} days: {weeks}")

    finally:
        print("Thank you.")

calculateWeeks()
