n_players_A = 11
n_players_B = 11
is_Stopped = False
red_card_index = 0
input_cards = input().split(" ")
red_carded_A_players = []
red_carded_B_players = []

for red_card_index in range(len(input_cards)):

    if "A-" in (input_cards[red_card_index]):
        if (input_cards[red_card_index]) in red_carded_A_players:
            continue
        else:
            red_carded_A_players.append(input_cards[red_card_index])
            n_players_A -= 1

    elif "B-" in (input_cards[red_card_index]):
        if (input_cards[red_card_index]) not in red_carded_B_players:
            red_carded_B_players.append(input_cards[red_card_index])
            n_players_B -= 1

    if 7 > n_players_A or 7 > n_players_B:
        is_Stopped = True
        break


if is_Stopped:
    print(f"Team A - {n_players_A}; Team B - {n_players_B}")
    print("Game was terminated")

else:
    print(f"Team A - {n_players_A}; Team B - {n_players_B}")

