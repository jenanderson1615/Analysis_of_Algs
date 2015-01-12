#########################################
#					#
#  This algorithm uses a divide and	#
#    conquer algorithm with recursion.	#
#    Output gives timing values		#
#					#
#########################################

import random 
import time 

sizeOfArray = 9000 

def recurse(myarray, start, stop):
    if stop == start:
        return (0, 0, 0)
    elif stop == start + 1:
        if myarray[start] > 0:
            return (myarray[start], start, stop)
        else:
            return (0, start, start)
    else:
        mid = (start + stop) // 2
        total = 0
        leftmax = (0, mid)
        for i in range(mid-1, start-1, -1):
            total += myarray[i]
            if total > leftmax[0]:
                leftmax = (total,i)
        total = 0
        rightmax = (0, mid)
        for j in range(mid+1, stop+1):
            total += myarray[j-1]
            if total > rightmax[0]:
                rightmax = (total,j)
        overlay = (leftmax[0]+rightmax[0], leftmax[1], rightmax[1])
        return max(recurse(myarray, start, mid),
                   recurse(myarray, mid, stop),
                   overlay) 

def algorithm3(myarray):
    return recurse(myarray, 0, len(myarray)) 

myarray = [] 
for i in range(sizeOfArray):
	myarray.append(random.randrange(-50, 50, 1)) 

x = 0 
timeArray = [0,0,0,0,0,0,0,0,0,0] 
while x < 10:
	t0 = time.time()
	algorithm3(myarray)
	elapsedtime = time.time() - t0
	timeArray[x] = elapsedtime
	x = x + 1 

y = 0 
tot = 0 
while y < 10:
	tot = tot + timeArray[y]
	y += 1 

average = tot/10 
print "average time for array of size ", sizeOfArray, ": ", average
