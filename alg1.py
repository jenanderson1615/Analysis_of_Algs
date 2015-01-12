#########################################
#					#
#  Uses an enumeration loop over a pair #
#    of indices to find the max 	#
#    subarray with a random array.  	#
#    Random arrays are created with	#
#    values -50 to 50			#
#					#
#########################################

import random 
import time 

sizeOfArray = 50 

def maxSubArray(myarray):
	maxarray = myarray[0]
	current = 0
	lengthBeingChecked = 1
	m = 0
	i = 0
	while lengthBeingChecked <= len(myarray):
		while i <= (len(myarray) - lengthBeingChecked):
			current = 0
			m = i
			while m <= (lengthBeingChecked - 1 + i):
				current = current + myarray[m]
				m += 1
			if current > maxarray:
				maxarray = current
			i += 1
		i = 0
		lengthBeingChecked += 1
	print maxarray

#defining an array
myarray = [] 
for i in range (sizeOfArray):
    myarray.append(random.randrange(-50,50,1))

#start clock, call function, stop clock
t0 = time.time() 
maxSubArray(myarray)
print time.time() - t0, "seconds time"
