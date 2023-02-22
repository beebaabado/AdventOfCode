import sys


def part1(grid, grid_x):
   print("Part 1")
   visible = 0
   
   # edges trees are all visible
   visible = len(grid) * 2 + (len(grid_x) - 2) * 2
   print("edge trees: ", visible)

   #ignore edges...all edges visible
   for grid_i, row in enumerate(grid):  # up down
      if grid_i == 0 or grid_i == len(grid)-1:
         continue
      for r_i, value in enumerate(row):  #left right
        if r_i == 0 or r_i == len(row)-1:
          continue
        top = grid_x[r_i][:grid_i]
        bottom = grid_x[r_i][grid_i+1:]
        left = grid[grid_i][:r_i]
        right = grid[grid_i][r_i+1:]
        
        if value > max(top) or value > max(bottom) or value > max(right) or value > max(left):
          visible+=1

   print("Num visible trees: ", visible)
        
def part2(grid, grid_x):
   print("Part 2")
   v_distance = 1
   v_distances = []
   t_count = b_count = l_count = r_count = 0
   # edges trees are all visible
   # visible = len(grid) * 2 + (len(grid_x) - 2) * 2
   # print("edge trees: ", visible)

   #ignore edges...all edges visible
   for grid_i, row in enumerate(grid):  # up down
      if grid_i == 0 or grid_i == len(grid)-1:
         continue
      for r_i, value in enumerate(row):  #left right
        if r_i == 0 or r_i == len(row)-1:
          continue
       # print("row, col, value: ", r_i, grid_i, value) 
        top = grid_x[r_i][:grid_i]
        top.reverse()
        bottom = grid_x[r_i][grid_i+1:]
        left = grid[grid_i][:r_i]
        left.reverse()
        right = grid[grid_i][r_i+1:]
      #   print("t: ", top, ", ", len(top))
      #   print("b: ", bottom, ", ", len(bottom))
      #   print("l: ", left, ", ", len(left))
      #   print("r: ", right, ", ", len(right))

        for tree in top:
          if value > tree:
            t_count +=1
          elif tree >=  value:  # tree height > current tree
            t_count +=1
            break

        for tree in bottom:
          if value > tree:
            b_count +=1
          elif tree >= value:  # tree height > current tree
            b_count +=1
            break
          
        for tree in left:
          if value > tree:
            l_count +=1
          elif tree >= value:  # tree height > current tree
            l_count +=1
            break
          
        for tree in right:
          if value > tree:
            r_count +=1
          elif tree >= value:  # tree height > current tree
            r_count +=1
            break
          
        #print("Scenic Counts: ", t_count, b_count, l_count, r_count)
        v_distances.append(t_count * b_count * l_count * r_count)
        t_count = b_count = l_count = r_count = 0
        #print(v_distances)
   print("Best veiwing distance: ", max(v_distances))

# ----------------------------
def main():
    # args:  script   input    part   "day1_puzzle.py  day1_example.txt  1"    
    
   filename = sys.argv[1]
   f = open(filename, 'r')
   lines = f.readlines() # to be able to get length
   part = sys.argv[2]
   
   grid=[]
   grid_xpose=[[0 for i in range(len(lines))] for j in range(len(lines))]
   
   # data by rows
   for line in lines:
     x = line.strip()
     row = []
     for d in x: 
       row.append(d)
     grid.append(row)
   
   # data by cols
   i = j = 0

   for line in lines:
     x = line.strip()
     for d in x: 
       grid_xpose[j][i] = d
       j+=1
     # set grid indexes for next column  
     i+=1
     j=0

   # print grid to validate
   #print("GRID: ")
   # for r in grid:
   #    r_str = "{}"
   #    print(r_str.format(r))
   # #print("GRID_transposed")   
   # for r in grid_xpose:
   #    r_str = "{}"
   #    print(r_str.format(r))

   if part == "1":
      print(part1(grid, grid_xpose))  
     
   elif part == "2":
      print(part2(grid, grid_xpose))  
   else:
         print("missing part argument")

if __name__=="__main__":
    main()
	
