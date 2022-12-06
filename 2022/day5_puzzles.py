import sys
import re

def part1(lines):
  lxl = []
  n=4
  stacks = 0
  num_stacks = 0
  s=[]

  for line in lines:
    if line.strip():
      x = re.sub("\n", "", line)
      inner_list = [(x[i:i+n]).strip() for i in range(0, len(x), n)]
      lxl.append(inner_list)
    else:
      print("EMPTY LINE")
      stacks=lxl.pop()  #remove column numbers
      print("COLS: ", stacks)
      l_x = list(map(list,zip(*lxl)))
      num_stacks = int(stacks.pop())
      print("NUM STACKS:  ", num_stacks) 
      for n in range(num_stacks):
        temp = [el for el in l_x[n] if el.strip()]
        s.append(temp)
      print(s)
      break

  moves = lines.readlines()
  q=0
  f=0
  t=0

  for line in moves:
    print(line)
    move = re.findall(r'\d+',line)
    q = int(move[0])
    f = int(move[1])-1
    t = int(move[2])-1
    print(q,f,t)
    for n in range(q):
      print(s[f][0])
      s[t].insert(0, s[f][0])
      s[f].remove(s[f][0])
      print(s)

    for n in range(num_stacks):
      if (s[n]):
        print(s[n][0])

def part2(lines):
  lxl = []
  n=4
  stacks = 0
  num_stacks = 0
  s=[]

  for line in lines:
    if line.strip():
      x = re.sub("\n", "", line)
      inner_list = [(x[i:i+n]).strip() for i in range(0, len(x), n)]
      lxl.append(inner_list)
    else:
      print("EMPTY LINE")
      stacks=lxl.pop()  #remove column numbers
      print("COLS: ", stacks)
      l_x = list(map(list,zip(*lxl)))
      num_stacks = int(stacks.pop())
      print("NUM STACKS:  ", num_stacks)
      for n in range(num_stacks):
        temp = [el for el in l_x[n] if el.strip()]
        s.append(temp)
      print(s)
      break

  moves = lines.readlines()
  q=0
  f=0
  t=0

  for line in moves:
    print(line)
    move = re.findall(r'\d+',line)
    q = int(move[0])
    f = int(move[1])-1
    t = int(move[2])-1
    print(q,f,t)
    print(s[f][0:q])
    s[t] = s[f][0:q] + s[t]
    print(s)     
    for x in range(q-1, -1, -1):
      print(x,s[f])
      s[f].pop(x)
    print(s)

    for x in range(num_stacks):
      if (s[x]):
        print(s[x][0])



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
	
