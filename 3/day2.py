from pathlib import Path

input = (Path(__file__).parent / 'input.txt').read_text()

answer = 0

for line in input.splitlines():
    joltage = ""
    for i in reversed(range(0, 12)):
        joltage += max(line[:-i]) if i != 0 else max(line)
        line = line[line.index(joltage[-1]) + 1:]
    answer += int(joltage)

print(answer)