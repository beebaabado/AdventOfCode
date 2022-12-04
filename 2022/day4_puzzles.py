import sys

def part1(lines):
  count=0
  for line in lines:
    x, y = line.split(",")
    x1, x2 = x.split("-")
    y1, y2 = y.split("-")
    task2 = range(int(y1),int(y2)+1)
    task1 = range(int(x1),int(x2)+1)       
    
    if set(task1) & set(task2) == set(task2) or set(task1) & set(task2) == set(task1):
      count+=1
  print("COUNT: ", count)
  
def part2(lines):
  count=0
  for line in lines:
    x, y = line.split(",")
    x1, x2 = x.split("-")
    y1, y2 = y.split("-")
    task2 = range(int(y1),int(y2)+1)
    task1 = range(int(x1),int(x2)+1)    
    
    if set(task1) & set(task2):
      count+=1
  print("COUNT: ", count)



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
	
