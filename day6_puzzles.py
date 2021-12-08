import matplotlib.pyplot as plt
import numpy as np

def hatchery(interval, filename):
    school = []
    f=open(filename)
    line = f.readline().strip().split(',')
    f.close()
    for x in line:
        fish = {}
        fish['life'] = int(x)
        fish['respawn'] = False
        fish['baby'] = False
        school.append(fish)
    #print("SCHOOL of lantern fish: ", school)
    
    day = 1
    while day <= interval:
        for idf, (fish) in enumerate(school):
        #while day < 80:
            #print("day: ", day
            if fish['respawn'] == True:
                school[idf]['life'] = 6
                school[idf]['respawn'] = False
                f={}
                f['life'] = 8
                f['respawn'] = False
                f['baby'] = True        
                school.append(f)
            elif fish['life'] > 0 and not fish['baby'] == True:
                school[idf]['life'] -= 1
                if fish['life'] == 0:
                    school[idf]['respawn'] = True
            
            if fish['baby'] == True:
                school[idf]['baby'] = False
                #print("reset baby: ",  school[idf]['baby'])
        #print ("day: ", day, " ", school)      
        day = day + 1      
    numberOfFish = len(school)

    return numberOfFish

def genCount(init, school, which_fish, generation, days):
# Does not work...skips last generation...
# Maybe I can get it to work later...hmmmm
    fish_count = 5   # start with 5 in school
    gen_count = 0
    increment = 2
    day = 0
    first_day = init
    first_day_in_gen = 0
    generation = 0
    iterations = 0
    # initial school of fish
    #for fish in school: 

    if which_fish < len(school):
      
        fish = school[which_fish]
        print("FISH #: ", fish)                          
        while day <= days:
            if first_day == True:    
                generation = 1   
                first_day = False
                day = (fish -1 ) + increment 
                first_day_in_gen = day
                gen_count = gen_count + 1
                iterations += 1
                print("================>FISH COUNT (DAY): {}  ({}) ".format(gen_count, day))
       
            if generation in [0,1]:
                increment = 7 
            elif generation > 1:
                increment = 9  

            day = day + increment
            gen_count = gen_count + 1
            iterations +=1
            if iterations == 1:
                first_day_in_gen = day
            print("================>FISH COUNT (DAY): {}  ({}) ".format(gen_count, day))     
           
            if day + increment > days:
                generation = generation + 1
                day = first_day_in_gen
                # first_day_in_gen = day + increment  # this is incrementing everytime...need it to stay
                print("Next gen start day: ", day)
                iterations = 0
                
            if day + increment > days:
                break
        
        gen_count = gen_count + genCount(True, school, which_fish + 1, generation,days)
    
    return gen_count #fish_count        


def try3(school, interval):
    count = 0
    temp = school.copy()
    days = interval + 1
    next_index = len(school) 
    print("Initial school: {}".format(school))
    for day in range(1, days):
        size = len(temp) 
        for key in school:
            fish = school[key]
            if fish == 0:
                fish = 6 
                temp[str(next_index)] = 8
                next_index += 1
            else:
                if int(key) < size:
                    fish -= 1
            temp[key] = fish

        school = temp.copy()        
        #print("School at day {}: {}".format(day, [temp[key] for key in temp]))

    return len(school)

def main():

    file_example = "day6_example_input.txt"
    file_my = "day6_input.txt"
    #part 1    

    #can't do too high of interval...take forever...never comes back   
    # print("Grow the school of lantern fish: ", hatchery(80,file_example))
    # print("Grow the school of lantern fish: ", hatchery(80,file_my))

    #part 2 
    school = []
    # school = {}
    f=open(file_example)
    line = f.readline().strip().split(',')
    f.close()
    # i=0
    # for num in line:
    #     index = str(i)
    #     school[index] = int(num)
    #     i += 1
    
    school = [int(num) for num in line]
    print(school)
    # # pass in initial school
    days = 18

    count = genCount(True, school, 0, 0, days)
    print("Lantern fish count after {} days: {}".format(days, count + len(school)))


# Initial state: 3,4,3,1,2
# After  1 day:  2,3,2,0,1
# After  2 days: 1,2,1,6,0,8
# After  3 days: 0,1,0,5,6,7,8
# After  4 days: 6,0,6,4,5,6,7,8,8
# After  5 days: 5,6,5,3,4,5,6,7,7,8
# After  6 days: 4,5,4,2,3,4,5,6,6,7
# After  7 days: 3,4,3,1,2,3,4,5,5,6
# After  256 days = 26984457539


   # print("Lantern fish count after {} days: {}".format(days, try3(school, days)))
    return 0
    
if __name__ == "__main__":
    main()