# -----------------------------------------+
# William Wood                             |
# CSCI 127, Program 2                      |
# -----------------------------------------|
# Simplified Poker Hand evaluation system. |
# -----------------------------------------+

from __future__ import barry_as_FLUFL


def get_all_ranks(hand):
    result = []
    for card in hand:
        result.append(card[0])
    return result

def royal_flush(hand):
    
    suit = False
    rank = False

    royalflush = [10,11,12,13,14]
    ranks = []

    for card in hand:
        ranks.append(card[0])

    if ranks == royalflush:
        rank = True

    for i in range(1,len(hand)):
        if hand[0][1] != hand[i][1]:
            suit = False
            break
        else: suit = True

    if suit and rank:
        return True
    else: return False


def straight_flush(hand):
    consecutive = False
    suit = False

    for i in range(1,len(hand)):
        if hand[i][0] - hand[i-1][0] != 1:
            consecutive = False
            break
        else: consecutive = True
    
    
    for i in range(1,len(hand)):
        if hand[0][1] != hand[i][1]:
            suit = False
            break
        else: suit = True
    
    if consecutive and suit:
        return True
    else: return False

def straight(hand):
    consecutive = False

    for i in range(1,len(hand)):
        if hand[i][0] - hand[i-1][0] != 1:
            consecutive = False
            break
        else: consecutive = True
    
    if consecutive:
        return True
    else: return False

def four_of_a_kind(ranks):
    kind = 0
    
    for rank in ranks:
        if rank == ranks[0]:
            kind += 1

    if kind != 4:
        kind = 0
        for rank in ranks:
            if rank == ranks[1]:
                kind += 1

    if kind == 4:
        return True
    else: return False

def full_house(ranks):
    unique = []

    for rank in ranks:
        if rank not in unique:
            unique.append(rank)

    if len(unique) == 2:
        return True
    else: return False

def three_of_a_kind(ranks):
    unique = []
    combo = []

    for rank in ranks:
        if rank not in unique:
            unique.append(rank)
    
    for i in range(len(ranks)):
        if len(combo) == 3:
            break
        elif len(combo) == 0:
            combo.append(ranks[i])
        else:
            if ranks[i] == combo[0]:
                combo.append(ranks[i])
            else:
                combo.clear()
                combo.append(ranks[i])

        

    if len(unique) == 3 and len(combo) == 3:
        return True
    else: return False

def two_pair(ranks):
    unique = []
    counts = []

    for rank in ranks:
        if rank not in unique:
            unique.append(rank)
    
    for i in range(len(unique)):
        counter = 0
        for j in range(len(ranks)):
            if unique[i] == ranks[j]:
                counter +=1
        counts.append(counter)

    counts.sort()

    if len(unique) == 3 and [1,2,2] == counts:
        return True
    else: return False


def one_pair(ranks):
    unique = []

    for rank in ranks:
        if rank not in unique:
            unique.append(rank)

    if len(unique) == 4:
        return True
    else: return False


# -----------------------------------------+
# Do not modify the evaluate function.     |
# -----------------------------------------+

def evaluate(poker_hand):
    poker_hand.sort()
    poker_hand_ranks = get_all_ranks(poker_hand)
    print(poker_hand, "--> ", end="")
    if royal_flush(poker_hand):
        print("Royal Flush")
    elif straight_flush(poker_hand):
        print("Straight Flush")
    elif four_of_a_kind(poker_hand_ranks):
        print("Four of a Kind")
    elif full_house(poker_hand_ranks):
        print("Full House")
    elif straight(poker_hand):
        print("Straight")
    elif three_of_a_kind(poker_hand_ranks):
        print("Three of a Kind")
    elif two_pair(poker_hand_ranks):
        print("Two Pair")
    elif one_pair(poker_hand_ranks):
        print("One Pair")
    else:
        print("Nothing")
		
# -----------------------------------------+

def main():
    print("CSCI 127: Poker Hand Evaluation Program")
    print("---------------------------------------")
    evaluate([[10, "spades"], [14, "spades"], [12, "spades"], [13, "spades"], [11, "spades"]])  # royal flush
    evaluate([[10, "clubs"], [9, "clubs"], [6, "clubs"], [7, "clubs"], [8, "clubs"]])           # straight flush
    evaluate([[2, "diamonds"], [7, "clubs"], [2, "hearts"], [2, "clubs"], [2, "spades"]])       # 4 of a kind
    evaluate([[8, "diamonds"], [7, "clubs"], [8, "hearts"], [8, "clubs"], [7, "spades"]])       # full house
    evaluate([[13, "diamonds"], [7, "clubs"], [7, "hearts"], [8, "clubs"], [7, "spades"]])      # 3 of a kind
    evaluate([[10, "clubs"], [9, "clubs"], [6, "clubs"], [7, "clubs"], [8, "spades"]])          # straight
    evaluate([[10, "spades"], [9, "clubs"], [6, "diamonds"], [9, "diamonds"], [6, "hearts"]])   # 2 pair
    evaluate([[10, "spades"], [12, "clubs"], [6, "diamonds"], [9, "diamonds"], [12, "hearts"]]) # 1 pair
    evaluate([[2, "spades"], [7, "clubs"], [8, "diamonds"], [13, "diamonds"], [11, "hearts"]])  # nothing
# -----------------------------------------+

main()
