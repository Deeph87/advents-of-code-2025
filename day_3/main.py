import heapq

def get_banks():
    values = open("input.txt")
    values_list = values.read().split('\n')
    return values_list

def get_higher_combo(bank, tail_count = 1):
    combos = []
    ten_index = 0
    bank_len = len(bank)
    while ten_index < bank_len:
        for unit_index in range(ten_index + 1, bank_len):
            combo = [bank[ten_index]]
            for tail_index in range(tail_count):
                computed_index = unit_index + tail_index
                if computed_index < len(bank):
                    combo.append(bank[unit_index + tail_index])
                    combos.append(int(''.join(combo)))
        ten_index += 1
    return heapq.nlargest(1, combos)[0]


def main():
    banks = get_banks()
    higher_combos = []
    giga_mega_higher_combos = []
    for bank in banks:
        higher_combo = get_higher_combo(bank)
        giga_mega_higher_combo = get_higher_combo(bank, 11)
        higher_combos.append(higher_combo)
        giga_mega_higher_combos.append(giga_mega_higher_combo)
    print("Sum of max combos is : " + str(sum(higher_combos)))
    print(bank, giga_mega_higher_combos)
    print("Sum of max giga mega combos is : " + str(sum(giga_mega_higher_combos)))

main()