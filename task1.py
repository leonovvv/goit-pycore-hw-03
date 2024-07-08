from datetime import datetime

def get_days_from_today(date):
    try:
        # Parse the input date string into a datetime object
        input_date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        # Handle incorrect date format
        return "Incorrect date format. Please use 'YYYY-MM-DD'."
    
    # Get today's date
    today = datetime.today()
    
    # Calculate the difference in days
    difference = (today - input_date).days
    
    return difference

# Example usage:
date_str = '2020-10-09'
days_difference = get_days_from_today(date_str)
print(f"The difference between {date_str} and today is {days_difference} days.")

# Example with incorrect format:
incorrect_date_str = '10/09/2020'
incorrect_days_difference = get_days_from_today(incorrect_date_str)
print(f"The result for incorrect date format is: {incorrect_days_difference}")