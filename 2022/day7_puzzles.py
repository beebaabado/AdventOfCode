import sys
from deepdiff import DeepDiff

def part1(dir_tree):
   
    if isinstance(dir_tree, int):
      return dir_tree, 0

    size = 0
    total = 0
    for subdir in dir_tree.values():
        s, t = part1(subdir)
        size += s
        total += t
    if size <= 100000:
        total += size
    return (size, total)
   

def part2(dir_tree, totals):
# find directory with smallest size to free up enough disk space
# total size of outmost directory is 44965705
# filesystem size is 70000000
# total size unused space is 70000000 - 44965705  = 25034295
# need at least...4965705  (30000000 - 25034295)
   if isinstance(dir_tree, int):
      return dir_tree, 0

   size = []
   for subdir in dir_tree.values():
      s= part2(subdir, totals)  
      if type(s) is int:
         size.append(s)
      else:
         size += s
      #print("current dir sizes: ", size)
      print("current min ", size[0], sum (size))
      totals[size[0]] = sum(size)
   return (size)

# ----------------------------
def main():
    # args:  script   input    part   "day1_puzzle.py  day1_example.txt  1"    
    
    filename = sys.argv[1]
    lines = open(filename, 'r')
    part = sys.argv[2]

    if part == "1":
      cwd = root = {}  # current working dir, root directory i.e. points to same value 
      dir_stack = []  #represents stack and holds latest cwd on top

      #build directory tree
      for line in lines:
         line = line.strip()
         if line[0] == '$':
            if line[2:4] == "cd":   # if ls ignore
               temp_dir = line[5:]
               if temp_dir == "..":
                  cwd = dir_stack.pop() 
               elif temp_dir == "/":
                  print("At root directory.")
                  cwd = root
                  dir_stack = []
               else:
                  # if temp_dir not in cwd:  # I don't think this code ever gets called because all dirs are added below in else.
                  #   cwd[temp_dir] = {}
                  dir_stack.append(cwd) # save current cwd
                  cwd = cwd[temp_dir]       
                  #print("CWD>>>>>>>>>>", cwd)
         else:  #file list or dir name add to cwd list 
            pos1, pos2 = line.split()
            if pos1 == "dir":  # check dir in cwd
               if pos2 not in cwd:
                  cwd[pos2] = {}
            else:  # store file size 
               cwd[pos2] = int(pos1)
         #print("ROOT: ", root)
      #print("dir_stack: ", dir_stack)   
      #print("ROOT: ", root) 

      print(part1(root))  
      #print (cwd == root) # This is false not the same
      # diff = DeepDiff(cwd, root)
      # diff = DeepDiff(root, cwd) 
      # print(diff)
      
    elif part == "2":
      cwd = root = {}  # current working dir, root directory i.e. points to same value 
      dir_stack = []  #represents stack and holds latest cwd on top

      #build directory tree
      for line in lines:
         line = line.strip()
         if line[0] == '$':
            if line[2:4] == "cd":   # if ls ignore
               temp_dir = line[5:]
               if temp_dir == "..":
                  cwd = dir_stack.pop() 
                  #print("CWD>>>>>>>>>>", cwd)
               elif temp_dir == "/":
                  print("At root directory.")
                  cwd = root
                  dir_stack = []
               else:
                  # if temp_dir not in cwd:  # I don't think this code ever gets called because all dirs are added below in else.
                  #   cwd[temp_dir] = {}
                  dir_stack.append(cwd) # save current cwd
                  cwd = cwd[temp_dir]       
         else:  #file list or dir name add to cwd list 
            pos1, pos2 = line.split()
            if pos1 == "dir":  # check dir in cwd
               if pos2 not in cwd:
                  cwd[pos2] = {}
            else:  # store file size 
               cwd[pos2] = int(pos1)
      #print ("file size:  ", cwd)
      #print("ROOT: ", root)
      t = {}
      size = part2(root, t)
      # print("Part 2: ", x)
      print("TOTALS: ", t)
      print("SUM PART 2: ", sum(size))
      for i in t:
         print(" dir sizes: ",i, t[i])
      t_values = list(t.values())
      min_val = min([v for v in t_values if v >= 4965705])
      print("MIN: ", min_val)
      
    else:
         print("missing part argument")

if __name__=="__main__":
    main()
	
