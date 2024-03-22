#### num_list1 = [10,20,30,11,22], num_list2 = [20,10,30,40,22], num_list3 = [30,20,22,50,60] 
#### write a python program to find the minimum element in a rated and sorted list ?

# Given lists
num_list1 = [10, 20, 30, 11, 22]
num_list2 = [20, 10, 30, 40, 22]
num_list3 = [30, 20, 22, 50, 60]

# Function to find minimum element in a rated and sorted list
def find_minimum_element(rated_sorted_list):
    if not rated_sorted_list:
        return None
    else:
        return rated_sorted_list[0]

# Find the minimum element in each list
min_num_list1 = find_minimum_element(num_list1)
min_num_list2 = find_minimum_element(num_list2)
min_num_list3 = find_minimum_element(num_list3)

# Compare the minimum elements from each list
overall_min = min(min_num_list1, min_num_list2, min_num_list3)

# Print the overall minimum element
print("Overall minimum element in the rated and sorted lists:", overall_min)
