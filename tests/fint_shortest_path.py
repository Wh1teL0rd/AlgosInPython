import unittest

from src.lab4.find_shortest_path import find_shortest_path


class TestFindShortestPath(unittest.TestCase):
    def test_shortest_path(self):
        with open("test_input.txt", "w") as input_file:
            input_file.write("8\n")
            input_file.write("7,0\n")
            input_file.write("0,7\n")

        find_shortest_path("test_input.txt", "test_output.txt")

        with open("test_output.txt", "r") as output_file:
            result = int(output_file.read())
            self.assertEqual(result, 6)

    def test_invalid_path(self):
        with open("test_input1.txt", "w") as input_file:
            input_file.write("8\n")
            input_file.write("0,0\n")
            input_file.write("7,77\n")

        find_shortest_path("test_input1.txt", "test_output1.txt")

        with open("test_output1.txt", "r") as output_file:
            result = int(output_file.read())
            self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
