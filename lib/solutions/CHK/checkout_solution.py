

# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter
def checkout(skus):
    # raise NotImplementedError()
    product = {
        'A': {-1: 50, 3:130},
        'B': {-1: 30, 2:45},
        'C': {-1: 20},
        'D': {-1: 15},
    }

    total = 0
    counters = Counter(skus)
    for key, val in counters.items():
        if key.upper() in product:
            if val in product[key.upper()]:
                total += product[key.upper()][val]

            else:
                total += val * product[key.upper()][-1]

        else:
            return -1

    return total



