from pathlib import Path

input = (Path(__file__).parent / 'input.txt').read_text()

answer = 0

input = input.splitlines()

for y, row in enumerate(input):
    for x, spot in enumerate(row):
        if spot == "@":
            rolls = [
                input[y - 1][x - 1] if x > 0 and y > 0 else "",
                input[y - 1][x] if y > 0 else "",
                input[y - 1][x + 1] if x < len(row) - 1 and y > 0 else "",
                input[y][x - 1] if x > 0 else "",
                input[y][x + 1] if x < len(row) - 1 else "",
                input[y + 1][x - 1] if x > 0 and y < len(input) - 1 else "",
                input[y + 1][x] if y < len(input) - 1 else "",
                input[y + 1][x + 1] if x < len(row) - 1 and y < len(input) - 1 else "",
            ]
            if rolls.count("@") < 4:
                answer += 1

print(answer)