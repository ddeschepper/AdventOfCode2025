from pathlib import Path

input = (Path(__file__).parent / 'input.txt').read_text()

position = 50
zero_count = 0

def turn(direction, count):
    global position, zero_count

    if direction == "L":
        position = (position - count) % 100
    else:
        position = (position + count) % 100
    
    if position == 0:
        zero_count += 1

for line in input.splitlines():
    dir = line[0]
    cnt = int(line[1:])
    turn(dir, cnt)

print(f'Zero count: {zero_count}')