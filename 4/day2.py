from pathlib import Path

input = (Path(__file__).parent / 'input.txt').read_text()

answer = 0

input = input.splitlines()

while True:
    partial_answer = 0
    next_input = ["" for _ in range(0, len(input))]
    for y, row in enumerate(input):
        for x, spot in enumerate(row):
            removed = spot == "@" and [
                input[y - 1][x - 1] if x > 0 and y > 0 else "",
                input[y - 1][x] if y > 0 else "",
                input[y - 1][x + 1] if x < len(row) - 1 and y > 0 else "",
                input[y][x - 1] if x > 0 else "",
                input[y][x + 1] if x < len(row) - 1 else "",
                input[y + 1][x - 1] if x > 0 and y < len(input) - 1 else "",
                input[y + 1][x] if y < len(input) - 1 else "",
                input[y + 1][x + 1] if x < len(row) - 1 and y < len(input) - 1 else "",
            ].count("@") < 4

            partial_answer += int(removed)
            next_input[y] += "." if removed else spot
    if partial_answer == 0:
        break

    answer += partial_answer
    input = next_input

print(answer)