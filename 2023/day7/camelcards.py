"""
Strategy:
1.  Group hands into hand 'buckets': 5 of a kind, full house etc.
    This is done by counting the unique occurences of each card.
2.  Sort the hands in each bucket by increasing order of strength
3.  Iterate over the buckets and hands starting at rank 1 and incrementing rank with each hand

Part 2:
Count the jokers seperatley and add to the max count
e.g. 77AJ3: 2 (sevens) + 1 (Joker) => 3 (of a kind)

Note: It is always optimal to make all of the jokers the same value
Proof:

ABCJJ: Best same = 3 of a kind; best different = 2 pair
AABJJ: Best same = 4 of a kind; best different = full house
AAAJJ: Best same = 5 of a kind; best different = 4 of a kind

ABJJJ: Best same = 4 of a kind; best different (2 same) = full house; (0 same) = 2 pair
AAJJJ: Best same = 5 of a kind (best hand)
AJJJJ: Best same = 5 of a kind (best hand)

JJJJJ: Obviously

In all cases using the same value for the joker results in the optimal hand

Therefore we can just add the number of jokers there are to the highest count to represent
the best new hand
"""

hands = {}
buckets = {
    '5kind': [],
    '4kind': [],
    'house': [],
    '3kind': [],
    '2pair': [],
    '1pair': [],
    'high': []
}

card_strength = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 0,
    'Q': 12,
    'K': 13,
    'A': 14
}

def place_in_bucket(hand):
    counts = [hand.count(c) for c in set(hand) if c != 'J']

    # Part 2
    joker_count = hand.count('J')
    if len(counts) != 0:
        cmax = max(counts)
        counts.remove(cmax)
        counts.append(cmax + joker_count)
    else:
        counts = [5]
    
    key = 'high'
    if 5 in counts:
        key = '5kind'
    elif 4 in counts:
        key = '4kind'
    elif 3 in counts and 2 in counts:
        key = 'house'
    elif 3 in counts:
        key = '3kind'
    elif counts.count(2) == 2:
        key = '2pair'
    elif 2 in counts:
        key = '1pair'
    
    buckets[key].append(hand)

def compare_hands(hand_a, hand_b):
    for i in range(len(hand_a)):
        if card_strength[hand_a[i]] > card_strength[hand_b[i]]:
            return True
        elif card_strength[hand_a[i]] < card_strength[hand_b[i]]:
            return False
    
    return False

def sort_hands(h):
    """ Sort a list of cards in same group """
    for _ in range(len(h)):
        for i in range(len(h) - 1):
            swap = compare_hands(h[i], h[i+1])
            if swap:
                temp = h[i]
                h[i] = h[i+1]
                h[i+1] = temp
    return h

with open('in.txt') as f:
    for line in f.readlines():
        hand, bid = line.split(' ')
        hands[hand] = int(bid)
    
    for hand, bid in hands.items():
        place_in_bucket(hand)
    
    for bucket, h in buckets.items():
        buckets[bucket] = sort_hands(h)
        
    rank = 1
    winnings = 0
    for bucket, hlist in reversed(buckets.items()):
        for hand in hlist:
            winnings += rank * hands[hand]
            rank += 1
    
    print(winnings)