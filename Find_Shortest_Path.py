import sys

class Graph():

    def __init__(self, nodes):
        self.N = nodes
        self.distances = {}
        self.path = []
        # create a empty dictionary with refer to each node
        for i in range(nodes):
            self.distances[i+1] = {}
        print(self.distances)

    def shortestPath(self):
        print('The shortest path is', self.path[self.N-1])

    def distanceNode_Node(self):
        print('Distance from node to node:\n', self.distances, '\n')

    def addDistance(self, From, To, distance):
        # add into the distance to the respective node
        if(From != To):
            self.distances[From][To] = distance

    def minDistance(self, distanceSet, sptSet):
        # finding the min distance index
        min = sys.maxsize
        for i in range(self.N):
            if distanceSet[i] < min and sptSet[i] == False:
                min = distanceSet[i]
                min_index = i
        return min_index

    def search(self):
        distanceSet = [sys.maxsize] * self.N
        distanceSet[0] = 0
        # to make sure if the vertice been choosen, cannot choose again
        sptSet = [False] * self.N
        # to show the path for each vertice
        path = []
        for i in range(self.N):
            path.append([])

        for i in range(self.N):
            u = self.minDistance(distanceSet, sptSet)
            if path[u] == []:
                path[u].append(1)
            else:
                path[u].append(u+1)
            if u+1 == self.N:
                break
            sptSet[u] = True
            # get from the distance from node to node
            for j in self.distances[u+1]:
                distance = self.distances[u+1][j]
                if distanceSet[j-1] > distanceSet[u] + distance:
                    distanceSet[j-1] = distanceSet[u] + distance
                    if 1 in path[j-1] and 1 in path[u]:
                        path[j-1].clear()
                    for n in path[u]:
                        path[j-1].append(n)
            print('Path:\n',path)
            print('Shortest distance to each node:\n',distanceSet,'\n')

        self.path = path
        print(path)

# a = Graph(5)
# a.addDistance(1,2,50)
# a.addDistance(1,3,35)
# a.addDistance(2,3,10)
# a.addDistance(2,4,5)
# a.addDistance(3,4,25)
# a.addDistance(3,5,30)
# a.addDistance(4,5,15)
# a.distanceNode_Node()
# a.search()
# a.shortestPath()

b = Graph(7)
b.addDistance(1,2,4)
b.addDistance(1,3,6)
b.addDistance(1,4,5)
b.addDistance(2,3,3)
b.addDistance(2,5,7)
b.addDistance(3,4,11)
b.addDistance(3,5,8)
b.addDistance(4,5,2)
b.addDistance(4,6,10)
b.addDistance(4,7,2)
b.addDistance(5,6,5)
b.addDistance(6,7,3)
b.distanceNode_Node()
b.search()
b.shortestPath()