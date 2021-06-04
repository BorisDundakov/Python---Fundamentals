n_rooms = int(input())
free_chairs = 0
chairs_remaining = 0
Game_On = True

for room_number in range(1, n_rooms + 1):

    chairs_available, chairs_needed = input().split()
    difference = abs(len(chairs_available) - int(chairs_needed))

    if len(chairs_available) < int(chairs_needed):

        print(f"{difference} more chairs needed in room {room_number}")
        Game_On = False
    else:
        free_chairs += difference

if Game_On:
    print(f"Game On, {free_chairs} free chairs left")
