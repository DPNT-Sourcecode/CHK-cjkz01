

# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter
from itertools import combinations




def checkout(skus):
    # raise NotImplementedError()
    product = {
        'A': {-1: 50, 3:130,5: 200, 'bonus': [5, 3]},
        'B': {-1: 30, 2:45, 'bonus': [2]},
        'C': {-1: 20},
        'D': {-1: 15},
        'E': {-1: 40, 2:'B', 'free_bonus': [2]},
        'F': {-1: 10, 2:'F', 'free_bonus': [2]},
        'G': {-1: 20},
        'H': {-1: 10, 5:45,10: 80, 'bonus': [10, 5]},
        'I': {-1: 35},
        'J': {-1: 60},
        'K': {-1: 80, 2:150, 'bonus': [2]},
        'L': {-1: 90},
        'M': {-1: 15},
        'N': {-1: 40, 3:'M', 'free_bonus': [3]},
        'O': {-1: 10},
        'P': {-1: 50, 5: 200, 'bonus': [5]},
        'Q': {-1: 30, 3: 80, 'bonus': [3]},
        'R': {-1: 50, 3: 'Q', 'free_bonus': [3]},
        'S': {-1: 20},
        'T': {-1: 20},
        'U': {-1: 40, 3: 'U', 'free_bonus': [3]},
        'V': {-1: 50, 2: 90, 3:130 ,'bonus': [3,2]},
        'W': {-1: 20},
        'X': {-1: 17},
        'Y': {-1: 20},
        'Z': {-1: 21},

    }



    total = 0
    counters = Counter(skus)


    for comb in combinations("STXYZ", 3):
        if comb in tuple(skus):
            print(True, ''.join(comb), skus )
        else:
            print(False, ''.join(comb), skus)




    for key, val in counters.items():
        if key not in product:
            return -1

        if 'free_bonus' in product[key]:

            for bonus in product[key]['free_bonus']:
                if key == 'F':
                    div = int(val / 3)
                elif key == 'U':
                    div = int(val / 4)
                else:
                    div = int(val / bonus)
                if product[key][bonus] in counters:
                    counters[product[key][bonus]] -= min(div, counters[product[key][bonus]])

    for key, val in counters.items():
        if 'bonus' in product[key]:
            rem = 0
            for bonus in product[key]['bonus']:
                div = int(val / bonus)
                total += (product[key][bonus] * div)
                rem = val % bonus
                val = rem
            total += (product[key][-1] * rem)

        else:
            total += val * product[key][-1]


    return total




checkout("VTXS")

