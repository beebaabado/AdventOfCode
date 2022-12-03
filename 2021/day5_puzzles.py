from os import X_OK
from numpy import true_divide
import pandas as pd

def printGrid(gridMap, x,y):
    print("Toxic Map:")
    print(pd.DataFrame(gridMap, index=['']*y, columns=['']*x))

def initInput():
    x1Values = []
    x2Values = []
    y1Values = []
    y2Values = []

    filename="day5_example_input.txt"
    f = open(filename, "r")

    for line in f:
        temp1, temp2 = line.split("->")
        x1, y1 = temp1.strip().split(',')
        x2, y2 = temp2.strip().split(',')
        
        # horizontal and vertical only
        if (x1 == x2) or (y1 == y2):
            x1Values.append(int(x1))
            x2Values.append(int(x2))
            y1Values.append(int(y1))
            y2Values.append(int(y2))
    f.close()  

    tmpl = []
    tmpl.extend(x1Values)
    tmpl.extend(x2Values)
    maxX = max(tmpl) + 1 
    print("maxX: ", maxX)
    tmpl.clear()
    tmpl.extend(y1Values)
    tmpl.extend(y2Values)
    maxY = max(tmpl) + 1
    print("maxY: ", maxY)
    toxicMap = [[ '.' for i in range(maxX)] for j in range(maxY)]
    printGrid(toxicMap, maxX, maxY)
    
    overlap = 0
   
    for idx, (v) in enumerate(x1Values):
        #print("~~~~~~~~~~~~~~~~~`")
        if v == x2Values[idx]:
            if y1Values[idx] < y2Values[idx]:
                y = [*range(y1Values[idx], y2Values[idx] + 1)]
            else:
                y = [*range(y2Values[idx], y1Values[idx] + 1)]
            # print("X: ", v)
            # print("Y values: ", y)
            for i in y:
                if  toxicMap[i][v] == '.':
                    toxicMap[i][v] = 0
                toxicMap[i][v] += 1
                if toxicMap[i][v] == 2:
                    overlap += 1
            
        if y1Values[idx] == y2Values[idx]:
            if x1Values[idx] < x2Values[idx]:
                x = [*range(x1Values[idx], x2Values[idx] + 1)]
            else:
                x = [*range(x2Values[idx], x1Values[idx] + 1)]
            y = y1Values[idx]
            #print("X values: ", x)
            #print("y: ", y1Values[idx])
            for i in x:
                if  toxicMap[y][i] == '.':
                    toxicMap[y][i] = 0
                toxicMap[y][i] += 1
                if toxicMap[y][i] == 2:
                    overlap += 1

    printGrid(toxicMap, maxX, maxY)    
    return overlap
    
def withDiagonals():
    x1Values = []
    x2Values = []
    y1Values = []
    y2Values = []

    filename="day5_input.txt"
    f = open(filename, "r")

    for line in f:
        temp1, temp2 = line.split("->")
        x1, y1 = temp1.strip().split(',')
        x2, y2 = temp2.strip().split(',')
        
        x1Values.append(int(x1))
        x2Values.append(int(x2))
        y1Values.append(int(y1))
        y2Values.append(int(y2))
    f.close()  

    print("X1: ", x1Values)
    print("X2: ", x2Values)
    print("Y1: ", y1Values)
    print("Y2: ", y2Values)

    tmpl = []
    tmpl.extend(x1Values)
    tmpl.extend(x2Values)
    maxX = max(tmpl) + 1 
    print("maxX: ", maxX)
    tmpl.clear()
    tmpl.extend(y1Values)
    tmpl.extend(y2Values)
    maxY = max(tmpl) + 1
    print("maxY: ", maxY)
    toxicMap = [[ '.' for i in range(maxX)] for j in range(maxY)]
    printGrid(toxicMap, maxX, maxY)
    
    overlap = 0
   
    for idx, (v) in enumerate(x1Values):
            print("~~~~~~~~~~~~~~~~~`")
            if x1Values[idx] < x2Values[idx]:
                x = [*range(x1Values[idx], x2Values[idx] + 1)]
            else:
                x = [*range(x2Values[idx], x1Values[idx] + 1)]
                x.reverse()

            if y1Values[idx] < y2Values[idx]:
                y = [*range(y1Values[idx], y2Values[idx] + 1)]
            else:
                y = [*range(y2Values[idx], y1Values[idx] + 1)]
                y.reverse()
            print("Y values: ", y)
            print("X values: ", x)
            if len(x) == 1:
                j= x[0]
                for i in y:
                    if  toxicMap[i][j] == '.':
                        toxicMap[i][j] = 0
                    toxicMap[i][j] += 1
            elif len(y) == 1:
                j = y[0]
                for i in x:
                    if  toxicMap[j][i] == '.':
                        toxicMap[j][i] = 0
                    toxicMap[j][i] += 1
            else:
                for k, (i) in enumerate(x):
                    j = y[k]
                    if  toxicMap[j][i] == '.':
                        toxicMap[j][i] = 0
                    toxicMap[j][i] += 1
    
    printGrid(toxicMap, maxX, maxY)    
    overlap = 0
    for idr, (row) in enumerate(toxicMap):
        for idn, (i) in enumerate(row):
            if toxicMap[idr][idn] == '.':
                pass
            elif toxicMap[idr][idn] >= 2:
                overlap +=1

    
    return overlap
    

def main():
    print("Overlap count: ", initInput())
    print("with diags count: ", withDiagonals())
    return 0
 
if __name__ == "__main__":
  main()    
