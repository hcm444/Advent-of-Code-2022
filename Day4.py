import re

reader = open('Day4.txt', 'r')
# opem
lines = reader.readlines()
# read lines
counter = 0
# counter
for line in lines:
    # scrape data per line
    num_list = re.findall('[0-9]+', line.strip())
    # remove integers
    X = (int(num_list[0]), int(num_list[1]))
    # remove range 1
    Y = (int(num_list[2]), int(num_list[3]))
    # remove range 2
    if Y[0] <= X[0] and X[1] <= Y[1] or X[0] <= Y[0] and Y[1] <= X[1]:
        # check if Y is subset of X or X is subset of Y
        counter += 1
        # increment counter if true
print(counter)
# print final sum
