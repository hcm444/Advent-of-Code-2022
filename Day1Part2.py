reader = open('Day1.txt', 'r')
lines = reader.readlines()
sum_x = 0
#sum
index = 0
#index
arr = []
#array of sums
for line in lines:
    #iterate
    x = (line.strip())
    #strip data
    if x.isnumeric():
        #check if numeric
        sum_x = sum_x + int(x)
        #summation
        arr.insert(index, sum_x)
        #insert sum at index 0
    else:
        sum_x = 0
        #reset sum if blank line
        index = index + 1
        #iterate index by 1

i = sorted(arr)
print(i[-1]+i[-2]+i[-3])









