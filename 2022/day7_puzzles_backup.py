import sys

# # def part1(lines, total, under_100K, r_level, c_dir):
# def part1(lines):
#    print("RECURSION LEVEL: ", r_level)
#    print("total: ", total)
#    print("under_100K: ", under_100K)
#    r_level +=1



#    for line in lines:
#       print("Current line *********: ", line)
#       line = line.strip()
#       if line[0] == '$':
#          if line[2] == "c":
#             if line.find("..")!=-1:
#                t = total[len(total)-1] #t = total.pop() 
#                total[len(total)-2]['size'] += int(t['size'])
#                # t = total[len(total)-1]
#                # total[len(total)-1]['size'] += int(t['size'])
#                print("t: ", t)
#                if t['size'] > 0 and t['size'] <= 100000:
#                   under_100K.append(t)
#                   print("cd .. under_100k: ", under_100K)
#                   return(part1(lines, total, under_100K, r_level, c_dir)) 
#             else:
#                c_dir = line_info[2]      
#                total.append({'dir': c_dir, 'size': 0})
#                print("Added new dir to Total: ", total)
#       elif line_info[0].isnumeric():
#          total[len(total)-1]['size'] += int(line_info[0])
#          print("Updated total ", total)











# def part1(lines, total, under_100K, r_level, c_dir):
def part1(lines):
   



# def part1(lines):
#    root = {}
#    cwd = {}
#    dirs_list = []
#    for line in lines:
#       line = line.strip()
#       if line[0] == "$":
#          if line[2] == 'c':
#             dir = line[5:]
#             if dir == "/":
#                cwd == root
#                dirs_list = []
#             elif dir == "..":
#                cwd = dirs_list.pop()
#             else:
#                if dir not in cwd:
#                   cwd[dir] = {}
#                dirs_list.append(cwd)   
               
               




def part2(lines):
   pass

# ----------------------------
def main():
    # args:  script   input    part   "day1_puzzle.py  day1_example.txt  1"    
    
    filename = sys.argv[1]
    lines = open(filename, 'r')
    part = sys.argv[2]
    if part == "1":
       total_under = 0
       total = []
       under_100k = []
       c_dir=""
       part1(lines, total, under_100k, 1, c_dir)
       print("UNDER: ", under_100k)
       for i in under_100k:
         total_under += i['size']
       print("TOTAL UNDER: ", total_under)
       total_under =0
       for i in total:
         if i['size'] <= 100000:
            total_under += i['size']
       print("TOTAL UNDER #2: ", total_under)

    elif part == "2":
       part2(lines)
    else:
       print("missing part argument")

if __name__=="__main__":
    main()
	
