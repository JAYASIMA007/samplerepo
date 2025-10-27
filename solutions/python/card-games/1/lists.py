# 1. Return the current round and the next two rounds
def get_rounds(round_number):
    return [round_number, round_number + 1, round_number + 2]


# 2. Combine two lists of rounds
def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2


# 3. Check if a round number is in the list
def list_contains_round(rounds, round_number):
    return round_number in rounds


# 4. Return the average of the cards in a hand
def card_average(hand):
    return sum(hand) / len(hand)


# 5. Check if approximate averages match the real average
def approx_average_is_average(hand):
    actual_avg = card_average(hand)
    avg_first_last = (hand[0] + hand[-1]) / 2
    median = hand[len(hand) // 2]
    return actual_avg in (avg_first_last, median)


# 6. Compare averages of even and odd indexes
def average_even_is_average_odd(hand):
    even_cards = hand[::2]  
    odd_cards = hand[1::2]  
    return card_average(even_cards) == card_average(odd_cards)


# 7. Double the last card if it’s a Jack (value 11)
def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] = 22
    return hand

