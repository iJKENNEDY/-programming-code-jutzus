abc = ["A","B","C","D","E","F"]
f = open("colorcmds.cmd","a+")

for i in range(len(abc)):
    for j in range(10):
        f.write("start color %s%d \n" % (abc[i],j))

f.close()
