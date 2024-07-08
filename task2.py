import random

def get_numbers_ticket(min, max, quantity):
    # Validate input parameters
    if min < 1 or max > 1000 or quantity > max - min + 1:
        return []

    # Generate 'quantity' of unique random numbers in the range 'min' to 'max'
    random_numbers = random.sample(range(1, 101), 5)
    # Sort the numbers before returning
    sorted_numbers = sorted(random_numbers)
    return sorted_numbers

# Example usage:
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)