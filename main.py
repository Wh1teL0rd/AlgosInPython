from algo_functions.biggest_kth_element_in_arr import biggest_kth_element_in_arr
from algo_functions.squared_sorted_nums import squared_sorted_nums

print("--- Part 1 ---\n")

nums1 = [-4, -2, 0, 1, 3]
result1 = squared_sorted_nums(nums1)
print(result1)

nums2 = [1, 2, 3, 4, 5]
result2 = squared_sorted_nums(nums2)
print(result2)

print("\n--- Part 2 ---\n")

nums3 = [15, 7, 22, 9, 36, 2, 42, 18]
result3, position = biggest_kth_element_in_arr(nums3, 3)
print(f"k-тий найбільший елемент: {result3}, його позиція (індекс): {position}")
