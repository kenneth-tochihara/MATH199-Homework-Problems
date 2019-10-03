#Calculating pi by tossing coins

#Import random library
from random import random

def runSim():
    #Run k simulations, with 2n flips each,
    k, n2 = 10**5, 2*(10**1)
    flips = []

    for i in range(k):
        sum = 0 #Initialize for total number of heads
        for j in range(n2):
            if int(random() * 2) == 1: #Flip event and check to see if heads
                sum += 1
        flips.append(sum) #Get an array of flips per simulation

    #Loop through results to find if 10**3 = n
    sum = 0 #Initialize counter for number of simulations had 10**3 = n
    for l in flips:
        if l == n2/2:
            sum += 1

    #Probability that exactly n heads in 2n tosses based on k simulations
    prob = sum/k

    #Return value for pi
    return (1/(((n2/2)**(1/2))*prob))**2

print(runSim())
