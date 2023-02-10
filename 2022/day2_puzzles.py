import sys

def part1():
  curr_round = 0
  rounds_total = 0

  # A B C  X Y Z  = Rock Paper Scissors   value 1  2  3
  filename = sys.argv[1]
  opponent = ['A', 'B', 'C']
  player = ['X', 'Y', 'Z']

  lines = open(filename)
  for line in lines:
    count += 1
    opp, me = line.split(' ')
    opp_value = opponent.index(opp.strip()) + 1
    me_value = player.index(me.strip()) + 1
    curr_round = me_value #assume loss
    #Play rock paper scissors
    if ((opp_value == 1 and me_value == 2) or (opp_value == 2 and me_value == 3) or (opp_value == 3 and me_value == 1)):
        curr_round += 6   # I win
        print("WIN")
    elif (opp_value == me_value):
        curr_round += 3   # A Draw
        print("Draw")
      
    print("line: ", count)
    print("current score: ", opp_value, me_value, curr_round)
    rounds_total += curr_round
    print("TOTAL SO FAR: ", rounds_total)


def part2():
  curr_round = 0
  rounds_total = 0

  # A B C  X Y Z  = Rock Paper Scissors   value 1  2  3
  filename = sys.argv[1]
  opponent = ['A', 'B', 'C']
  player = ['X', 'Y', 'Z']

  lines = open(filename)
  for line in lines:
    opp, me = line.split(' ')
    opp_value = opponent.index(opp.strip()) + 1
    me_value = player.index(me.strip()) + 1
    #Play rock paper scissors
    me = me.strip()
    if me == "X":   # need to lose
      print("NEED TO LOSE")
      if opp_value == 3:    #scissors
        me_value = 2	    #paper loses to scissors
      elif opp_value == 2:  #paper
        me_value = 1       # rock loses to paper
      elif opp_value == 1:  #rock
        me_value = 3	    # scissors loses to rock
      curr_round = me_value
    elif me == "Y":
      print("NEED TO DRAW")
      me_value = opp_value   # need a draw
      curr_round = me_value + 3
    elif me == "Z":   # need to win
      print("NEED TO WIN")
      if opp_value == 3:    #scissors
        me_value = 1        #rock  wins over scissors
      elif opp_value == 2:  #paper
        me_value = 3       #scissors wins over paper
      elif opp_value == 1:  #rock
        me_value = 2       #paper wins over rock	
    
      curr_round = me_value + 6

    print("current score: ", opp_value, me_value, curr_round)
    rounds_total += curr_round
    print("TOTAL SO FAR: ", rounds_total)


# ----------------------------
if sys.argv[2] == 1:
  part1()
else:
  part2()
	
