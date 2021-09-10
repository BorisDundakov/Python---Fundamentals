import re

pattern = r">>(?P<furniture>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)"
line = input()
furniture_names = []
total_money = 0

while line != "Purchase":
    match = re.match(pattern, line)
    if match:
        data = match.groupdict() # make it as a dict
        furniture_names.append(data['furniture']) # append info from the dict called data with key 'furniture'
        total_money += int(data['quantity']) * float (data['price'])
    line = input()


print("Bought furniture:")
if furniture_names:
    print("\n".join(furniture_names))
print(f"Total money spend: {total_money :.2f}")