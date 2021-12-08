def tryagain(counts, days):
   
    # This works for small numbers like 80 but get bigger and just spins out of control!!!
    # for day in range(1, days +1):
    #     num_0 = school.count(0) 
    #     school = [fish-1 if fish !=0 else 6 for fish in school ]  
    #     school.extend([8]*num_0) 
    # return len(school)

    # So with hint...from Ron  use fixed array of counts
    for day in range(1, days + 1):
                num_0 = counts[0]
                for id in range(0,8):
                    counts[id] = counts[id + 1]      
                if num_0 > 0:
                    counts[6] += num_0    
                counts[8] = num_0     
    return sum(counts)

def evenMoreSimple(counts, days):
    for day in range(1, days + 1):
        counts.append(counts.pop(0))
    return sum(counts)    

def main():

    file_example = "day6_example_input.txt"
    file_my = "day6_input.txt"
   
    #part 2 
    # create an list from 0 t0 8 to represent number of fish at each time in life cycle 0 to 8
    # start with all 0 counts
    school_counts = [0]*9
    print ("SCHOOL counts:", school_counts)
    # school = {}
    f=open(file_my)
    line = f.readline().strip().split(',')
    f.close()
    school = [int(num) for num in line]
    print("SCHOOL: ", school)
    for num in school:
        school_counts[num] +=1
    print ("SCHOOL counts:", school_counts) 
    days = 256
    count = tryagain(school_counts, days)
    print("Lantern fish count after {} days: {}".format(days, count))
    count = evenMoreSimple(school_counts, days)
    print("Lantern fish count after {} days: {}".format(days, count))


# Initial state: 3,4,3,1,2
# After  1 day:  2,3,2,0,1
# After  2 days: 1,2,1,6,0,8
# After  3 days: 0,1,0,5,6,7,8
# After  4 days: 6,0,6,4,5,6,7,8,8
# After  5 days: 5,6,5,3,4,5,6,7,7,8
# After  6 days: 4,5,4,2,3,4,5,6,6,7
# After  7 days: 3,4,3,1,2,3,4,5,5,6
# After  8 days: 2,3,2,0,1,2,3,4,4,5
# After  9 days: 1,2,1,6,0,1,2,3,3,4,8
# After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
# After 11 days: 6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
# After 12 days: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
# After 13 days: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
# After 14 days: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
# After 15 days: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
# After 16 days: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
# After 17 days: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
# After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8
# After  256 days = 26984457539

    return 0
    
if __name__ == "__main__":
    main()