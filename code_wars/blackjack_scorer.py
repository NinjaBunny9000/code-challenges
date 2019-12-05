def score_hand(cards):
    score = 0
    aces = 0
    face_cards = 'JKQ'

    print(cards)
   
    for card in cards:
        try:
            # cast as an int
            score += int(card)
        except:        
            if card in face_cards:
                score += 10
            elif card == 'A':
                aces += 1

    score += aces

    while aces:
        if score - 1 + 11 <= 21:
            score += 10
        aces -= 1
    
    return score

print(score_hand(['A', 'A', 'A', 'J'])) # 13
print(score_hand(['A', '3'])) # 14
print(score_hand(['A', 'J'])) # 21
# print(score_hand(['2', '3'])) # 5
# print(score_hand(['7', '7', '8'])) # 22
# print(score_hand(['4', '7', '8'])) # 19
# print(score_hand(['K', 'Q','J'])) # 30
# print(score_hand(['A', '3'])) # 14
# print(score_hand(['A', 'A'])) # 12 
# print(score_hand(['A', '2', 'A', '9', '9'])) # 22

