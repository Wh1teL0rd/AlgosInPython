def biggest_kth_element_in_arr(nums, k):
    if k <= 0 or k > len(nums):
        return "Wrong k"

    sorted_nums = sorted(nums, reverse=True)

    kth_biggest = sorted_nums[k-1]

    position = nums.index(kth_biggest)

    return kth_biggest, position
