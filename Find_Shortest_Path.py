import sys
class Graph():

    def __init__(self, nodes, start, end):
        self.N = len(nodes)
        self.distances = {} # distance From to To (each node)
        self.dictionary = {} # map the direction as int nodes
        self.path = []
        self.shortest_distance = 0
        self.start = start
        self.end = end
        mylist = [start]
        nodes.remove(start)
        for i in nodes:
            if i != end:
                mylist.append(i)
        mylist.append(end)
        # create a empty dictionary with refer to each node
        for i in range(len(mylist)):
            self.distances[i] = {}
            self.dictionary[mylist[i]] = i
        print(self.distances)
        print(self.dictionary)

    def shortestPath(self):
        print('The shortest path is', self.path[self.N - 1])
        print('The distance is', self.shortest_distance)
        to_return = []
        listOfItems = list(self.dictionary.items())
        for i in self.path[self.N - 1]:
            to_return.append(listOfItems[i][0])
        return to_return

    def distanceNode_Node(self):
        # print('Distance from node to node:\n', self.distances, '\n')
        print('Distance from node to node:\n')
        for i in self.distances.keys():
            print("From", i, end="")
            for n in self.distances[i].keys():
                print(" to ", n ,"with",self.distances[i][n])


    def addDistance(self, From, To, distance):
        # add into the distance to the respective node
        from_index = self.dictionary[From]
        to_index = self.dictionary[To]
        self.distances[from_index][to_index] = distance

    def minDistance(self, distanceSet, sptSet):
        # finding the min distance index
        min = sys.maxsize
        min_index = 0
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
                path[u].append(0)
            else:
                path[u].append(u)
            if u + 1 == self.N:
                break
            sptSet[u] = True
            # get from the distance from node to node
            for j in self.distances[u]:
                distance = float(self.distances[u][j])
                if distanceSet[j] > distanceSet[u] + distance:
                    distanceSet[j] = distanceSet[u] + distance
                    if 0 in path[j] and 0 in path[u]:
                        path[j].clear()
                    for n in path[u]:
                        path[j].append(n)
        self.path = path
        end_index = self.dictionary[self.end]
        self.shortest_distance = distanceSet[end_index]
        print('Path:\n',path)
        print('Shortest distance to each node:\n',distanceSet,'\n')
        # print(path)

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
# distance=[]
# temp=[]
# for i in len(fullcoordinatex):
#     for k in len(fullcoordinatex[i]) - 1:
#         distance(fullcoordinatex[i][k],fullcoordinatey[i][k],fullcoordinatex[i][k+1],fullcoordinatey[i][k+1])


# b = Graph(7)
# b.addDistance(1,2,4)
# b.addDistance(1,3,6)
# b.addDistance(1,4,5)
# b.addDistance(2,3,3)
# b.addDistance(2,5,7)
# b.addDistance(3,4,11)
# b.addDistance(3,5,8)
# b.addDistance(4,5,2)
# b.addDistance(4,6,10)
# b.addDistance(4,7,2)
# b.addDistance(5,6,5)
# b.addDistance(6,7,3)
# b.distanceNode_Node()
# b.search()
# b.shortestPath()