import re

instructions = []
rangeLen = 100
startPosition = 50
positionsList = list(range(rangeLen))
with open("real_input.txt") as f:
  for instruction in f:
    direction = re.search('^L|R', instruction, re.IGNORECASE)
    shiftCount = re.search('[0-9]+$', instruction, re.IGNORECASE)
    instructions.append({
      "direction": direction.group(),
      "shiftCount": shiftCount.group()
    })

position = startPosition
hitZeroCount = 0
# print("hitZeroCount : " + str(hitZeroCount))
# print("Position : " + str(position))
for instruction in instructions:
  if instruction['direction'] == "L":
    for i in range(int(instruction['shiftCount'])):
      position = positionsList[(position - 1) % rangeLen]
      if(position == 0):
        hitZeroCount += 1
  else:
    for i in range(int(instruction['shiftCount'])):
      position = positionsList[(position + 1) % rangeLen]
      # print(position)
      if(position == 0):
        hitZeroCount += 1
  # print("hitZeroCount : " + str(hitZeroCount))
  # print("Position : " + str(position))

print(hitZeroCount)
