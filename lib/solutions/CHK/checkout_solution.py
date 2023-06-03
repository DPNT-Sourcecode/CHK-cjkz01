

# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter
def checkout(skus):
    # raise NotImplementedError()
    product = {
        'A': {'1': 50, 'bonus':3,'amount': 130},
        'B': {'1': 30, 'bonus':2, 'amount': 45},
        'C': {'1': 20},
        'D': {'1': 15},
    }

    total = 0
    counters = Counter(skus)
    for key, val in counters.items():
        if key in product:
            if 'bonus' in product[key] and val >= product[key]['bonus']:
                div = int(val / product[key]['bonus'])
                rem = val % product[key]['bonus']
                total += (product[key]['amount'] * div) + (product[key]['1'] * rem)

            else:
                total += val * product[key]['1']

        else:
            return -1

    return total






