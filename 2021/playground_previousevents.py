#example = ["F10", "N3", "F7", "R90", "F11"]

def loadInput(filename, multiVars, sep):
    ''' load input from filename and store in list (array)'''
    f = open(filename, "r")
    input_array = []
    for line in f:
        if multiVars == 0:
            input_array.append(line.strip())  #remove white beg/end white spaces and /n
        else:    
            values = line.strip().split(sep)
            input_array.append(values)  
    f.close() 
    return input_array


def main():

    example = loadInput("playground_previousevents.txt", 0, '')
    print("INPUT: ", example)
    
    north_south  = 0
    east_west  = 0
    north = 0
    south = 0
    east = 0
    west = 0
    heading = "e"
    for direction in example:
        d = direction[0]
        i = int(direction[1:])
        
        if heading == "e":
            if direction in ["R90", "L270"]:
                heading = "s"
            elif direction in ["R180", "L180"]:
                heading = "w"
            elif direction in ["L90", "R270"]:
                heading = "n"

        elif heading == "w":
            if direction in ["R90", "L270"]:
                heading = "n"
            if direction in ["R180", "L180"]:
                heading = "e"
            if direction in ["L90", "R270"]:
                heading = "s"
           
        elif heading == "s":
            if direction in ["R90", "L270"]:
                heading = "w"
            if direction in ["R180", "L180"]:
                heading = "n"
            if direction in ["L90", "R270"]:
                heading = "e"
             
        elif heading == "n":
            if direction in ["R90", "L270"]:
                heading = "e"
            if direction in ["R180", "L180"]:
                heading = "s"
            if direction in ["L90", "R270"]:
                heading = "w"
        
        print("CURRENT HEADING: ", heading)
        print("CURRENT DIRECTION: ", direction)
        if d == "F":
            if heading == "e":
                east += i
                print("EAST : ", east)
            elif heading == "w":
                west += i
                print("WEST: ", west)
            elif heading == "s":
                south += i
                print("SOUTH: ",south)
            elif heading == "n":
                north += i
                print("NORTH: ", north)

        elif d == "N":
                north += i
                print("NORTH : ", north)
        elif d == "S":
                south += i
                print("SOUTH: ", south)
        elif d == "E":
                east += i
                print("EAST : ", east)
        elif d == "W":
                west += i
                print("WEST: ", west)           

    print("Manhattan: ", abs(north - south) + abs(east - west))
    return 0

if __name__ == "__main__":
  main()    