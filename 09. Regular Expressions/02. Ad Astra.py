import re

text = input()

regex = r"(#|\|)\w+( \w+|\w+)\1\d{2}/\d{2}/\d{2}\1(\d{4}|\d{3}|\d{2}|\d{1}|10000)\1"

valid_dates = [obj.group() for obj in re.finditer(regex, text)]

item_nutrition_expire_dict = {}
calorie_sum = []
actual_sum = []
the_sum = 0
counter = 0
for each_entry in valid_dates:
    actual_sum = []
    for each_letter in reversed(each_entry):
        if each_letter.isdigit():
            calorie_sum.append(each_letter)
        continue

    calorie_sum.reverse()

    for each_calorie in calorie_sum:
        counter += 1
        if counter > 6:
            actual_sum.append(each_calorie)
    counter = 0
    calorie_sum.clear()
    actual_sum = "".join(actual_sum)
    the_sum += int(actual_sum)

food_required_for_a_day = 2000
food_available_days = the_sum // food_required_for_a_day

print(f"You have food to last you for: {food_available_days} days!")

for el in valid_dates:
    a = el.split("#")
    b = el.split("|")

    if "#" in el:
        item_nutrition_expire_dict["Item: "] = a[1] + ","
        item_nutrition_expire_dict["Best before: "] = a[2] + ","
        item_nutrition_expire_dict["Nutrition: "] = int(a[3])

        for key, value in item_nutrition_expire_dict.items():
            print(f"{key}{value}", end=" ")

        item_nutrition_expire_dict.clear()
        print()

    else:
        item_nutrition_expire_dict["Item: "] = b[1] + ","
        item_nutrition_expire_dict["Best before: "] = b[2] + ","
        item_nutrition_expire_dict["Nutrition: "] = int(b[3])

        for key, value in item_nutrition_expire_dict.items():
            print(f"{key}{value}", end=" ")
        item_nutrition_expire_dict.clear()
        print()

