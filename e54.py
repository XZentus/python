rank = dict()

for i in range(1, 10):
    rank[str(i)] = i
    
for val, r in enumerate('TJQKA', 10):
    rank[r] = val

rank_trans = ' 123456789TJQKA'

def is_same_suit(cards):
    return all(c[1] == cards[0][1] for c in cards)

def Royal_Flush(cards):
    if not is_same_suit(cards):
        return False, cards

    values = [c[0] for c in cards]
    values.sort()
    if ''.join(values) == 'AJKQT':
        return True, []
    
    return False, cards
    
    
def Straight_Flush(cards):
    if not is_same_suit(cards):
        return False, cards

    values = [c[0] for c in cards]
    values.sort(key=lambda x: rank[x])
    if ''.join(values) in rank_trans:
        return True, []
    
    return False, cards
    
def Four_of_a_Kind(cards):
    cards.sort(key=lambda c: rank[c[0]])
    
    ranks = [rank[c[0]] for c in cards]
    
    if ranks.count(ranks[0]) == 4:
        return ranks[0], [c for c in cards if c[0] != rank_trans[ranks[0]]]
    elif ranks.count(ranks[1]) == 4:
        return ranks[1], [c for c in cards if c[0] != rank_trans[ranks[1]]]
    
    return False, cards

def Three_of_a_Kind(cards):
    cards.sort(key=lambda c: rank[c[0]])
    
    ranks = [rank[c[0]] for c in cards]
    
    if ranks.count(ranks[0]) == 3:
        return ranks[0], [c for c in cards if c[0] != rank_trans[ranks[0]]]
    elif ranks.count(ranks[1]) == 3:
        return ranks[1], [c for c in cards if c[0] != rank_trans[ranks[1]]]
    elif ranks.count(ranks[2]) == 3:
        return ranks[2], [c for c in cards if c[0] != rank_trans[ranks[2]]]
    
    return False, cards

def One_Pair(cards):
    cards.sort(key=lambda c: rank[c[0]])
    
    ranks = [rank[c[0]] for c in cards]
    
    for r in ranks:
        if ranks.count(r) == 2:
            return r, [c for c in cards if c[0] != rank_trans[r]]
    
    return False, cards

def Full_House(cards):
    res1, rest1 = Three_of_a_Kind(cards)
    if res1:
        res2, rest2 = One_Pair(rest1)
        if res2:
            return max(res1, res2), rest2
    return False, cards

def Flush(cards):
    if not is_same_suit(cards):
        return False, cards
    return True, []

def Straight(cards):
    values = [c[0] for c in cards]
    values.sort(key=lambda x: rank[x])

    if ''.join(values) in rank_trans:
        return True, []
    
    return False, cards

def Two_Pairs(cards):
    res1, rest1 = One_Pair(cards)
    if res1:
        res2, rest2 = One_Pair(rest1)
        if res2:
            return max(res1, res2), rest2
    return False, cards

def High_Card(cards):
    cards.sort(key=lambda c: rank[c[0]])
    
    return cards[-1], cards[0:-1]

def apply_highest(cards1, cards2):
    rest1 = cards1
    rest2 = cards2
    
    while rest1 and rest2:
        c1, rest1 = High_Card(rest1)
        c2, rest2 = High_Card(rest2)
        if c1[0] != c2[0]:
            if rank[c1[0]] > rank[c2[0]]:
                return 1
            else:
                return 2

    raise Exception('DRAW: {} {}'.format(cards1, cards2))

def apply_rules(cards1, cards2):
    rules_order = [Royal_Flush, Straight_Flush, Four_of_a_Kind, Full_House, Flush,
                   Straight, Three_of_a_Kind, Two_Pairs, One_Pair]
    
    for f in rules_order:
        res1, rest1 = f(cards1)
        res2, rest2 = f(cards2)
        if res1 > res2:
            return 1
        elif res2 > res1:
            return 2
        
        if res1 and res2:
            return apply_highest(rest1, rest2)
    return apply_highest(cards1, cards2)

def check_pair(inp):
    cards = inp.split()
    return apply_rules(cards[:5], cards[5:])


def solve():
    wins1 = 0;
    with open('p054_poker.txt', 'r') as inp:
        for line in inp:
            if check_pair(line) == 1:
                wins1 += 1
    return wins1