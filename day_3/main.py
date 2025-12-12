import itertools
from functools import reduce

COMBO_LENGTH = 12

def get_banks():
    values = open("input.txt")
    values_list = values.read().split('\n')
    return values_list

# def get_higher_combo(bank, combo_length):
#     combinations = itertools.combinations(bank, combo_length)
#     combinations_list = []
#     for item in combinations:
#         combinations_list.append(int(''.join(item)))
#     return max(combinations_list)

def get_higher_combos(banks):
    return map(lambda bank : max_numeric_combination(bank, COMBO_LENGTH), banks)

def get_sum_of_higher_combos(combos):
    higher_combos = get_higher_combos(combos)
    return sum(higher_combos)

def max_numeric_combination(s: str, k: int):
    stack = []
    to_remove = len(s) - k

    for c in s:
        while stack and to_remove > 0 and stack[-1] < c:
            stack.pop()
            to_remove -= 1
        stack.append(c)

    # on garde seulement les k premiers (stack peut être plus longue)
    return int("".join(stack[:k]))


def main():
    banks = get_banks()
    sum = get_sum_of_higher_combos(banks)
    print("Sum of all joltages : " + str(sum))

main()