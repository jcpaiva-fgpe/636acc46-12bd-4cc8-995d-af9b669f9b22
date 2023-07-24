card_strength = "A K Q J 10 9 8 7 6 5 4 3 2"

def card_compare(card1, card2):
    i1, i2 = card_strength.find(card1), card_strength.find(card2)
    if i1 < i2: return 1
    if i1 > i2: return 2
    return 0

print (card_compare("7", "A"))
print (card_compare("Q", "9"))
print (card_compare("10", "10"))
