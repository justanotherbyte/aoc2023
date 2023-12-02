import sys
import os

import requests

with open(".session", "r") as f:
    session = f.read().strip()

day = sys.argv[1]
url = f"https://adventofcode.com/2023/day/{day}/input"
cookies = {"session": session}
resp = requests.get(url, cookies=cookies)

resp.raise_for_status()

day_input = resp.content
resp.close()

folder_path = f"day{day}"
os.mkdir(folder_path)
os.chdir(folder_path)

template = '''
with open("input.txt", "r") as f:
    lines = f.readlines()
'''

with open("task1.py", "w") as f:
    f.write(template)

with open("task2.py", "w") as f:
    f.write(template)

with open("input.txt", "wb") as f:
    f.write(day_input)

print(f"Day {day} setup.")