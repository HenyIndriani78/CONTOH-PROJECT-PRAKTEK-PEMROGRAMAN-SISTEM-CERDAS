def force(fruits, value_limit: int):
    if len(fruits) == 0:
        return 0, []

    max_weight = 0
    max_weight_packed = []
    for i, fruit in enumerate(fruits):
        if fruit.value > value_limit:
            continue

        weight, packed = force(fruits[i + 1:], value_limit - fruit.value)
        if weight + fruit.weight >= max_weight:
            max_weight = weight + fruit.weight
            max_weight_packed = [fruit] + packed

    return max_weight, max_weight_packed