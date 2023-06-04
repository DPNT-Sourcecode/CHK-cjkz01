

# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter
def checkout(skus):
    # raise NotImplementedError()
    product = {
        'A': {-1: 50, 3:130,5: 200, 'bonus': [5, 3]},
        'B': {-1: 30, 2:45},
        'C': {-1: 20},
        'D': {-1: 15},
        'E': {-1: 40, 2:'B', 'free_bonus': [2]},
    }

    total = 0
    counters = Counter(skus)
    for key, val in counters.items():
        if key in product:

            if 'bonus' in product[key]:
                rem = 0
                for bonus in product[key]['bonus']:
                    div = int(val / bonus)
                    total += (product[key][bonus] * div)
                    rem = val % bonus
                    val = rem
                total += (product[key][-1] * rem)

                for bonus in product[key]['free_bonus']:
                    total += product[product[key][bonus]][-1]

            else:
                total += val * product[key][-1]

        else:
            return -1

    return total





