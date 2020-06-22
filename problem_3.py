from SemanticAnalysis import positiveword,negativeword
from Getlocation import distance,files

#read option pf path
line=[]
for i in range(len(files)):
    line.append(files[i].split('\n'))


preference = [0] *(7)

transport=[0]*7
transport_string=['bus','ferry','lrt and mrt','ktm','grab','taxi','flight']

# calculate level of preference for each transportation, if negative then tranportation+=2, 3 negative ,transport=6, 3 positve, transport=0
for i in range(3):
    if positiveword[i]<negativeword[i]:
        transport[0]+=2
    if positiveword[i+3]<negativeword[i+3]:
        transport[1]+=2
    if positiveword[i+6]<negativeword[i+6]:
        transport[2]+=2

    if positiveword[i+9]<negativeword[i+9]:
        transport[3]+=2

    if positiveword[i+12] < negativeword[i+12]:
        transport[4]+=2

    if positiveword[i+15] < negativeword[i + 15]:
        transport[5]+=2
    if positiveword[i+18] < negativeword[i + 18]:
        transport[6]+=2

for i in range(len(transport)):
    if transport[i]==4:
        print(transport_string[i],'shows negative sentiment')
    elif transport[i]==6:
        print(transport_string[i],'shows negative sentiment')
    else:
        print(transport_string[i],'shows positive sentiment')


#calculate total preference of transportation used in each option
for i in range(len(line)):
    lines=str(line[i])
    path = lines.split(',')
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
            temp +=3
    preference[i] = temp / len(path)


#index=rank of path according to distance,shorter distance=lowest mark
index=[0]*len(line)
for i, x in enumerate(sorted(range(len(distance)), key=lambda y: distance[y])):
    index[x] = i

#
for i in range(len(index)):
    preference[i]+=index[i]

# first and second is the index of first and second smallest preference
#first_value and second_value is their value
first=second =0
first_value=second_value=2147483648
for i in range (len(preference)):
    #if current preference([i]) is bigger than first, first = preference[i], second =first
    if (preference[i] < first_value):
        second = first
        second_value = first_value
        first_value = preference[i]
        first = i
    # if if current preference([i]) is bigger than second,second=preference[i]
    elif (second_value > preference[i] and preference[i] != first_value):
        second = i
        second_value = preference[i]


# print best path
bestpath=str(line[first])
bestpath=bestpath.replace('[','').replace(']','').replace('.kml','')
print('The best path is by:', bestpath)
print('the distance of the path is:',distance[first])
print('the negative preference score of the path is:',preference[first])
print('We choose the path because it is shortest, providing second shortest distance=',distance[second],'and second smallest negative preference score=',preference[second])








