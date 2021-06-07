from collections import defaultdict
class graph:
    def __init__(self, vertices):
        self.Ver = vertices
        self.graph = defaultdict(list)
        self.visited = [False] * (self.Ver)
        self.pathes=[]
    def print_of_pathes(self, u, d):
        self.visited[u]= True
        self.pathes.append(u)
        if u == d:
            print(self.pathes)
        else:
            for i in self.graph[u]:
                if self.visited[i]== False:
                    self.print_of_pathes(i, d)
        self.pathes.pop()
        self.visited[u]= False

if __name__ == "__main__":
    n = 1
    s = 1
    fle = open("cord.txt")

    while True:
        g = graph(22)
        l = str(fle.readline()).removeprefix("\n")
        if  l == "":
            break
        e = int(l)

        while True:
            edge = str(fle.readline()).removeprefix("\n").split()
            b = int(edge[1])
            r = int(edge[0])
            if r == 0 and b == 0:
                break
            g.graph[r].append(b)
            g.graph[b].append(r)
        print("CASE "+str(n)+":")
        n =n+1
        g.print_of_pathes(s,e)