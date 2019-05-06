from lib.poker_hand_evaluator import handStats
from lib.monte_carlo import win_prob
import sys

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Provide a valid hand, like '3s 2c 6d 5d ts'")
		exit(1)
	c = sys.argv[1].lower().split()
	if len(c) < 2:
		print("Provide a valid hand, like '3s 2c 6d 5d ts'")
		exit(1)

	print("Hand: {}".format(c))
	print("Stats: {}".format(handStats(c)))
	h_cards = c[:2]
	c_cards = c[2:]
	print("Win% for this hand: {:.2f}".format(win_prob(simulations=1000,
													opponents=5,
													h_cards=h_cards,
													c_cards=c_cards) * 100))