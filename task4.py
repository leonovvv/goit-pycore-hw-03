from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        name = user['name']
        birthday_str = user['birthday']
        birthday_date = datetime.strptime(birthday_str, "%Y.%m.%d").date()
        
        # Change the year to the current year to calculate the birthday for this year
        birthday_this_year = birthday_date.replace(year=today.year)
        
        # If the birthday has already passed this year, consider the next year
        if birthday_this_year < today:
            birthday_this_year = birthday_date.replace(year=today.year + 1)
        
        # Calculate the difference in days between today and the birthday
        delta_days = (birthday_this_year - today).days
        
        # If the birthday is within the next 7 days
        if 0 <= delta_days <= 7:
            # If the birthday falls on a weekend, move it to the next working day
            if birthday_this_year.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
                # Calculate the next Monday
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
            
            # Add the user to the congratulations list
            upcoming_birthdays.append({
                'name': name,
                'congratulation_date': birthday_this_year.strftime('%Y.%m.%d')
            })

    return upcoming_birthdays

# Example usage:
users = [
    {'name': 'Alice', 'birthday': '1990.07.01'},
    {'name': 'Bob', 'birthday': '1992.07.05'},
    {'name': 'Charlie', 'birthday': '1995.07.09'},
    {'name': 'David', 'birthday': '1988.07.13'},
    {'name': 'Eve', 'birthday': '1991.07.08'}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

