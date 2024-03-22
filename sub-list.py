#### Given a list [4,2,-3,1,6]  write a python program to find if there is a sub-list with
#### sum equal to zero?

def sublist_with_zero_sum(nums):
    prefix_sum = 0
    seen = set()

    for num in nums:
        prefix_sum += num
        if prefix_sum == 0 or prefix_sum in seen:
            return True
        seen.add(prefix_sum)

    return False

# Given list
nums = [4, 2, -3, 1, 6]

# Check if there is a sublist with sum equal to zero
if sublist_with_zero_sum(nums):
    print("Yes, there is a sublist with sum equal to zero.")
else:
    print("No, there is no sublist with sum equal to zero.")
