#Practical Lab 2

#imports
import random

#task 1

def toss_coin(n):
    vals = [0,0]
    for i in range(n):
        x = random.randint(0,1)

        if x == 0:
            vals[0] += 1
        else:
            vals[1] += 1

    return vals

print(toss_coin(5))


#task 2

def loop():
    x = 0
    sum = 0
    while True:
        x = int(input("please enter a number: "))

        if type(x) == int and x > 0:
            sum += x
        elif type(x) == int and x < 0:
            break
    
    return sum

print(loop())

#task 3
def print_pattern(n):
    for i in range (n, 0, -1):
        print("*"*i)

print_pattern(5)

#task 4

def fah(i):
    return (9/5)*i + 32

def display_temp():
    temp = [[0, 32]]
    for i in range (1, 20):
        temp += [[i, fah(i)]]
    
    print(temp)

    for (C, F) in temp:
        print("" + str(C) + "C, " + str(F) + "F")

display_temp()

#task 5

#part 1

def loop30():
    sum = 0
    for i in range(1,31):
        sum += i/(30-(i-1))
    return sum

print(loop30())

#part 2

def loopN(n):
    sum = 0
    for i in range(1,(n+1)):
        sum += i/(n-(i-1))
    return sum

print(loopN(5))
        

#task 6
def rand80():
    i = 0
    while i <= 80:
        i = random.randint(1,100)
        print(i)

rand80()