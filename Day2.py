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
                    #lose + 1
            if i == "C":
                if j == "Y":
                    line_score = 2
                    #lose + 2
            if i == "A":
                if j == "Z":
                    line_score = 3
                    #lose + 3
            if i == "A":
                if j == "X":
                    line_score = 4
                    #draw + 1
            if i == "B":
                if j == "Y":
                    line_score = 5
                    #draw + 2
            if i == "C":
                if j == "Z":
                    line_score = 6
                    #draw + 3
            if i == "C":
                if j == "X":
                    line_score = 7
                    #win + 1
            if i == "A":
                if j == "Y":
                    line_score = 8
                    #win + 2
            if i == "B":
                if j == "Z":
                    line_score = 9
                    #win + 3
    a = a + line_score
print(a)
