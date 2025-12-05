from pathlib import Path

input = (Path(__file__).parent / 'input.txt').read_text()

answer = 0

ranges, ids = [part.splitlines() for part in input.split("\n\n")]
ranges = [range.split("-") for range in ranges]
ranges = [range(int(start), int(end) + 1) for start, end in ranges]
ids = [int(id) for id in ids]

for id in ids:
    for range in ranges:
        if id in range:
            answer += 1
            break

print(answer)