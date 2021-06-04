budget = float(input())
price_flour_per_kg = float(input())
money_remaining = budget
counter_easters = 0
counter_eggs = 0
# one Easter bread -> 1 pack eggs; 1 kg flour; 0.250 l milk
price_pack_eggs = 0.75 * price_flour_per_kg
price_liter_milk = 1.25 * price_flour_per_kg
price_one_easter_milk = price_liter_milk / 4
price_one_easter = price_one_easter_milk + price_flour_per_kg + price_pack_eggs

while money_remaining > price_one_easter:
    counter_easters += 1
    money_remaining -= price_one_easter
    counter_eggs += 3

    if counter_easters % 3 == 0:
        counter_eggs -= counter_easters - 2

    if money_remaining < price_one_easter:
        break

print(f"You made {counter_easters} cozonacs! Now you have {counter_eggs} eggs and {money_remaining :.2f}BGN left.")
