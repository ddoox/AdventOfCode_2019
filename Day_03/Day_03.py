moves = []

with open("input", "r") as input_file:
    input_file = input_file.readlines()
    for line in input_file:
        moves.append(line.strip())
print(moves)
