#Jen Anderson 
#CS 325 
#project 2 
#dynamic programming max sub array problem

#########################################
#					#
#  This program uses a dynamic		#
#    programming algorithm to find the  #
#    max subarray.  Output is the max	#
#    subarray and the average time 	#
#    to find 10 max subarrays		#
#					#
#########################################

import random 
import time 
sizeOfArray = 9000 

def maxSubArray(myarray):
	currentSectionMax = myarray[0]
	maxarray = myarray[0]
	currentMaxArray = []
	i = 1
	while i < len(myarray):
		currentSectionMax = max(currentSectionMax + myarray[i], myarray[i])
		currentMaxArray.append(currentSectionMax)
		i += 1
	maxarray = max(currentMaxArray)
	print "max: ", maxarray

myarray = [] 

for i in range (sizeOfArray):
	myarray.append(random.randrange(-50,50,1)) 
x = 0 
timeArray = [0, 0,0,0,0,0,0,0,0,0] 
while x < 10:
	t0 = time.time()
	maxSubArray(myarray)
	elapsedtime = time.time() - t0
	timeArray[x] = elapsedtime
	x = x+1
	myarray = []
	for i in range(sizeOfArray):
		myarray.append(random.randrange(-50,50,1)) 
y = 0 
tot = 0 
while y < 10:
	tot = tot + timeArray[y]
	y += 1 
average = tot/10 
print "average time for array of size ", sizeOfArray, ": ", average
