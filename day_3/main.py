import heapq

def get_banks():
    values = open("input.txt")
    values_list = values.read().split('\n')
    return values_list

def get_higher_combo(bank):
    combos = []
    ten_index = 0
    bank_len = len(bank)
    while ten_index < bank_len:
        for unit_index in range(ten_index + 1, bank_len):
            combo = int(bank[ten_index] + bank[unit_index])
            combos.append(combo)
        ten_index += 1
    return heapq.nlargest(1, combos)[0]


def main():
    banks = get_banks()
    higher_combos = []
    for bank in banks:
        higher_combo = get_higher_combo(bank)
        higher_combos.append(higher_combo)
    print("Sum of max combos is : " + str(sum(higher_combos)))

main()