#Smallest and largest gaps between points
from random import random

def gaps(n):
    nums = []
    for i in range(n):
        nums.append(random())

    nums = sorted(nums)

    max_gap = float('-inf')
    min_gap = float('inf')

    for j in range(n-1):
        gap = nums[j+1] - nums[j]
        if (max_gap < gap): max_gap = gap
        if (min_gap > gap): min_gap = gap

    return [min_gap, max_gap]

for k in range(1, 6):
    #Calculate min and max gaps
    inst = 10**k
    val = gaps(inst)

    #Write to terminal min and max gaps
    print("m(" + str(inst) + ") = " + str(val[0]))
    print("M(" + str(inst) + ") = " + str(val[1]) +"\n")

print("Equation: m(n) = (10^-3)/n")
print("          M(n) = 1/n")
