from pathlib import Path

input = (Path(__file__).parent / 'input.txt').read_text()

ranges, _ = [part.splitlines() for part in input.split("\n\n")]
ranges = [range.split("-") for range in ranges]

# remove duplicate ranges
ranges = set([(int(start), int(end)) for start, end in ranges])

# remove fully overlapping ranges
redundant_range_indexes = []
for i, (start, end) in enumerate(ranges):
    for j, (start_other, end_other) in enumerate(ranges):
        if j == i:
            continue
        if start >= start_other and end <= end_other:
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
    start_updated = start
    updated_start = end
    for j, (start_other, end_other) in enumerate(ranges):
        if j == i:
            continue
        if end_other >= updated_start >= start_other:
            updated_start = start_other - 1
        elif start_other <= start_updated <= end_other:
            start_updated = end_other + 1
    
    ranges[i] = (start_updated, updated_start)

answer = sum([
    len(range(start, end + 1))
    for start, end
    in ranges
])

print(answer)