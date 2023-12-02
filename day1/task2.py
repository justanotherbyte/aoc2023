with open("input.txt", "r") as f:
  lines = f.readlines()

spelled = {
  "one": 1,
  "two": 2,
  "six": 6,
  "four": 4,
  "five": 5,
  "nine": 9,
  "three": 3,
  "seven": 7,
  "eight": 8,
}

total = 0
for line in lines:
  nums = []
  for idx, char in enumerate(line):
    try:
      num = int(char)
      nums.append(num)
    except Exception:
      pass


    for (key, _) in spelled.items():
      if key.startswith(char):
        word = line[idx: idx + len(key)]
        t = spelled.get(word)
        if t:
          nums.append(t)


  d1 = nums[0]
  d2 = nums[-1]
  total += (d1 * 10) + (d2)

print(total)