#How often does a random walk return to the start?

#Import randint function from random
from random import randint
from math import pi

returns = []
K = 10000
def runSim(n, k = K):
    #Initializing position
    x = 0

    #Running multiple simulations
    for i in range(k):
        sum = 0 #Number of times it returns to zero

        #Drunkard's Walk Simulation
        for j in range(n):

            #Movement
            if randint(0,1) == 1: #Generates 0 or 1
                x += 1 #Right
            else:
                x -= 1 #Left

            #Check if returned to the same location
            if x == 0:
                sum += 1

        returns.append(sum)

    #Data Analysis to find Rn
    total = 0
    for m in returns:
        total += m

    return (total/float(k*n)) #Experimental Data

#Run Sim for multiple n's
print("Experimental Probability total returns/total walks")
for n in [10, 100, 1000]:
    probs = runSim(n)
    print(str(n) + ": " + str(probs))

print("\nCalculated probability = (1/(((n*pi)**(0.5))))/(K**(0.5))")
for n in [10, 100, 1000]:
    probs = (1/(((n*pi)**(0.5))))/(K**(0.5))
    print(str(n) + ": " + str(probs))
