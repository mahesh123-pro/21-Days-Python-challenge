import calendar
year = int(input("Enter the year (e.g., 2023): "))
month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day (1-31): "))
day_of_week = calendar.weekday(year, month, day)
days= ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_name = days[day_of_week]
print(f"The day of the week for {year}-{month:02d}-{day:02d} is {days[day_of_week]}.")