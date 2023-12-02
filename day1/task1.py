with open("input.txt", "r") as f:
  lines = f.readlines()

total = 0
for line in lines:
    nums = []
    for char in line:
        try:
            n = int(char)
            nums.append(n)
        except Exception:
            pass

    d1 = nums[0]
    d2 = nums[-1]
    total += (d1 * 10) + d2

print(total)