# DAY 1
from typing import final


def getGreaterCount():
    count_greater = 0
    prev = 0
    f = open("day1_puzzle1_input.txt", "r")
    prev = f.readline()  
   # print("prev (line1): ", prev)
    for x in f:
        #print("VALUE: ", x)
        #print(prev, x)
        if int(x) > int(prev):
            count_greater += 1    # increment count if number greater than previous
            #print("YES, it is greater: ", count_greater)
        prev = x
        #print ("Prev:", prev)
    #print("Counter: ", count_greater)
    f.close
    
    return count_greater

def getGreaterSumsCount():
    count_greater = 0
    prev = 0
    values=[]
     # move values into array
    f = open("day1_puzzle1_input.txt", "r")
    for value in f:
        values.append(int(value))
    f.close()
    #print("Values:", values)
    #print("Values length: ", len(values))
    # sum first three values, prev
    for x in range(0, 3):
        prev += values[x]
    #print("Prev sum: ", prev)
    
    sums_array = []
    size = len(values)
    # loop through and compare sums of threes starting at each index
    for i in range (1, size):
        # print("-----------------")
        # print("Index: ", i)
        if (i + 3) <= size:
            sum = 0
            for x in range( i, i + 3):
                sum += values[x]   
        # print("PREV: ", prev)
        # print("SUM: ", sum)        
        if sum > prev:
            count_greater +=1
        prev = sum  
    return count_greater

# Day 2
def getPosition(): 
   horizontal = 0
   depth = 0

   f = open("day2_input.txt", "r")
   for line in f:
       p, v = line.strip().split(' ')
    #    print(p)
    #    print(v)
       v = int(v)
       if p == "forward":
          horizontal += v
       elif p == "down":
           depth += v
       elif p == "up":
           depth -= v

#    print("horizontal: ", horizontal)
#    print("depth: ",depth)    
   position = horizontal * depth
   return position


def getAimPosition(): 
   horizontal = 0
   depth = 0
   aim = 0

   f = open("day2_input.txt", "r")
   for line in f:
       p, v = line.strip().split(' ')
    #    print(p)
    #    print(v)
       v = int(v)
       if p == "forward":
          horizontal += v
          depth += aim * v
       elif p == "down":
           #depth += v
           aim += v
       elif p == "up":
           #depth -= v
           aim -= v

#    print("horizontal: ", horizontal)
#    print("depth: ",depth) 
#    print("aim: ", aim)
   position = horizontal * depth
   f.close()
   return position


# Day 3
def getGamma(length):
    f = open("day3_input.txt", "r")

    line_count = 0
    for line in f:
        if line != "\n":
            line_count += 1
    
    f.seek(0)
    binary_len = length
    # print("line count: ", line_count)
    # print("length of binary: ", binary_len)
    gamma_bit_counts_1 = [0] * binary_len
    gamma = list('000000000000')

    for x in f:
       b = str(x)
       for i in range (0, binary_len):
           if (b[i] == "1"):
               gamma_bit_counts_1[i] += 1
    f.close()

    for i in range (0, binary_len):
        if gamma_bit_counts_1[i] >  line_count/2:
           gamma[i]='1'
        else: 
           gamma[i]='0'

    print("Gamma: ", "".join(gamma))    
    return "".join(gamma)

def getEpsilon(gamma, length):
    
    gamma_list = list(gamma)
    epsilon_list = list('000000000000')
    for i in range(0, length):
        if gamma_list[i] =='0':
            epsilon_list[i] = '1'
        else:
            epsilon_list[i] = '0'
     
    print("Epsilon: ", "".join(epsilon_list))    
    return "".join(epsilon_list)   
    
def getPower(length):
    gamma = getGamma(length)
    epsilon = getEpsilon(gamma, length)
    return int(gamma, base=2) * int(epsilon, base=2)

def commonValue(num_array, num_array_len, bit_position, mode):
    bit_count = 0
    for num in num_array:
        if mode == 1:
            if (num[bit_position] == "1"):
                bit_count += 1
            if bit_count >= num_array_len/2:
                common_value = '1' 
            else:
                common_value = '0'   
        
        if mode == 0:
            if (num[bit_position] == "0"):
                bit_count += 1
            if bit_count <= num_array_len/2:
                common_value = '0' 
            else:
                common_value = '1'          
    return common_value

# def bitCounts(num_array, length):    
#     bit_counts_1 = [0] * length
#     for num in num_array:
#        for i in range (0, length):
#            if (num[i] == "1"):
#                bit_counts_1[i] += 1
#     return bit_counts_1

def removeValues(num_array, num_array_len, length, position, mode):
    modified_num_array = num_array.copy()
    #print("----------Iter ", position)
    if num_array_len == 1:
         return modified_num_array
    else:
        value = commonValue(modified_num_array, num_array_len, position, mode) 
        newlist = [num for num in num_array if num[position] == value]
        position +=1
        #print("newlist: ", newlist)
        return removeValues(newlist, len(newlist), length, position, mode)  

def getRating(length, input, mode):
    input_array = input.copy()
    final_array = removeValues(input_array, len(input_array), length, 0, mode)
    return final_array[0]   # should only be 1 value left

def getLifeSupportRating(length, input):
    return int(getRating(length, input, 1), base=2) * int(getRating(length, input, 0), base=2)

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
    
    print("~~~~~~Day 1~~~~~~~")
    count = getGreaterCount()
    print("Greater: ", count)
    count2 = getGreaterSumsCount()
    print("GreaterSums: ", count2)

    print("~~~~~Day 2~~~~~")
    filename = "day2_input.txt"
    input = loadInput(filename, 2, ' ')
    #print("Day 2 input: ", input)
    position = getPosition()
    print("Position: ", position)
    positionAim = getAimPosition()
    print("Aim Position: ", positionAim)
    
    print("~~~~~Day 3~~~~~")
    power = getPower(12)
    print("Power: ", power)
    filename = "day3_input.txt"
    input = loadInput(filename, 0, '')
    lifeRating=getLifeSupportRating(12, input)
    print("Life support rating: ", lifeRating)

if __name__ == "__main__":
  main()