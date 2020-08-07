import argparse
from von_neumann import *


class Main:
	def __init__(self):
		parser = argparse.ArgumentParser(
			description='Calculate how long a self-replicating probe could colonize the whole galaxy.')
		parser.add_argument(
			'--probes',
			type=int,
			default=1,
			help='How many initial probes to send out. Default is 1.')
		parser.add_argument(
			'--lightspeed',
			type=float,
			default=.9,
			help='Fraction of the speed of light the probes will travel (in decimal format). Default of .9.')
		parser.add_argument(
			'--stars',
			type=int,
			default=100000000000,
			help='How many star systems the galaxy should have. Default is 100 billion.')
		args = parser.parse_args()

		von = VonNeumann(args.probes, args.lightspeed, args.stars)
		num = NumberFormatter()
		big_num = num.as_big_num(von.complete_coloization())

		print("It would take " + big_num + " years to colonize the whole galaxy")


if __name__ == "__main__":
	Main()
