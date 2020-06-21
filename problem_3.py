from SemanticAnalysis import positiveword,negativeword
from Getlocation import distance,files

#read option pf path
line=files.split("\n")




preference = [0] *( len(line)-1)
temp=[0]*( len(line)-1)
transport=[10]*7
transport_string=['bus','ferry','lrt and mrt','ktm','grab','taxi','flight']

# calculate level of preference for each transportation, if negative then tranportation-=1
for i in range(3):
    if positiveword[i]<negativeword[i]:
        transport[0]-=1
    if positiveword[i+3]<negativeword[i+3]:
        transport[1]-=1
    if positiveword[i+6]<negativeword[i+6]:
        transport[2]-=1

    if positiveword[i+9]<negativeword[i+9]:
        transport[3]-=1

    if positiveword[i+12] < negativeword[i+12]:
        transport[4]-=1

    if positiveword[i+15] < negativeword[i + 15]:
        transport[5]-=1
    if positiveword[i+18] < negativeword[i + 18]:
        transport[6]-=1

for i in range(len(transport)):
    if transport[i]==7:
        print(transport_string[i],'shows negative sentiment')
    else:
        print(transport_string[i],'shows positive sentiment')


#calculate total preference of transportation used in each option
for i in range(len(line)-1):
    path = line[i].split(',')
    temp = 0
    for j in range(len(path)):
        if path[j].__contains__('bus'):
            temp += transport[0]

        elif path[j].__contains__('ferry'):
            temp += transport[1]
        elif path[j].__contains__('lrt') or path[j].__contains__('mrt'):
            temp += transport[2]

        elif (path[j].__contains__('komuter') or path[j].__contains__('ets')):
            temp += transport[3]

        elif path[j].__contains__('grab'):
            temp +=transport[4]
        elif path[j].__contains__('taxi'):
            temp += transport[5]
        elif path[j].__contains__('flight'):
            temp += transport[6]
        elif path[j].__contains__('walk'):
            temp += 5
    preference[i] = temp / len(path)


#index=rank of path according to distance,shorter distance=lowest mark
index=[0]*len(distance)
for i, x in enumerate(sorted(range(len(distance)), key=lambda y: distance[y])):
    index[x] = i

#
for i in range(7):
    preference[i]+=index[i]


max_value=preference[0]
max=0
for i in range (len(preference)-1):

    if(preference[i]<max_value):
        max=i
        max_value=preference[i]




print('the best option is taking',line[max])










