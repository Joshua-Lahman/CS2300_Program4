# Joshua Lahman
# CS2300 Programming Assignment #4
# Part 1

import math


# FUNCTIONS==========================================
# dot product for 2 3x1 column vectors
def dot3x1(a, b): # input is 2 lists of 3 floats each
    return (a[0]*b[0]) + (a[1]*b[1]) + (a[2]*b[2])


# addition for 2 3x1 column vectors
def add3x1(a, b): # input is 2 lists of 3 floats each
    return [round(a[0]+b[0], 1) , round(a[1]+b[1], 1), round(a[2]+b[2], 1)]


# subtractions for 2 3x1 column vectors
def sub3x1(a, b): # input is 2 lists of 3 floats each
    return [a[0]-b[0] , a[1]-b[1], a[2]-b[2]]


# multiplication for 2 3x1 column vectors
def mul3x1(a, b): # input is a float & 1 lists of 3 floats
    return [a*b[0], a*b[1], a*b[2]]


# normalize vector
def normalize(y):
    normal = math.sqrt(y[0]*y[0] + y[1]*y[1] + y[2]*y[2])
    return [y[0]/normal, y[1]/normal, y[2]/normal]


# equation: x' = ((q dot n) / (x dot n)) * x //this is perspective
# perspective projection
def persProj(q, n, x): # input is 3 lists of 3 floats each
    a = dot3x1(q, n) / dot3x1(x, n)
    return mul3x1(a, x)


# equation: x' = x + (([q-x] dot n)/(v dot n)) * v //this is parallel
# parallel projection
def paraProj(q, n, x, v): #input is 4 lists of 3 floats each
    a = sub3x1(q, x)
    b = round(dot3x1(a, n)/dot3x1(v, n), 1)#######################################################################################
    c = mul3x1(b, v)
    return add3x1(c, x)


# DATA INPUT===========================================
# set file name to variable
txt = 'input_1.txt'

# open txt file and copy data
with open(txt, 'r') as f:
    data = f.readlines()  # read raw lines into an array

# organize data into n-dimension array
matrix = []
intCount = 0
for raw_line in data:
    split_line = raw_line.strip().split(" ")  # ["1", "0" ... ]
    # loop to count number of items in matrix
    for x in split_line:
        intCount = intCount + 1
    # format matrix
    nums_ls = [float(x.replace('"', '')) for x in split_line]
    matrix.append(nums_ls)

# INPUT PROCESSING===========================================
# count number of rows in input matrix
totalRowCount = 0
for line in matrix:
    totalRowCount += 1

# create new matrix with by deleting first row of input matrix
newMatrix = []
for i in range(1, totalRowCount):
    newMatrix.append(matrix[i])

# parse instructions from first line in matrix
input123 = []
input456 = []
input789 = []
for i in range(0, 3):
    input123.append(matrix[0][i])
for i in range(3, 6):
    input456.append(matrix[0][i])
for i in range(6, 9):
    input789.append(matrix[0][i])

q = input123
v = input456
n = input789

# normalize n
n = normalize(n)

# create array of points-----------------------
points = []
aList = []
for line in newMatrix:
    aList = []
    for i in range(0, 3):
        aList.append(line[i])
    points.append(aList)

    aList = []
    for i in range(3, 6):
        aList.append(line[i])
    points.append(aList)

    aList = []
    for i in range(6, 9):
        aList.append(line[i])
    points.append(aList)

# PROJECTION CALCULATIONS =======================================
# q = plane point 11, 12, 13
# n = plane direction 17 18 19
# x = point x1 x2 x3, x4 x5 x6, x7 x8 x9

# calculate parallel projections of every point
parallelList = []
for line in points:
    parallelList.append(paraProj(q, n, line, v))

# calculate perspective projections of every point
perspectiveList = []
for line in points:
    perspectiveList.append(persProj(q, n, line))

# DATA OUTPUT =====================================================
# convert parallel points list to matrix
parallelMatrix = []
newLine = []
count = 0
for line in parallelList:
    for i in line:
        newLine.append(i)
    count += 1
    if count % 3 == 0:
        parallelMatrix.append(newLine)
        newLine = []


# convert perspective points list to matrix
perspectiveMatrix = []
newLine = []
count = 0
for line in perspectiveList:
    for i in line:
        newLine.append(i)
    count += 1
    if count % 3 == 0:
        perspectiveMatrix.append(newLine)
        newLine = []

# write parallel to file
parallelFile = open("Part1_parallel_jlahman", "w")
for line in parallelMatrix:
    parallelFile.writelines(str(line[0]) + ' ' + str(line[1]) + ' ' + str(line[2]) + ' ' + str(line[3]) + ' ' + str(line[4]) + ' ' + str(line[5]) + ' ' + str(line[6]) + ' ' + str(line[7]) + ' ' + str(line[8]) + "\n")

# write perspective to file
perspectiveFile = open("Part1_perspective_jlahman", "w")
for line in perspectiveMatrix:
    perspectiveFile.writelines(str(line[0]) + ' ' + str(line[1]) + ' ' + str(line[2]) + ' ' + str(line[3]) + ' ' + str(line[4]) + ' ' + str(line[5]) + ' ' + str(line[6]) + ' ' + str(line[7]) + ' ' + str(line[8]) + "\n")


