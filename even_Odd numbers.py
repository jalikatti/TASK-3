#### write a python program to given list [10,501,22,37,100,999,87,351] create two list one which have all the even numbers 
### and another list will have all the odd numbers

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Initializing empty lists for even and odd numbers
even_numbers = []
odd_numbers = []

# Iteraterting through the given above list
for num in numbers:
    # Check if the number is even in the above list
    if num % 2 == 0:
        even_numbers.append(num)  # Append to even_numbers in the given above list
    else:
        odd_numbers.append(num)   # Append to odd_numbers in the given above list

# Print the lists even or odd as per above list
print("List of even numbers:", even_numbers)
print("List of odd numbers:", odd_numbers)
