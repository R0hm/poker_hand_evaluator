# Poker two plus two hand evaluator and a small Monte Carlo simulation function

This is a partial translation of the excellent javascript hand evaluator by chenosaurus (https://github.com/chenosaurus/poker-evaluator) to python. 

The idea behind the hand evaluator is as follows: each hand's value is a number. This number is encoded in a huge binary lookup table. To get to the value for the hand, this lookup table has to be traversed using each card from the hand. As can be seen from lib/poker_hand_evaluator.py, the script is just a couple of dicts and one small function. All the magic is in the lookup table.

The Monte Carlo function simulates the full round a number of times, and reports the win probability.

## Usage:
```
from lib.poker_hand_evaluator import handStats
from lib.monte_carlo import win_prob

print(handStats(['as', 'ac', 'ad', '5d', '5s']))
# {'handType': 7, 'handRank': 148, 'value': 28820, 'handName': 'full house'}

h_cards = ['as', 'ac']
c_cards = ['ad', '5d', '5s']
print("Win% for this hand: {:.2f}".format(win_prob(simulations=1000,
                                                opponents=5,
                                                h_cards=h_cards,
                                                c_cards=c_cards) * 100))
# Win% for this hand: 97.20
```

