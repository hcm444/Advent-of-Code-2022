reader = open('Day2.txt', 'r')
lines = reader.readlines()
a = 0
line_score = 0
for line in lines:
    #iterate
    line_data = (line.strip())
    #strip data
    for i in line_data:
        for j in line_data:
            if i == "B":
                if j == "X":
                    line_score = 1
                    #paper / lose with rock
            if i == "C":
                if j == "Y":
                    line_score = 6
                    #scizzors / draw with scizzors
            if i == "A":
                if j == "Z":
                    line_score = 8
                    #rock / win with paper
            if i == "A":
                if j == "X":
                    line_score = 3
                    #rock / lose with scizzors
            if i == "B":
                if j == "Y":
                    line_score = 5
                    #paper / draw with paper
            if i == "C":
                if j == "Z":
                    line_score = 7
                    #scizzors / win with rock
            if i == "C":
                if j == "X":
                    line_score = 2
                    #scizzors / lose with paper
            if i == "A":
                if j == "Y":
                    line_score = 4
                    #rock / draw with rock
            if i == "B":
                if j == "Z":
                    line_score = 9
                    #paper / win with scizzors
    a = a + line_score
print(a)
