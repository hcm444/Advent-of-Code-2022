import re
reader = open("Day5.txt", "r")
lines = reader.readlines()[10:]
arr_ = [
    ["B", "S", "V", "Z", "G", "P", "W"],
    ["J", "V", "B", "C", "Z", "F"],
    ["V", "L", "M", "H", "N", "Z", "D", "C"],
    ["L", "D", "M", "Z", "P", "F", "J", "B"],
    ["V", "F", "C", "G", "J", "B", "Q", "H"],
    ["G", "F", "Q", "T", "S", "L", "B"],
    ["L", "G", "C", "Z", "V"],
    ["N", "L", "G"],
    ["J", "F", "H", "C"],
]
for line in lines:
    command = re.findall(r"\d+", line)
    # splice integer array into parts
    MOVE = list(reversed(arr_[int(command[1]) - 1]))[: int(command[0])]
    # remove the reversed array
    arr_[int(command[1]) - 1] = list(
        reversed(list(reversed(arr_[int(command[1]) - 1]))[int(command[0]):])
    )
    # I don't know what to say here, just ensure the first array op is correct
    arr_[int(command[2]) - 1] = arr_[int(command[2]) - 1] + MOVE
print(arr_[-1])
# last elements of each array
