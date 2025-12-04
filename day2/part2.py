import re
from pathlib import Path

input = (Path(__file__).parent / 'input.txt').read_text()

answer = 0

for r in input.split(","):
    start, end = r.split("-")
    for n in range(int(start), int(end) + 1):
        if re.fullmatch(r"^(\d+?)(\1)+$", str(n)):
            answer += n 

print(answer)