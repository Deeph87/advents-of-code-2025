import re


instructions = []
rangeLen = 100
startPosition = 50
positionsList = list(range(rangeLen))
with open("input.txt") as f:
  for instruction in f:
    direction = re.search('^L|R', instruction, re.IGNORECASE)
    shiftCount = re.search('[0-9]+$', instruction, re.IGNORECASE)
    instructions.append({
      "direction": direction.group(),
      "shiftCount": shiftCount.group()
    })

position = startPosition
hitZeroCount = 0
for instruction in instructions:
  if instruction['direction'] == "L":
    position = positionsList[(position - int(instruction['shiftCount'])) % rangeLen]
  else:
    position = positionsList[(position + int(instruction['shiftCount'])) % rangeLen]
  if position == 0:
    hitZeroCount += 1

print(hitZeroCount)
