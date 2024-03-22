##### num_list1 = [10,20,30,11,22], num_list2 = [20,10,30,40,22], num_list3 = [30,20,22,50,60] 
#### find the duplicates in these list using python program?

num_list1 = [10, 20, 30, 11, 22]
num_list2 = [20, 10, 30, 40, 22]
num_list3 = [30, 20, 22, 50, 60]

# Find duplicates
duplicates = set(num_list1) & set(num_list2) & set(num_list3)

if duplicates:
    print("Duplicates found:", duplicates)
else:
    print("No duplicates found.")
