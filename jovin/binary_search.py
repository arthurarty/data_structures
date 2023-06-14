from typing import List


# Given cards, and a card to find, we find the index of desired_card
# input formats: cards: list, desired_card is an int
# output format: index of the desired card if found in the list
# return -1 if not found in cards


def locate_card(cards: List[int], desired_card: int) -> int:
    # we are going to use a binary search
    # this is possible because the list is sorted
    # this involves splitting the list into 2 at a midway point
    # and then picking one half of the list to concentrate on basing on whether it 
    # greater than or less than the desired card
    # we keep splitting till we have one element left
    # we need to keep track of low and high index.
    # when decide to pick a half of the list, we adjust the low and the high.
    low, high = 0, len(cards) - 1
    while low <= high:
        # if low == high, we have finished the entire list
        # if list is empty, 0 is greater than -1 so condition exists
        midpoint = (low + high) // 2
        if desired_card == cards[midpoint]:
            return midpoint
        elif desired_card < cards[midpoint]:
            high = midpoint - 1
        elif desired_card > cards[midpoint]:
            low = midpoint + 1
    return -1


test_cases = [
    {
        "func_input": {
            "cards": [],
            "desired_card": 4,
        },
        "func_output": -1
    },
    {
        "func_input": {
            "cards": [5, 9, 12, 14],
            "desired_card": 9,
        },
        "func_output": 1
    },
]


for test_case in test_cases:
    output = locate_card(**test_case['func_input'])
    assert output == test_case['func_output']
