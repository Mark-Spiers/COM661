#--------------------------------Part 1--------------------------------
import os
import re
script_dir = os.path.dirname(__file__)
rel_path = "FTSE100.txt"
abs_file_path = script_dir + "/" + rel_path

file = open(abs_file_path, 'r')
heading = file.readline().rstrip()
heading = re.split(r'\t+', heading)
print(heading)

companies = [line.rstrip('\n') for line in file]

for i in range(len(companies)):
    companies[i] = re.split(r'\t+', companies[i])
    print(companies[i])
    #^this print command may have issues depending on the terminal it is being ran on, due to the way it is formated

file.close()

#--------------------------------Part 2--------------------------------
def lowest_lastPrice(companies):
    lowest = 0

    for i in range(1, len(companies)):
        if companies[i][2] < companies[lowest][2]:
            lowest = i

    return companies[lowest][1]

print(lowest_lastPrice(companies))
    
#--------------------------------Part 3--------------------------------
def change(companies):

    changes = []
    for i in companies:
        try:
            changes += [[i[1], i[3]]]
        except:
            continue
        
    max = changes[0]
    min = changes[0]
    total = 0.
    for i in changes:
        if i[1] == '':
            continue
        val = float(i[1])
        total += val
        if val < 0:
            val *= -1
            
        if val > float(max[1]):
            max = i
            continue
        if val < float(min[1]):
            min = i
            continue

    avg = total/(len(changes))
    
    print(max)
    print(min)
    print(avg)

change(companies)

#I didn't do part 4, cause it was simple, just create a new arr, and add values which are full to it then return it back, so completeSym = complete(companies)


#--------------------------------Part 5--------------------------------
#float wasn't required here, but I feel this should of been float in the first place.
def get_dict(companies):
    dictionary = {}
    for i in companies:
        try:
            #converting all companies with a value to float
            dictionary[i[0]] = float(i[len(i)-1].replace("\"", "").replace(",", ""))
        except:
            #2 companies don't have values so set the value to a float of 0
            dictionary[i[0]] = 0.0
            continue
    return dictionary
            
CompDict = get_dict(companies)

print(CompDict)