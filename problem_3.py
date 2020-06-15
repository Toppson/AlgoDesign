from SemanticAnalysis import positiveword,negativeword
from Getlocation import distance

#read option pf path
with open('options.txt') as myfile:
    line = myfile.read().split("\n")


# distances= ranking of path according to distance in Shortest Path
distances = [0] * 7

# the first element of distances =7 and the last =1
for i in range(7):
    distances[i] = i

preference = [0] *( len(line)-1)

car = 10
flight = 10
bus = 10
ktm = 10
lrt_mrt = 10
grab = 10
taxi = 10
ferry = 10
walk = 5

# calculate level of preference for each transportation, if negative then tranportation-=1
for i in range(3):
    if positiveword[i]<negativeword[i]:
        bus-=1

    if positiveword[i+3]<negativeword[i+3]:
        ferry-=1
    if positiveword[i+6]<negativeword[i+6]:
        lrt_mrt-=1

    if positiveword[i+9]<negativeword[i+9]:
        ktm-=1

    if positiveword[i+12] < negativeword[i+12]:
        grab -= 1

    if positiveword[i+15] < negativeword[i + 15]:
        taxi-= 1
    if positiveword[i+18] < negativeword[i + 18]:
        flight -= 1


#calculate total preference of transportation used in each option
for i in range(len(line)-1):
    path = line[i].split(',')
    temp = 0
    for j in range(len(path)):
        if path[j].__contains__('car'):
            temp += car
        elif path[j].__contains__('ferry'):
            temp += ferry
        elif path[j].__contains__('bus'):
            temp += bus
        elif path[j].__contains__('flight'):
            temp += flight
        elif (path[j].__contains__('komuter') or path[j].__contains__('ets')):
            temp += ktm
        elif path[j].__contains__('lrt') or path[j].__contains__('ets'):
            temp += lrt_mrt
        elif path[j].__contains__('grab'):
            temp += grab
        elif path[j].__contains__('taxi'):
            temp += taxi
        elif path[j].__contains__('walk'):
            temp += walk
    preference[i] = temp / len(path)


#distance = distance of path from Getlocation,sort option accendingly according to distance
for i in range(len(distances)):
    for j in range(0, len(distances) - 1 - i):
        if distances[j] > distances[j + 1]:
            distances[j], distances[j + 1] = distances[j + 1], distances[j]
            preference[j], preference[j + 1] = preference[j + 1], preference[j]
            line[j], line[j + 1] = line[j + 1], line[j]

# add distances to preference, preference=ranking of path according to distance and preference of article
for i in range(len(distances)):
    preference[i]+=distances[i]


max=0

for i in range (len(distances)-1):

    if(preference[i]<preference[i+1]):
        max=i+1

print('the best option is taking',line[max])










