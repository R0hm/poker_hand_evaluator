'''
A library to generate Monte Carlo simulations using a given hand and return win percentage
'''

from lib.poker_hand_evaluator import CARDS, handStats
import random

def win_prob(h_cards=['as', 'ac'], c_cards=[], simulations=1000, opponents=5):
    '''
    Takes details about the table, runs Monte Carlo simulation,
    and returns the win probability for the given hand under the given conditions

    Takes:
    h_cards: hole cards e.g., ['3s', '2c']
    c_cards: community cards e.g., [] or ['6d', '5d', 'ts']
    simulations: number of  simulaltions to make
    opponents: number of other players left in the round

    Returns:
    probability of win [0.0 - 1.0]
    '''
    # make a list of cards available for simulations
    used_cards = h_cards + c_cards
    unused_cards = [i for i in CARDS if i not in used_cards]

    # simulate community_cards "simulations" times
    c_cards_sim = [c_cards + random.sample(unused_cards, 
                    (7 - len(used_cards))) \
                    for _ in range(simulations)]

    # simulate hole_cards for each opponent for each community card set
    others_hand = []
    others_hand = [_make_opponents_hole_cards(each_com_cards + h_cards, opponents) \
        for each_com_cards in c_cards_sim]

    # record win if handStats['value'] for hero's hand is the higher than everyone else
    win = []
    for idx in range(len(c_cards_sim)):
         win.append(_did_hand_win(c_cards_sim[idx], h_cards, others_hand[idx]))
    return float(sum(win))/len(c_cards_sim)

def _did_hand_win(c, h, o):
    return handStats(c+h)['value'] > max([handStats(i+c)['value'] for i in o])

def _make_opponents_hole_cards(my_hand, opponents):
    unused_cards = [i for i in CARDS if i not in my_hand]
    random.shuffle(unused_cards)
    return [unused_cards[i:i+2] for i in range(0, opponents * 2, 2)]
        
