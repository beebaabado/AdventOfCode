import matplotlib.pyplot as plt
import numpy as np


def holdingArea():
     # with example input
    x=[]
    y=[]
    for i in [*range(5, 81, 5)]:
        x.append(i)
        y.append(hatchery(i,file_example))
        #print("{}".format(i), hatchery(i,file_example))

    # WRONG!!!!!!!!!!!
   # a = np.polyfit(np.log(x), y, 1)
    # a = np.polyfit(x, y, 1)
    # print("polyfit: ", a)
    # # y = A + Blogx , x = 256
    # for i in x:
    #     curve = a[1] + a[0]*np.log(x)
    #     print("curve {} {}: ".format(i, curve))  

    # the shape of the data suggests a 2d polynomial, so begin there
    # a, b, c are the polynomial coefficients: ax^2 + bx + c
    a, b = np.polyfit(x, y, 1)
    y_pred = np.polyval([a, b], x)    # y_pred refers to predicted values of y

    # how good is the fit?
    # calculate MSE:
    MSE = np.sqrt( np.sum((y_pred-y)**2)/10 )
    print("MSE: ", MSE)
    # MSE = .2

    # now use the model polynomial to generate y values based on x values outside 
    # the range of the original data:
    x_out = x.append([100, 150, 200, 250, 256])  # choose 20 points, 10 in, 10 outside original range
    y_pred = np.polyval([a, b], x_out)

    # now plot the original data points and the polynomial fit through them
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(x, y, 'g.', x_out, y_pred, 'b-' )

    plt.grid(True)  
    # x = [5, 10,15,20,50,80]
    # y = [578, 833, 1200, 2215, 29228, 390923]
    plt.xlim(0, 275)
    # plt.plot(x, y, alpha = 0.4, label ='Y = X²',
    #      color ='red', linestyle ='dashed',
    #      linewidth = 2, marker ='D',
    #      markersize = 5, markerfacecolor ='blue',
    #      markeredgecolor ='blue')
    plt.show()     
    
    # with my input  function will not return if days too big for initial data set
    x=[]
    y=[]
    for i in [*range(5, 81, 5)]:
        x.append(i)
        y.append(hatchery(i,file_my))
        #print("{}".format(i), hatchery(i,file_my))
        
    # x = [5, 10,15,20,50,80]
    # y = [578, 833, 1200, 2215, 29228, 390923]
    # WRONG!!!!!!!!!!!
    # a = np.polyfit(x, y, 1)
    # print("polyfit: ", a)
    # # y = A + Blogx , x = 256
    # for i in x:
    #     curve = a[0] + a[1]*np.log(x)
    #     print("curve {} {}: ".format(i, curve))
    
    # plt.xlim(0, 275)
    # plt.plot(x, y, alpha = 0.4, label ='Y = X²',
    #      color ='red', linestyle ='dashed',
    #      linewidth = 2, marker ='D',
    #      markersize = 5, markerfacecolor ='blue',
    #      markeredgecolor ='blue')     
    # plt.show()     
    
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

def genCount():
    pass

def main():

    file_example = "day6_example_input.txt"
    file_my = "day6_input.txt"
    #part 1    

    # print("Grow the school of lantern fish: ", hatchery(80,file_example))
    # print("Grow the school of lantern fish: ", hatchery(80,file_my))
    
    #part 2 
    school = []
    f=open(file_example)
    line = f.readline().strip().split(',')
    f.close()
    school = [int(num) for num in line] 
    print(x)    

    for fish in school:   
        gen1 = (fish - 1) + 2
    
    return 0
    
if __name__ == "__main__":
    main()