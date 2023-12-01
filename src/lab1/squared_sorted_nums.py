def squared_sorted_nums(nums):
    squared_nums = []
    for num in nums:
        squared_nums.append(num ** 2)
    squared_nums.sort()
    return squared_nums
