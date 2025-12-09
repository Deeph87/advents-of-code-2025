import math

def get_all_ids():
    values = open("input.txt")
    values_list = values.read().split(',')
    output = []
    for ids in values_list:
        range_split = ids.split('-')
        start_range = int(range_split[0])
        end_range = int(range_split[1]) + 1
        output.extend(list(range(start_range, end_range)))
    output.sort()
    return output

def remove_odd_length_ids(ids):
    return [id for id in ids if len(str(id)) % 2 == 0]

def get_invalid_ids(ids):
    invalid_ids = []
    for id in ids:
        sliced = id_slicer(id, 2)
        if len(set(sliced)) == 1:
            invalid_ids.append(id)
    return invalid_ids

def id_slicer(id, group_count):
    result = []
    group_size = math.ceil(len(str(id)) / group_count)
    slice_start = 0
    slice_end = group_size
    for _ in range(group_count):
        result.append(str(id)[slice(slice_start, slice_end)])
        slice_start += group_size
        slice_end += group_size
    return result

def get_multiples(id_length):
    result = []
    loop_range = range(1, id_length + 1)
    for i in loop_range:
        if id_length % i == 0:
            result.append(i)
    return result

def get_additional_invalid_ids(ids):
    invalid_ids = []
    for id in ids:
        multiples = get_multiples(len(str(id)))
        for multiple in multiples:
            sliced = id_slicer(id, multiple)
            if len(sliced) > 1 and len(set(sliced)) == 1:
                invalid_ids.append(id)
    return list(set(invalid_ids))

def main():
    all_ids = get_all_ids()
    filtered_ids = remove_odd_length_ids(all_ids)
    invalid_ids = get_invalid_ids(filtered_ids)
    print("# of invalid ids : " + str(len(invalid_ids)))
    print("sum of invalid ids : " + str(sum(invalid_ids)))
    additional_invalid_ids = get_additional_invalid_ids(all_ids)
    print("# of additional invalid ids : " + str(len(additional_invalid_ids)))
    print("sum of additional invalid ids : " + str(sum(additional_invalid_ids)))

main()
