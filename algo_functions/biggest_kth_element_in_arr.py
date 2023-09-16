def biggest_kth_element_in_arr(nums, k):
    if k <= 0 or k > len(nums):
        return "Wrong k"

    if len(nums) < k:
        return "Length of array < k"

    sorted_nums = sorted(nums, reverse=True)

    kth_biggest = sorted_nums[k-1]

    position = nums.index(sorted_nums[k-1])

    return kth_biggest, position
