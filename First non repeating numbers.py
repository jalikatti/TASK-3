#### num_list1 = [10,20,30,11,22], num_list2 = [20,10,30,40,22], num_list3 = [30,20,22,50,60] find out the first 
#### non repeating elements in these list of integer using python program

from collections import OrderedDict

def first_non_repeating_element(*lists):
    all_numbers = []
    for num_list in lists:
        all_numbers.extend(num_list)

    count_dict = OrderedDict()
    for num in all_numbers:
        count_dict[num] = count_dict.get(num, 0) + 1

    for num, count in count_dict.items():
        if count == 1:
            return num

    return None

# Given lists
num_list1 = [10, 20, 30, 11, 22]
num_list2 = [20, 10, 30, 40, 22]
num_list3 = [30, 20, 22, 50, 60]

# Find the first non-repeating element
result = first_non_repeating_element(num_list1, num_list2, num_list3)

if result is not None:
    print("First non-repeating element:", result)
else:
    print("No non-repeating element found.")
