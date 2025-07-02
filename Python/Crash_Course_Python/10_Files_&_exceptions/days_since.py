from datetime import datetime, date

# Input from user
user_input = input("Please enter the date in YY/DD/MM format: ")

# Convert string to date object
user_date = datetime.strptime(user_input, "%y/%d/%m").date()

# Today's date
today = date.today()

# Difference in days
days_between = (today - user_date).days

print(f"Days between: {days_between}")


















# from datetime import timedelta, datetime

# today = datetime.now()
# future = today + timedelta(days=10)
# print(future)