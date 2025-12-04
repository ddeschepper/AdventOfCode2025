from math import floor
from pathlib import Path

input = (Path(__file__).parent / 'input.txt').read_text()

position = 50
zero_count = 0

def turn(direction, count):
    global position, zero_count

    if direction == "L":
        zero_count += floor(abs(count + ((100 - position) % 100)) / 100)
        position = (position - count) % 100
    else:
        zero_count += floor(abs(count + position) / 100)
        position = (position + count) % 100

for line in input.splitlines():
    dir = line[0]
    cnt = int(line[1:])
    turn(dir, cnt)

print(f'Zero count: {zero_count}')