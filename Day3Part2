reader = open('Day3.txt', 'r')
#open file
lines = reader.readlines()
#reader
counter = 0
arr = []
new_arr = []
sum = 0
#counter
def split(list_a, chunk_size):
  for i in range(0, len(list_a), chunk_size):
      #divide array into new array of thirds
    yield list_a[i:i + chunk_size]
for line in lines:
    #for each read line
    counter += 1
    #scan lines
    data = sorted(set((line.strip())))
    #convert to set of course
    arr.insert(counter-1,data)
new = (split(arr,3))
for arr in new:
    first = arr[0]
    #first line to compare
    second = arr[1]
    #second line to compare
    third = arr[2]
    #third line to compare
    for char in first:
        if char in second:
            if char in third:
                new_arr.append(char)
for character in new_arr:
    if character.islower():
        #if lower convert to proper letter of the alphabet
        converted_number = ord(character) - 96
    if character.isupper():
        #if upper do the same
        converted_number = (ord(character) - 96) + 58
    sum = sum + converted_number
print(sum)

