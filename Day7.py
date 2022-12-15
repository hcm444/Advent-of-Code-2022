from collections import defaultdict

dict = {"":0}
path = []
sum = []
i = 0
with open('Day7.txt', 'r') as reader:
    for line in reader:
        files = line.strip().split()
        if files[1] == "cd":

            if files[2] == "..":
                path.pop

            else:
                path.append(files[2])
                list = [[] for i in path]
        elif files[1] == "ls":
            continue

        else:
            if files[0] != "dir":
                print(path, int(files[0]))
                for i in list:
                    i.append(int(files[0]))
                    print(i)






