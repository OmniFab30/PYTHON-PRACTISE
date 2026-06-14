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
#Exercise 05: Merged Sorted List => Merges two sorted lists into a single sorted list (without using sort()).
fSortedList = [1,3,5]
sSortedLsit = [2,4,6]

def mergedSortedList(firstList, secondList):
    firstList.extend(secondList)
    for i in range(len(firstList)):
        for j in range(len(firstList)):
            if firstList[i] < firstList[j]: # [1, 2, 3, 4, 5, 6]
                firstList[i], firstList[j] = firstList[j], firstList[i]
    print(firstList)

mergedSortedList(fSortedList, sSortedLsit)

#============================x=================================================
#Exercise 06:Nested comprehension => Transforms a list of lists into a single list (flatten).

#basic solution
listNoFlatten = [[1,2],[3,4],[5]]
flatten = []
for item in listNoFlatten:
    for i in range(len(item)):
        flatten.append(item[i])

print(flatten)

#using list compréhension
def flattenList(nestedList):
    flatten = [i for item in nestedList for i in item]
    return flatten

print(flattenList(listNoFlatten)) 


#============================x=================================================
#Exercise 07: Matrix => diagonal = 1 and rest = 0
matrix , matrixDimension = [], 3
def doMatrix(m, d):
    for i in range(d):
        subMatrix = []
        for j in range(d):
            subMatrix.append(1) if i == j else subMatrix.append(0)
        m.append(subMatrix)
    
    for i in range(d):
        print(m[i])


doMatrix(matrix,matrixDimension)

#============================x=================================================
#Exercise 08: diagonally Count how many times each element appears in a list
#basic
input = ['a', 'b', 'a', 'c', 'b', 'a']
output = {}
for i in range(len(input)):
    countItem = 0
    for j in range(len(input)):
        if input[i] == input[j] : countItem+= 1
    output.update({f"{input[i]}": countItem})

print(output)

#using count method
for item in input:
    output[item] = input.count(item)
print(output)

#using collections.counter()
from collections import Counter
def counterElement(i):
    output = dict(Counter(i))
    return output

print(counterElement(input))

#============================x=================================================
#Exercise 09: Anagrams => Write a function that checks if two lists of characters are anagrams.
aList = ['a', 'b', 'c']
bList = ['c', 'a', 'b'] 

#basic
if len(aList) == len(bList):
    valid = True
    for element in aList:
        if bList.count(element) != 1:
            valid = False
            break
    print(valid)
else: 
    print("length of array different")
 
#using list comprehension
print(len(aList) == len(bList) and all(bList.count(element) == 1 for element in aList))

#using set constructor
print(set(aList) == set(bList))

#using collections.Counter()
print(Counter(aList) == Counter(bList))

#============================x=================================================
#Exercise 10: Sequence detection => Checks if a list contains a given subsequence.
parentList = [1,2,3,4,5]
sequence = [3,4]

#checking a contiguous sublist using slice method
def contains_subsequence(pList, subseq):
    n, m = len(pList), len(subseq)
    for i in range(n - m + 1):
        if pList[i: i + m] == subseq: return True
    return False

print(contains_subsequence(parentList, sequence))

#checking a contiguous sublist using any() method
def containSubsequence(pList, subseq):
    m = len(subseq)
    return any(pList[i: i + m] == subseq for i in range(len(pList) - m + 1))

print(containSubsequence(parentList, sequence))

#using issubset()
print(set(sequence).issubset(set(parentList)))

#using issuperset()
print(set(parentList).issuperset(set(sequence)))

#using intersection()
print((bool)(set(parentList).intersection(set(sequence))))

# Non-contiguous subsequence using iter() and all() methods
def is_subsequence(pList, subsequence):
    it = iter(pList)
    return all(element in it for element in subsequence)

print(is_subsequence(parentList, sequence))

#============================x=================================================
#Exercise 11: Custom sorting
#basic 
tupleList, i = [("Bina", 12), ("Fabiano", 19), ("Ali", 15)], 0
sortedList = sorted(tupleList, key = lambda x : x[i])
print(sortedList)

#============================x=================================================
#Exercise 12: search nearist value
numbers, target = [10, 22, 35, 47, 55], 41
closet = min(numbers, key = lambda x : abs(x - target))
print(closet)

#============================x=================================================
#Exercise 13: compression
listNoCompressed, listCompressed = [1,1,1,2,2,4,8,9,7,7,2,1,3], []
for i in listNoCompressed:
    listCompressed.append((i, listNoCompressed.count(i)))

listCompressed = sorted(list(set(listCompressed)), key = lambda x :x[0])
print(listCompressed)
