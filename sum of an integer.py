#### write a python program to find the sum of the first and last digit of an integer 

def sum_first_last_digit(number):
    # Convert number to string to easily access its digits
    number_str = str(number)
    
    # Extract the first and last digits
    first_digit = int(number_str[0])
    last_digit = int(number_str[-1])
    
    # Calculate the sum of the first and last digits
    sum_first_last = first_digit + last_digit
    
    return sum_first_last

# Test the function
number = int(input("Enter an integer number: "))
result = sum_first_last_digit(number)
print("Sum of the first and last digit:", result)
