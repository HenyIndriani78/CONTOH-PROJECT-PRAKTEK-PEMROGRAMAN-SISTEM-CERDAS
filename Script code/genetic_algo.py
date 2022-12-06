from functools import partial
from utils.analyze import timer
import parcel
import genetic
import bruteforce

fruits = parcel.fruit_list

value_limit = int(input("Maximum Price = "))

with timer():
	result = bruteforce.force(fruits, value_limit)

print("")
print("GENETIC ALGORITHM")
print("----------")

with timer():
	population, generations = genetic.run_evolution(
		populate_func=partial(genetic.generate_population, size=10, genome_length=len(fruits)),
		fitness_func=partial(parcel.fitness, fruits=fruits, value_limit=value_limit),
		fitness_limit=result[0],
		generation_limit=100
	)

box = parcel.from_genome(population[0], fruits)
parcel.print_stats(box)
