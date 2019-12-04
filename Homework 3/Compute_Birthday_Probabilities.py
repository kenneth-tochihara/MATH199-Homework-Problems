#-------------------------------------------------------------------------------
# Compute_Birthday_Probabilities.py
#
# Problem 6 on homework 3 for MATH 199 CHP.
#-------------------------------------------------------------------------------

print("\n******************************************")
print("          Birthday Probabilities")
print("******************************************")

#-------------------------------------------------------------------------------
# Libraries used
#-------------------------------------------------------------------------------

from random import randint

#-------------------------------------------------------------------------------
# Custom functions and global variables
#-------------------------------------------------------------------------------

# possible combinations of dates
d = 365

# generate list of birthdates
def generate_dates(n):
    dates = []
    for i in range(n):
        dates.append(randint(0, d-1))
    return dates

# run a test case on function f
def test(f, n):
    # run the proability to get the average probability
    avg = 0
    for i in range(25):
        sum = 0
        for j in range(50):
            sum += f(n)
        avg += sum/50
    return avg/25

#-------------------------------------------------------------------------------
# Part (a): Common or adjacent birthdays
#-------------------------------------------------------------------------------

print("\n------------------------------------------")
print(" Part (a): Common, Adjacent\n")

# function to find if duplicate/consecutive birthdays occur
def ComAdj(n):
    dates = generate_dates(n)
    dates.sort()

    for i in range(len(dates)):
        # find common dates
        if dates.count(dates[i]) >= 2:
            return 1
        # find consective dates
        if dates.count(dates[i] + 1) + dates.count(dates[i] - 1) > 0:
            return 1

    return 0

# testing to find n based probability
n = 2
while True:
    prob = test(ComAdj, n)
    if prob > 0.5:
        print(" P_ComAdj(" + str(n) + ")\t= " + str(prob))
        break
    n += 1

#-------------------------------------------------------------------------------
# Part (b): Triple, Quadruple, Quintuple birthdays
#-------------------------------------------------------------------------------

print("\n------------------------------------------")
print(" Part (b): Triple, Quadruple, Quintuple\n")

# function to find if triple/quadruple/quintuple birthdays occur
def triple(n):
    dates = generate_dates(n)
    dates.sort()

    for i in range(len(dates)):
        # find triple days
        if dates.count(dates[i]) == 3:
            return 1

    return 0

def quadruple(n):
    dates = generate_dates(n)
    dates.sort()

    for i in range(len(dates)):
        # find quadruple days
        if dates.count(dates[i]) == 4:
            return 1

    return 0

def quintuple(n):
    dates = generate_dates(n)
    dates.sort()

    for i in range(len(dates)):
        # find quadruple days
        if dates.count(dates[i]) == 5:
            return 1

    return 0

# testing to find n based probability, n = 100 due to time contraint
n = 50
while True:
    prob = test(triple, n)
    if prob > 0.5:
        print(" P_tri(" + str(n) + ")\t= " + str(prob))
        break
    n += 1

n = 150
while True:
    prob = test(quadruple, n)
    if prob > 0.5:
        print(" P_quad(" + str(n) + ")\t= " + str(prob))
        break
    n += 1

n = 250
while True:
    prob = test(quintuple, n)
    if prob > 0.5:
        print(" P_quin(" + str(n) + ")\t= " + str(prob))
        break
    n += 1

#-------------------------------------------------------------------------------
# Part (c): Birthday on everyday of the year
#-------------------------------------------------------------------------------

print("\n------------------------------------------")
print(" Part (c): Everyday of the year\n")

# function to find probability that birthday on every day of the year
def everyday(n):
    dates = generate_dates(n)
    dates = list(set(dates)) # removes duplicates
    dates.sort()

    for i in range(len(dates) - 1):
        # check for each day
        if (dates[i + 1]) != (dates[i] + 1):
            return 0

    return 1

# testing to find n based probability, n = 2000 for time constraint
n = 2100
while True:
    prob = test(everyday, n)
    if prob > 0.5:
        print(" P_every(" + str(n) + ")\t= " + str(prob))
        break
    n += 10

print("\n------------------------------------------")
