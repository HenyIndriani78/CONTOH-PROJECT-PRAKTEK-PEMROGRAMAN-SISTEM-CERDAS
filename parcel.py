from collections import namedtuple
import genetic as Genome

Fruit = namedtuple('Fruit', ['name', 'value', 'weight'])

fruit_list = [
    Fruit('Pisang', 30000, 940),
    Fruit('Anggur', 35000, 500),
    Fruit('Jeruk', 4500, 100),
    Fruit('Pir', 6000, 150),
    Fruit('Apel', 5000, 120),
    Fruit('Buah Naga', 12000, 350),
    Fruit('Alpukat', 8000, 200),
    Fruit('Jambu', 4000, 100),
    Fruit('Kelengkeng', 25000, 500),
    Fruit('Nanas', 10000, 400)
]

def generate_fruit(num: int) -> [Fruit]:
    return [Fruit(f"fruit{i}", i, i) for i in range(1, num+1)]

def fitness(genome: Genome, fruits: [Fruit], value_limit: int) -> int:
    if len(genome) != len(fruits):
        raise ValueError("genome and fruits must be of same length")

    weight = 0
    value = 0
    for i, fruit in enumerate(fruits):
        if genome[i] == 1:
            weight += fruit.weight
            value += fruit.value

            if value > value_limit:
                return 0

    return weight


def from_genome(genome: Genome, fruits: [Fruit]) -> [Fruit]:
    result = []
    for i, fruit in enumerate(fruits):
        if genome[i] == 1:
            result += [fruit]

    return result


def to_string(fruits: [Fruit]):
    return f"[{', '.join([t.name for t in fruits])}]"


def value(fruits: [Fruit]):
    return sum([t.value for t in fruits])


def weight(fruits: [Fruit]):
    return sum([p.weight for p in fruits])


def print_stats(fruits: [Fruit]):
    print(f"fruits: {to_string(fruits)}")
    print(f"Value {value(fruits)}")
    print(f"Weight: {weight(fruits)}")