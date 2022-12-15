with open('Day6.txt', 'r') as reader:
#open
    line = reader.readline().strip()
#read and strip
for number in range(len(line)):
    if not 14 != len(set(line[number:number + 14])):
        print(number + 14)
        break
