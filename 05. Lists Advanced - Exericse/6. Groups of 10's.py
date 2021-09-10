nums = input().split(", ")
list_10 = []
list_20 = []
list_30 = []
list_40 = []
list_50 = []

for index in range(len(nums)):
    if len(nums[index]) == 1:
        list_10.append(int(nums[index]))
    if 9 < int(nums[index]) < 21:
        list_20.append(int(nums[index]))
    if 19 < int(nums[index]) < 31:
        list_30.append(int(nums[index]))
    if 29 < int(nums[index]) < 41:
        list_40.append(int(nums[index]))
    if 39 < int(nums[index]) < 51:
        list_50.append(int(nums[index]))

print(f"Group of 10's: {list_10}")
print(f"Group of 20's: {list_20}")
print(f"Group of 30's: {list_30}")
print(f"Group of 40's: {list_40}")
print(f"Group of 50's: {list_50}")
