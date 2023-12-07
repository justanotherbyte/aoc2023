from enum import IntEnum


with open("input.txt", "r") as f:
    lines = f.readlines()

labels = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

class CardStrength(IntEnum):
    FiveOfAKind     = 6
    FourOfAKind     = 5
    FullHouse       = 4
    ThreeOfAKind    = 3
    TwoPair         = 2
    OnePair         = 1
    HighCard        = 0

def calc_card_strength(card: str) -> CardStrength:
    components: dict[str, int] = {}
    for char in card:
        if char not in components:
            components[char] = 1
        else:
            components[char] += 1

    # five of a kind
    if len(components) == 1:
        return CardStrength.FiveOfAKind
    
    # four of a kind
    if 4 in components.values():
        return CardStrength.FourOfAKind
    
    if 3 in components.values() and len(components) == 2:
        return CardStrength.FullHouse
    
    if 3 in components.values() and len(components) == 3:
        return CardStrength.ThreeOfAKind
    
    if 2 in components.values() and len(components) == 3:
        return CardStrength.TwoPair
    
    if 2 in components.values() and len(components) == 4:
        return CardStrength.OnePair
        
    return CardStrength.HighCard

class Card:
    def __init__(self, value: str, bid: int):
        self.value = value
        self.bid = bid

        self.strength = calc_card_strength(value)

    def __lt__(self, other: "Card") -> bool:
        if self.strength != other.strength:
            return self.strength < other.strength
        
        for idx, char in enumerate(self.value):
            corr_char = other.value[idx]
            this_label_idx = labels.index(char)
            other_label_idx = labels.index(corr_char)

            if this_label_idx == other_label_idx:
                continue

            if this_label_idx < other_label_idx:
                return True
            else:
                return False
            
        return False
    
cards = []
for line in lines:
    value, num = line.split(" ")
    num = int(num)
    card = Card(value, num)
    cards.append(card)

sorted_cards = sorted(cards)
winnings = []

for rank, card in enumerate(sorted_cards, start=1):
    winning = card.bid * rank
    winnings.append(winning)

print(sum(winnings))
