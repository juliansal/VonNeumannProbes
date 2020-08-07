
class VonNeumann:
	def __init__(self, probe_count, percent_light_speed, galaxy_star_total):
		self.probe_count = probe_count
		self.percent_light_speed = percent_light_speed
		self.galaxy_star_total = galaxy_star_total

	def multiply_probe(self, probes):
		if probes < 1:
			probes = 1
		else:
			probes = probes * 2

		return probes

	def cycle_thru(self):
		generations = 0
		worlds_seeded = 1
		while worlds_seeded < self.galaxy_star_total:
			generations = generations + 1
			self.probe_count = self.multiply_probe(self.probe_count)
			worlds_seeded = self.probe_count * 2 - 1

		return generations

	def complete_coloization(self):
		return self.cycle_thru() * self.travel_time() * self.teraforming_time()

	def travel_time(self):
		to_reciprocal_c = 1 / self.percent_light_speed
		galaxy_length = 100000
		return galaxy_length * to_reciprocal_c

	def teraforming_time(self):
		return 1000


class NumberFormatter:
	def as_big_num(self, num):
		return '{:,.0f}'.format(num)
