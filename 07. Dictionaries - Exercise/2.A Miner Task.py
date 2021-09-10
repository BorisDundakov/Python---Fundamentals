command = input()
dictionary = {}
while command != "stop":
    if command not in dictionary:
        quantity = int(input())
        dictionary[command] = quantity
        # dictionary with the name dictionary
        # key with the name command
        # value with the name quantity
        #adding key command with value quantity to the dictionary

        command = input()
        continue
    quantity = int(input())
    dictionary[command] += quantity
    # since the key is already present, we increase the value by the new input
    command = input()


for (key, value) in dictionary.items():
    print(f"{key} -> {value}")
