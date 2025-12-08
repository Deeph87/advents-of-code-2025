import re

instructions = []
range_len = 100
start_position = 50
positions_list = list(range(range_len))
with open("real_input.txt") as f:
  for instruction in f:
    direction = re.search('^L|R', instruction, re.IGNORECASE)
    shift_count = re.search('[0-9]+$', instruction, re.IGNORECASE)
    instructions.append({
      "direction": direction.group(),
      "shift_count": shift_count.group()
    })

position = start_position
hit_zero_count = 0
for instruction in instructions:
  if instruction['direction'] == "L":
    for i in range(int(instruction['shift_count'])):
      position = positions_list[(position - 1) % range_len]
      if(position == 0):
        hit_zero_count += 1
  else:
    for i in range(int(instruction['shift_count'])):
      position = positions_list[(position + 1) % range_len]
      if(position == 0):
        hit_zero_count += 1

print(hit_zero_count)
