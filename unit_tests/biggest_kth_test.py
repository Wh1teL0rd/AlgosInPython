import unittest

from algo_functions.lab1.biggest_kth_element_in_arr import biggest_kth_element_in_arr


class TestBiggestKthInArr(unittest.TestCase):
    def test_biggest_kth_element_in_arr(self):
        nums = [15, 7, 22, 9, 36, 2, 42, 18]
        k = 3
        result = biggest_kth_element_in_arr(nums, k)
        self.assertEqual(result, (22, 2))

    def test_wrong_k(self):
        nums = [4, 2, 7, 1, 9]
        k = 0
        result = biggest_kth_element_in_arr(nums, k)
        self.assertEqual(result, "Wrong k")

    def test_length_of_arr_less_than_k(self):
        nums = [4, 2, 7, 1, 9]
        k = 23
        result = biggest_kth_element_in_arr(nums, k)
        self.assertEqual(result, "Wrong k")

    def test_empty_array(self):
        nums = []
        k = 1
        result = biggest_kth_element_in_arr(nums, k)
        self.assertEqual(result, "Wrong k")


if __name__ == '__main__':
    unittest.main()
