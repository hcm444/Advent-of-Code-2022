reader = open('Day3.txt', 'r')
lines = reader.readlines()
arr = []
k = 0
for line in lines:
    #scan lines
    data = (line.strip())
    #extract data
    data_first = data[0:len(data) // 2]
    #first half of string
    data_second = data[len(data) // 2:len(data)]
    #second half of string
    set_data_first = set(data_first)
    #convert to set so char appears only once
    set_data_second = set(data_second)
    # convert to set so char appears only once
    for char in set_data_first:
        #check first side for char
        if char in set_data_second:
            #if on second side append it to array
            arr.append(char)
def char_position(letter):
    if letter.islower():
        #if lower convert to proper letter of the alphabet
        return ord(letter) - 96
    if letter.isupper():
        #if upper do the same
        return (ord(letter) - 96) + 58
for i in arr:
    #sum all elements of array
    j = (char_position(i))
    k = k + j
print(k)





