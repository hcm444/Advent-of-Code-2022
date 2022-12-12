import re
reader = open('Day4.txt', 'r')
lines = reader.readlines()
counter = 0
for line in lines:
    num_list = re.findall('[0-9]+', line.strip())
    X = (int(num_list[0]), int(num_list[1]))
    Y = (int(num_list[2]), int(num_list[3]))
    print(X,Y)
    if X[0] in range(Y[0],Y[1]+1) \
    or X[1] in range(Y[0],Y[1]+1) \
    or Y[0] in range(X[0],X[1]+1) \
    or Y[1] in range(X[0],X[1]+1):
        counter+=1
print(counter)
