import math
import statistics

with open('final.txt', 'r') as file:       #initialize lists of nodes and edges
    matchedG1 = [int(line.split(None, 1)[0]) for line in file]
with open('final.txt', 'r') as file:
    matchedG2 = [int(line.split(None, 1)[1]) for line in file]   
with open('seed_G1.edgelist', 'r') as file:
    G1x = [int(line.split(None, 1)[0]) for line in file]
with open('seed_G1.edgelist', 'r') as file:
    G1y = [int(line.split(None, 1)[1]) for line in file]
with open('seed_G2.edgelist', 'r') as file:
    G2x = [int(line.split(None, 1)[0]) for line in file]
with open('seed_G2.edgelist', 'r') as file:
    G2y = [int(line.split(None, 1)[1]) for line in file]    

resultG1 = []
resultG2 = []
wrongNode = 9999

i = 0
index = 0
degreeG1 = 0
mappedG1 = 0
matchedLength = len(matchedG1)
G1Length = len(G1x)
G2Length = len(G2x)
mappedNeighbors = []
for a in G1x:       #iterate through each node in the seed_G1.edgelist file
    while G1x[i] == index:      #each node has multiple edges,
        for k in matchedG1:        #so check if i still points to current working node
            if k > matchedLength-1:
                continue
            if G1y[i] == matchedG1[k]:      #check if edge points to mapped node
                mappedG1 += 1
                mappedNeighbors.append(matchedG2[k])    #create list of mapped edges
        degreeG1+= 1
        if i == G1Length-1: #Prevent index out of range
            break
        i += 1
    index += 1
    j = 0           #values for G2, reset for each iteration
    index2 = 0
    degreeG2 = 0
    mappedG2 = 0
    score = 0
    max1 = 0
    max2 = 0
    maxNode = 0
    scoreList = []
    if index-1 == 4563:
        break
    for b in G2x:       #iterate through each node in seed_G2.edgefile
        while G2x[j] == index2:     #check if j still points to current working node
            if G2y[j] in mappedNeighbors:   #see if mapped edges list matches any G2 edges
                mappedG2+= 1    
            degreeG2+= 1
            if j == G2Length-1: #Prevent index out of range
                break
            j+= 1 
        while G2x[j] != index2:
            if degreeG1!=0 and degreeG2!=0: #calculate score
                score = (min(mappedG1, mappedG2)) / (math.sqrt(degreeG1) * math.sqrt(degreeG2))
            else:   
                score = 0       #if node is unconnected: score = 0
            scoreList.append(score)
            if score > max1:        #save max and 2nd max
                max1 = score
                maxNode = G2x[j]
            elif score > max2:
                max2 = score
            degreeG2 = 0
            mappedG2 = 0
            index2 += 1
            
    std = statistics.stdev(scoreList)        #calculte std
    if std != 0:
        ecce = (max1 - max2)/std             #calculate ECCE
    else: 
        ecce = 0
    print(ecce, index-1, maxNode-1)
    if ecce > 3.3:                          #ecce check
        resultG1.append(index-1)
        resultG2.append(maxNode-1)
    if ecce < 3.3:                          #if bad ecce:
        resultG1.append(index-1)
        resultG2.append(wrongNode)          #pairs with completely unattatched node
        wrongNode -= 1
 
    degreeG1 = 0              #reset G1 values
    mappedG1 = 0
    mappedNeighbors = []

file = open("trueFinal.txt", "w+")
for index in range(len(resultG1)):
    file.write(str(resultG1[index]) + " " + str(resultG2[index]) + "\n")
file.close()
