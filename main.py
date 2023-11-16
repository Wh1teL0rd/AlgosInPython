from algo_functions.lab5.count_of_pairs import count_of_pairs
from algo_functions.lab5.read_input import read_input
from algo_functions.lab5.write_output import write_output

# Зчитуємо вхідні дані з файлу
input_filename = 'input.txt'
N, pairs = read_input(input_filename)

# Рахуємо кількість можливих пар
result = count_of_pairs(pairs)

# Записуємо результат у файл
output_filename = 'output.txt'
write_output(output_filename, result)
