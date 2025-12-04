from pathlib import Path

input = (Path(__file__).parent / 'input.txt').read_text()

answer = 0

for line in input.splitlines():
    first = max(line[:-1])
    second = max(line[line.index(first) + 1:])
    answer += int(first + second)

print(answer)