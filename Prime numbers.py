#### given python list [10,501,22,37,100,999,87,351] count all the prime numbers and create 
#### new list which will contain all the prime numbers in it 

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Function to check if a number is prime or not
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Initialize an empty list to store prime numbers using above list
prime_numbers = []

# Count of prime numbers from the above list
prime_count = 0

# Iterate through the given above list
for num in numbers:
    # Check if the number is prime or not 
    if is_prime(num):
        prime_numbers.append(num)  # Add prime number to the list
        prime_count += 1

# Print the count of prime numbers and the list of prime numbers using above list
print("Count of prime numbers:", prime_count)
print("List of prime numbers:", prime_numbers)
