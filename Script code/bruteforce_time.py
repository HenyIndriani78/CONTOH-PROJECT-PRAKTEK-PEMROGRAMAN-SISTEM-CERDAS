import parcel
import bruteforce

import time

value_limit = 40000

for i in range(31):
    fruits = parcel.generate_fruit(i)
    start = time.time()
    bruteforce.force(fruits, value_limit)
    end = time.time()

    print(f"{i}\t|\t{end-start}s")
