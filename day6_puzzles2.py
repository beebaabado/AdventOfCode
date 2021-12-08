def tryagain(school, days):
    fish = 0

    for day in range(1, days +1):
        if 0 in school:
            school[:] = [fish if fish != 0 else 6 for fish in school]
            num_6 = school.count(6)
            school.extend([8]*num_6)  
            school[:] = [fish if fish in [6,8] else fish-1 for fish in school]
        else:
            school[:] = [fish-1 for fish in school]   
        print("school day {}:  {}".format(day, school))

    return len(school)

def main():

    file_example = "day6_example_input.txt"
    file_my = "day6_input.txt"
   

    #part 2 
    school = []
    # school = {}
    f=open(file_example)
    line = f.readline().strip().split(',')
    f.close()
    school = [int(num) for num in line]
    print(school)
    days = 18

    count = tryagain(school, days)
    print("Lantern fish count after {} days: {}".format(days, count))


# Initial state: 3,4,3,1,2
# After  1 day:  2,3,2,0,1
# After  2 days: 1,2,1,6,0,8
# After  3 days: 0,1,0,5,6,7,8
# After  4 days: 6,0,6,4,5,6,7,8,8
# After  5 days: 5,6,5,3,4,5,6,7,7,8
# After  6 days: 4,5,4,2,3,4,5,6,6,7
# After  7 days: 3,4,3,1,2,3,4,5,5,6
# After  256 days = 26984457539

    return 0
    
if __name__ == "__main__":
    main()