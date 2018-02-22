import numpy as np

sandy = np.array([-1,-1,-1,-1,1,1,0,-1,0,1,1,1,-1,0,1,-1,1,-1,-1,-1,1,1,-1,0,0])
dee = np.array([-1,0,-1,-1,1,0,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,0,-1,1,1])
jim = np.array([-1,0,0,0,1,-1,0,1,0,-1,-1,1,1,0,0,1,1,1,0,1,1,0,-1,-1,1])
tom = np.array([1,1,1,1,1,0,1,1,0,1,1,1,-1,0,0,0,1,1,-1,-1,1,1,1,0,0])
ilana = np.array([1,0,1,1,1,-1,1,1,1,1,1,-1,1,0,0,0,1,1,1,-1,1,0,1,1,0])
eli = np.array([1,0,1,1,-1,0,1,0,0,-1,1,-1,1,0,0,0,1,1,1,1,1,0,1,-1,0])
calvin = np.array([1,-1,0,0,1,0,1,1,0,-1,1,-1,1,0,0,1,1,0,1,-1,1,1,1,0,0])
brandon = np.array([-1,0,0,1,-1,0,-1,0,0,-1,1,-1,1,0,0,1,0,0,0,1,1,0,-1,0,1])
# john = np.array([1,0,0,])
# don = np.array([1,0,1,])
questions = ["Uses amplification","Hopes to become famous","Has a website","Pursued aother career before busking",
"Collaborates with other artists","Believes they won't be busking forever","Has signs while busking","Plays gigs or ope mic nights","Hates Apps",
"Born and Raised in NE","Parents were influetial in music","Millenial","Very interested in listeners and passers by"
,"Has Children","Exposed to music through church","Studied music academically","Will not play if weather is bad","Uses social media","Plays during the week",
"Needs income from busking","Plays in sanctioned spot","Is a teacher","Writes own music","Attached to one physical spot","Improvs"]
nameStrings = ["sandy","dee","jim","tom","ilana","eli","calvin","brandon"]
nameList = np.array([sandy,dee,jim,tom,ilana,eli,calvin,brandon])

def comparePeople(person,other):
    print("People Compared: ",nameStrings[person], " and ",nameStrings[other])

    person1 = nameList[person]
    person2 = nameList[other]
    comparison = person1 * person2
    print("Overall Compatability: ",np.mean(comparison))
    print("Similarities:")
    [print(questions[i]) for i,x in enumerate(comparison) if x ==1]

    print("     ")
    print("Differences:")
    [print(questions[i]) for i,x in enumerate(comparison) if x ==-1]
    print("     ")


def findNeighbor(person,k):

    closest = []
    for i in k:
        closest.append(np.sum((person-i)**2))

    closestk = np.argmin(closest)
    return closestk

def getGroups(k,num):
    buckets = [list() for i in range(num)]
    for index, person in enumerate(nameList):
        # print(findNeighbor(person,k))
        buckets[findNeighbor(person,k)].append(nameStrings[index])
        # print(buckets)

    for i, bucket in enumerate(buckets):
        print("Group: ",i)
        [print(name) for name in bucket]
        print("     ")

def iterateK(k):
    newk = np.zeros(k.shape)
    listK = []
    cost = 0
    for i in k:
        listK.append([])

    for person in nameList:
        closestk = findNeighbor(person,k)
        if not len(listK[closestk]):
            listK[closestk] =np.array([person])
        else:

            listK[closestk] = np.concatenate((listK[closestk],[person]))

    for i in range(len(listK)):
        # print("pre:",listK[i])
        if len(listK[i]) == 1:
            newk[i] = listK[i]
            # print("post 1:",k[i])
        elif len(listK[i]):
            newk[i] = np.mean(listK[i],axis = 0)
            for j in listK[i]:
                cost += np.sum((j-newk[i])**2)
            # print("post:",k[i])
        else:
            newk[i]=k[i]



    return newk, cost

def findkValues(numK,attributes):
    matrix = np.random.rand(numK,attributes)*2 -1
    newMatrix = np.random.rand(numK,attributes)*2 -1
    i = 0
    while not np.array_equal(matrix,newMatrix):
        matrix = newMatrix
        newMatrix,cost = iterateK(matrix)
        # print(matrix)
        # print(newMatrix)
        i+=1
        # print(i,": ",cost)
    return matrix,cost

def keepFindingValues(numK,attributes,iterations):
    finalMatrix, finalCost = findkValues(numK,attributes)
    for i in range(iterations):
        matrix, cost = findkValues(numK,attributes)
        if cost < finalCost:
            finalCost = cost
            finalMatrix = matrix

    return finalMatrix,finalCost
if "__main__" == __name__:
    comparePeople(0,1)
    comparePeople(3,4)
    comparePeople(2,7)
    # num = 3
    # for i in range(5):
    #     matrix, cost = keepFindingValues(num,len(sandy),100)
    #     getGroups(matrix,num)
    #     print("-------------")
