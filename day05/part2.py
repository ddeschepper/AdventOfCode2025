from pathlib import Path

input = (Path(__file__).parent / 'input.txt').read_text()

ranges, _ = [part.splitlines() for part in input.split("\n\n")]
ranges = [range.split("-") for range in ranges]

# remove duplicate ranges
ranges = set([(int(start), int(end)) for start, end in ranges])

# remove fully overlapping ranges
redundant_range_indexes = []
for i, (start, end) in enumerate(ranges):
    for j, (start_compare, end_compare) in enumerate(ranges):
        if j == i:
            continue
        if start >= start_compare and end <= end_compare:
            redundant_range_indexes.append(i)
            break

ranges = [
    range
    for i, range
    in enumerate(ranges)
    if i not in redundant_range_indexes
]

# remove overlap from remaining ranges
for i, (start, end) in enumerate(ranges):
    new_start = start
    new_end = end
    for j, (start_compare, end_compare) in enumerate(ranges):
        if j == i:
            continue
        if end_compare >= new_end >= start_compare:
            new_end = start_compare - 1
        elif start_compare <= new_start <= end_compare:
            new_start = end_compare + 1
    
    ranges[i] = (new_start, new_end)

answer = sum([
    len(range(start, end + 1))
    for start, end
    in ranges
])

print(answer)