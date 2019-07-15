from collections import Counter


def men_still_standing(cards):
    # your code
    team_a_red = []
    team_b_red = []
    team_a_yellow = []
    team_b_yellow = []

    def yellow_to_red(yellow_cards):
        """Count 2 yellow cards as one red"""
        counter = Counter(yellow_cards)
        red_cards = 0
        for yellow_card in counter:
            if counter[yellow_card] > 1:
                red_cards = red_cards + 1
        return red_cards

    def count_red_cards(red_card_list, yellow_card_list):
        "counts both red and yellow cards"
        unique_red_cards = set(red_card_list)
        no_players = 11 - (len(unique_red_cards)+yellow_to_red(yellow_card_list))
        return no_players

    for card in cards:
        if 'A' in card:
            if card[-1] == 'R':
                team_a_red.append(card)
            else:
                team_a_yellow.append(card)
        else:
            if card[-1] == 'R':
                team_b_red.append(card)
            else:
                team_b_yellow.append(card)

    team_a_players = count_red_cards(team_a_red, team_a_yellow)
    team_b_players = count_red_cards(team_b_red, team_b_yellow)
    print(f"{team_a_players} , {team_b_players}")
men_still_standing(["A4R", "A6R", "A8R", "A10R", "A11R"])

# to do
"""
what if a player gets a red card
followed by a yellow card..
"""
