class Stack:
    def __init__(self):
        self.stack = list()
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return -1
    def isEmpty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)

s = Stack()

def dfs_main(g,color):
    for i in range(len(g)):
        if color[i] == 0:
            dfs(g,color,i)
def dfs(g,color,i):
    color[i] = 1
    for index in g[i]:
        if color[index] == 0:
            dfs(g,color,index)
    s.push(i)
    color[i] = 2
def color(g,color,gr):
    count = 0
    while not s.isEmpty():
        tmp = s.pop()
        if color[tmp] == 0:
            count+=1
            dfs2(g,color,gr,count,tmp)
def dfs2(g,color,gr,count,i):
    color[i] = 1
    gr[i] = count
    for index in g[i]:
        if color[index] == 0:
            dfs2(g,color,gr,count,index)
    color[i] = 2

v,e = [int(e) for e in input().split()]
a = [[] for i in range(v)]
c = [0 for i in range(v)]
a_inverse = [[] for i in range(v)]
c_inverse = [0 for i in range(v)]
group = [0 for i in range(v)]

for i in range(e):
    start,end = [int(e) for e in input().split()]
    a[start].append(end)
    a_inverse[end].append(start)

print(a)
print(a_inverse)
dfs_main(a_inverse,c_inverse)
color(a,c,group)

for i in range(len(group)):
    print("index : "+str(i)+". the group is "+str(group[i]))
    
