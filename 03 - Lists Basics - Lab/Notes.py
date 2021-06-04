list = [4, 11, "Hello"]
print(list[2])

text = "My name is Slim Shady"

final = text.split()
print(final)

version_2 = " ".join(final)
print(version_2)

nums = [4, 5, 6]
print(nums[-1])

for index in range(len(nums) - 1, -1, -1):
    print(nums[index])

next = [1, 2, 3]
next[2] = 100
print(next)