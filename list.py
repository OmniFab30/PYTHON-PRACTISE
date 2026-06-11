# Exercise 01: Conditional Filtering
#basic code
numberList = [12,8,88,96,2,354,1,7,3]
def filtering(numberList):
    newList = []
    for i in numberList:
        if i % 2 == 0 and i > 10:
            newList.append(i)
    return newList

print(filtering(numberList)) # [12, 88, 96, 354]

#using list comprehension
def filterIng(numberList):
    newList = [i for i in numberList if i % 2 == 0 and i > 10]
    return newList

print(filterIng(numberList)) # [12, 88, 96, 354]

#============================x=================================================
#Exercice 02: Removing duplicates (without a set)
#using second list
listDuplicated = [1, 2, 2, 3, 1, 4]
listNoDuplicated = []
for i in listDuplicated:
    if i not in listNoDuplicated: listNoDuplicated.append(i) 

print(listNoDuplicated)

#no using another list
for i in range(0, len(listDuplicated) - 1):
    for j in range(i + 1, len(listDuplicated) - 1):
        if listDuplicated[i] == listDuplicated[j]: listDuplicated.pop(j)

print(listNoDuplicated)

#using set constructor
def listNoDuplicated(duplicateList):
    noDuplicateList = set(duplicateList)
    return list(noDuplicateList)

print(listNoDuplicated(listDuplicated))

#============================x=================================================
#Exercice 03: List rotation => Performs a rightward rotation by k positions.
liste, k = [1,2,3,4,5], 1
for i in range(k):
    liste.insert(0, liste[-1])
    liste.pop(len(liste) - 1)

print(liste)

#============================x=================================================
#Exercice 04:Intersecting Lists => Find the common elements between two lists 
#without duplicates in the result.

#using double list
firstList , secondList = [1,2,3,4,4,5,7], [3,6,1,1,2,5,7,8]
intersection = [i for i in secondList if i in firstList]
noneDouble = []
for element in intersection:
    if element not in noneDouble: noneDouble.append(element)

print(noneDouble)

#using set constructor
def intersectingList(fList, sList):
    intersection = [i for i in sList if i in fList]
    x = set(intersection)
    return list(x)

print(intersectingList(firstList, secondList))

#============================x=================================================
#Exercise 6: Merged Sorted List => Merges two sorted lists into a single sorted list (without using sort()).
fSortedList = [1,3,5]
sSortedLsit = [2,4,6]



