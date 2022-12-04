import sys
import string

def part1(lines):

    priorities = []
    alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    print(alphabet)

    for line in lines:
    # find center of list and split
    # find common value in each side
       sack = line.strip()  #remove newline
       x = len(sack)
       print("******************************* len = ", x)
       c1 = sack[:x//2]
       c2 = sack[(x//2):]
       #print(sack)
       #print(c1)
       #print(c2)
       
       comm_c = list(set(c1) & set(c2))[0] 
       print(comm_c)
       priority = alphabet.index(comm_c) + 1
       print("PRIORITY: ", priority)
       priorities.append(priority)
       print("Priorty: ", comm_c, ", ", priority)
       
    sum = 0
    for priority in priorities:
      sum = sum + priority
    print("SUM: ", sum)
              
def part2(lines):

    priorities = []
    alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    print(alphabet)
    
    while True:
    # find center of list and split
    # find common value in each side
       
       try:
       	 sack1 = lines.readline().strip() #remove spaces or endlines
         sack2 = lines.readline().strip()
         sack3 = lines.readline().strip()
       
         print(sack1)
         print(sack2)
         print(sack3)
     
         comm_c = list(set(sack1) & set(sack2) & set(sack3))[0]
         print(comm_c)
         priority = alphabet.index(comm_c) + 1
         print("PRIORITY: ", priority)
         priorities.append(priority)
         print("Priorty: ", comm_c, ", ", priority)
       except:
         break;

    sum = 0
    for priority in priorities:
      sum = sum + priority
    print("SUM: ", sum)

# ----------------------------
def main():
    filename = sys.argv[1]
    part = sys.argv[2]
    lines = open(filename)
    part = sys.argv[2]
    if part == "1":
       part1(lines)
    elif part == "2":
       part2(lines)
    else:
       print("missing part argument")

if __name__=="__main__":
    main()
	
