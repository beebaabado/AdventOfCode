import statistics as st

def part1(positions):
   # this one works with median  
   fuel = 0
   x_med = st.median(positions)
   for x in positions:
      fuel += abs(x - x_med)
   #print(fuel)    
   return fuel

def part2(positions):
   least_fuel = float("inf")
   x_med = st.median(positions)
   x_avg = round(st.mean(positions))
   print("avg: ", x_avg)
   diffs = 0
   sorted_positions = positions.copy()
   sorted_positions.sort()
   
   # compare position to all other positions to get differences and then sum up those differences 
   # grab the min value of all the sums  This method does not seem to work for example code.
   # if use average of positions the and then do abs(pos - avg)  gets the right answer for example input
   for p in sorted_positions:
      diffs = [abs(pos - x_avg) for pos in positions]  #this works for example input
      diffs = [abs(p - pos) for pos in positions]  # this works for my input
      #print("DIFF: ", diffs)
      # e.g.  11 + 10 + 9 + ... + 1
      sums = [(diff * (diff + 1))/2 for diff in diffs]
      #print("SUM: ", sum(sums))
      least_fuel = min(least_fuel, sum(sums)) 
   
   return least_fuel

def main():

    file_example = [16,1,2,0,4,2,7,1,2,14]
    file_my = "day7_input.txt"
    #part 1    my answer:  351901.0
   

    #part 2   my answer:   101079875.0
    positions = []
    f=open(file_my)
    line = f.readline().strip().split(',')
    f.close()
    positions = [int(num) for num in line]
    #print(positions)
    
    #part1
    fuel_count = part1(file_example) 
    print("Example Part 1 least fuel", fuel_count)
    fuel_count = part1(positions) 
    print("Part 1 least fuel", fuel_count)
    fuel_count = part2(file_example)
    print("Example Part 2 least fuel", fuel_count)
    fuel_count = part2(positions)
    print("Part 2 least fuel", fuel_count)

    return 0
    
if __name__ == "__main__":
    main()