import sys

def part1(lines):
  marker = ""
  pos1 = 0
  pos2 = 4
  found = False

  for line in lines:
    print(line)
    while not found:  
      marker = line[pos1:pos2]
      if len(set(marker)) == len(marker):
        found=True 
        print("marker found")
      else:
        pos1 +=1
        pos2 +=1
            
      print(marker)

  print(marker)
  print(pos1, ", ", pos2)

def part2(lines):
  marker = ""
  pos1 = 0
  pos2 = 14
  found = False

  for line in lines:
    print(line)
    while not found:
      marker = line[pos1:pos2]
      if len(set(marker)) == len(marker):
        found=True
        print("marker found")
      else:
        pos1 +=1
        pos2 +=1

      print(marker)

  print(marker)
  print(pos1, ", ", pos2)

# ----------------------------
def main():
    filename = sys.argv[1]
    part = sys.argv[2]
    lines = open(filename, 'r')
    part = sys.argv[2]
    if part == "1":
       part1(lines)
    elif part == "2":
       part2(lines)
    else:
       print("missing part argument")

if __name__=="__main__":
    main()
	
