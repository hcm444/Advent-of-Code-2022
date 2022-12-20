with open("Day7.txt") as file:
    cmds = [word.strip() for word in file.readlines()]
path = '/home'
dirs = {'/home': 0}
x = 0
for cmd in cmds:
    if cmd[0] == '$':
        if cmd[2:4] == 'ls':
            pass
        elif cmd[2:4] == 'cd':
            if cmd[5:6] == '/':
                path = '/home'
            elif cmd[5:7] == "..":
                path = path[:path.rfind("/")]
            else:
                path = path + '/' + cmd[5:]
                dirs.update({path: 0})
    elif cmd[0:3] == 'dir':
        pass
    else:
        d = path
        for i in range(path.count('/')):
            dirs[d] = dirs[d] + int(cmd[:cmd.find(" ")])
            d = d[:d.rfind("/")]

v = []
for d in dirs:
    if 100000 < dirs[d]:
        pass
    else:
        x = x + dirs[d]
    if 30000000 - (70000000 - dirs['/home']) > dirs[d]:
        pass
    else:
        v.append(dirs[d])
print(min(v, default=0))
