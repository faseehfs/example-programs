# Demonstrating exception handling.

def calculateWeeks():
    try:
        days = int(input("Enter no. of days: "))
        weeks = days // 7

    except ValueError:
        print("Enter integers only.")

    else:
        print(f"No. of weeks in {days} days: {weeks}")

    finally:
        print("Thank you.")

calculateWeeks()
