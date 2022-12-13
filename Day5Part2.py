reader = open('Day5.txt', 'r')
lines = reader.readlines()[10:]
import re

arr_1 = ['B', 'S', 'V', 'Z', 'G', 'P', 'W']
arr_2 = ['J', 'V', 'B', 'C', 'Z', 'F']
arr_3 = ['V', 'L', 'M', 'H', 'N', 'Z', 'D', 'C']
arr_4 = ['L', 'D', 'M', 'Z', 'P', 'F', 'J', 'B']
arr_5 = ['V', 'F', 'C', 'G', 'J', 'B', 'Q', 'H']
arr_6 = ['G', 'F', 'Q', 'T', 'S', 'L', 'B']
arr_7 = ['L', 'G', 'C', 'Z', 'V']
arr_8 = ['N', 'L', 'G']
arr_9 = ['J', 'F', 'H', 'C']
arr_ = [arr_1, arr_2, arr_3, arr_4, arr_5, arr_6, arr_7, arr_8, arr_9]
for line in lines:
    command = (re.findall(r'\d+', line))
    qty_ = int(command[0])
    from_ = int(command[1])
    to_ = int(command[2])
    # splice integer array into parts
    _MOVE = list(reversed(arr_[from_ - 1]))[:qty_]
    _MOVE_REV = list((arr_[from_ - 1]))[:qty_]
    MOVE_ = list(reversed(arr_[from_ - 1]))[qty_:]
    MOVE_REV_ = list((arr_[from_ - 1]))[qty_:]
    # remove the reversed array
    arr_[from_ - 1] = list(reversed(MOVE_))
    # I don't know what to say here, just ensure the first array op is correct
    TO = arr_[to_ - 1] + list(reversed(_MOVE))
    arr_[to_ - 1] = TO
print(arr_)
#print entire array, just notice last element of each
