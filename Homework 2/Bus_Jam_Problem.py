#Bus Jam Problem
from random import random

#bus jam problem
def P(n, k):
    times = []
    for i in range(n): #generate the times
        times.append(random() * 60)

    times = sorted(times) #sort the times

    gaps    = []  #arrays of all the time gaps
    timeGap = 0   #'current' time gap
    numBus  = 0   #number of buses at the stop, not including itself

    for j in range(n-1): #find all the time gaps
        gaps.append(times[j+1] - times[j])

    for k in gaps: #find if they overlap
        if ((timeGap + k) < 1):
            timeGap += k
            numBus += 1
        else:
            timeGap = 0
            numBus = 0

        if (numBus > k): #check for k
            return 1  #yes jam
        else:
            return 0 #no jam

#calculate the probability of having a bus jam
def probs(n, k):
    sum = 0
    for x in range(10000): #always iterate 100 times
        sum += P(n, k)
    return sum/10000.0

#fixed bus frequency print out
print("Fixed Bus Frequency")
print("-------------------")

fixed_bus = []
for a in range(1, 4):
    print("P(10, " + str(a) + ") = " + str(probs(10, a)))

#fixed capacity frequency print out
print("Fixed Capacity Frequency")
print("------------------------")

#n=1
fixed_bus = []
for a in range(10, 21):
    print("P(" + str(a) + ", 1) = " + str(probs(a, 1)))

print("")

#n=2
fixed_bus = []
for a in range(10, 21):
    print("P(" + str(a) + ", 2) = " + str(probs(a, 2)))
