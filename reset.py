f = open("input.txt", "wb")
resetString = ('''X X X | X X X | X X X
X X X | X X X | X X X
X X X | X X X | X X X
------+-------+------
X X X | X X X | X X X
X X X | X X X | X X X
X X X | X X X | X X X
------+-------+------
X X X | X X X | X X X
X X X | X X X | X X X
X X X | X X X | X X X''')
f.write(resetString.encode("UTF-8"))
f.close()