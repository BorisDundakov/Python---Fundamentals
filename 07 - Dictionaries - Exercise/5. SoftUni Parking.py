username_license_dict = {}

n = int(input())

for el in range(n):
    command = input().split()
    type_command = command[0]
    username = command[1]

    if type_command == "register":
        license_plate = command[2]
        if username not in username_license_dict:
            username_license_dict[username] = license_plate

            print(f"{username} registered {license_plate} successfully")

        else:
            print(f"ERROR: already registered with plate number {license_plate}")


    elif type_command == "unregister":
        if username not in username_license_dict:
            print(f"ERROR: user {username} not found")
        else:
            username_license_dict.pop(username)
            print(f"{username} unregistered successfully")

for key, value in username_license_dict.items():
       print(f"{key} => {value}")