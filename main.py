from algo_functions.find_shortest_path import find_shortest_path

with open("input.txt", "r") as input_file:
    N = int(input_file.readline().strip())
    src = tuple(map(int, input_file.readline().strip().split(',')))
    dest = tuple(map(int, input_file.readline().strip().split(',')))

result = find_shortest_path(N, src, dest)
with open("output.txt", "w") as output_file:
    output_file.write(str(result))

print("Найкоротший шлях:", result)
