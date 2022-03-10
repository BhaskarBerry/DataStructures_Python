"""
Python

"""

def add(a,b):
    for i in range(a-1,b):
        box[i]+=1
def count(k):
    if box.count(k)!=0:
        box.index(k)
        return len(box)-box.index(k)
    else:
        return 0

box=[0]*int(stdin.readline())
for i in range(int(stdin.readline())):
    a,b = stdin.readline().split()
    add(int(a),int(b))
box.sort()
for i in range(int(stdin.readline())):
    print( count(int(stdin.readline())))