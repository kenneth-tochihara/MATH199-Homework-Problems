#Expected duration of gambler's ruin game
from random import randint

def runSim(c, n): # run function f(c,n)
    counter = 0
    n_count = n
    while ((n_count > 0) & (n_count < (n*c))):
        if (randint(0, 1) == 1): #Win
            n_count += 1
        else: #Lose
            n_count -= 1
        counter += 1
    return counter

print("c = 3, n = 10")
sum = 0

for i in range(1000):
    sum += runSim(3, 10)

print("Average duration = " + str(sum/1000))
print("Equation: f(c,n) = (c-1)(n^2)")
