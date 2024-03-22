#### ####  Given python list  [10, 501, 22, 37, 100, 999, 87, 351] find out 
#### how many numbers are there in the given python list which are happy numbers ?

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

happy_count = 0
for num in numbers:
    n = num
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit)**2 for digit in str(n))
    if n == 1:
        happy_count += 1

print("Number of happy numbers in the list:", happy_count)

