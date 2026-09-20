import math
import random
from pathlib import Path


class GenerateTSPData:
	"""Generate deterministic random coordinates and distances for a TSP instance."""

	def __init__(self, number_of_cities: int):
		if isinstance(number_of_cities, bool) or not isinstance(number_of_cities, int):
			raise TypeError("number_of_cities must be an integer")
		if number_of_cities < 0:
			raise ValueError("number_of_cities must be non-negative")

		self.number_of_cities = number_of_cities
		self.coordinates = {}

	def generate_names(self):
		"""Generate names from city 1 through city N."""
		return [f"city {city_number}" for city_number in range(1, self.number_of_cities + 1)]

	def generate_coordinates(self):
		"""Generate integer coordinates in the inclusive range [0, number_of_cities]."""
		random_generator = random.Random(self.number_of_cities)
		coordinate_range = range(self.number_of_cities + 1)
		self.coordinates = {
			city_name: (
				random_generator.choice(coordinate_range),
				random_generator.choice(coordinate_range),
			)
			for city_name in self.generate_names()
		}
		return self.coordinates

	def calculate_distances(self):
		"""Return distances as {(city_a, city_b): distance} entries."""
		if len(self.coordinates) != self.number_of_cities:
			self.generate_coordinates()

		distances = {}
		for city_a, (first_x, first_y) in self.coordinates.items():
			for city_b, (second_x, second_y) in self.coordinates.items():
				distances[(city_a, city_b)] = math.ceil(
					math.hypot(first_x - second_x, first_y - second_y)
				)

		return distances
mincitiesdata=5
maxcitiesdata=9
for instance_number, number_of_cities in enumerate(range(mincitiesdata, maxcitiesdata + 1), start=1):
	generator = GenerateTSPData(number_of_cities)
	coordinates = generator.generate_coordinates()
	distances = generator.calculate_distances()
	file_path = Path(__file__).resolve().parent / f"instances{instance_number:02d}.txt"

	with open(file_path, "w", encoding="utf-8") as instance_file:
		instance_file.write(f"number_of_cities = {number_of_cities}\n")
		instance_file.write(f"coordinates = {coordinates!r}\n")
		instance_file.write(f"distances = {distances!r}\n")
