import pandas as pd
import copy


def isBingo(boardByRow, boardByCol):
    wbi = -1

    for idb,(board) in enumerate(boardByRow):
        for row in board:
            #print("board, row: ", idb, " ", row )
            if row.count('*') == 5:
                wbi = idb
                #print("WBI found ", winning_board_index)    
                break

    for idb,(board) in enumerate(boardByCol):
        for row in board:
            if row.count('*') == 5:
                wbi = idb
                #print("WBI found ", winning_board_index)   
                break
    #print("WBI x ", winning_board_index)        
    return wbi

def buildBoards(fname):
    filename=fname
    f = open(filename, "r")
    drawn = f.readline().strip().split(',')
    # pattern to read in boards
    # readline throw away empty line,  read in next 5 lines to array
    f.readline()
    boards_by_row = []
    boards_by_column = []
    count = 1

    for line in f:
        if count == 1:
            board = []
        
        row = line.strip().split()
        board.append(row)
        count += 1    
        if count > 5:
            # skip blank line
            f.readline()
            boards_by_row.append(board)
            # transpose
            temp_df = pd.DataFrame(board, index=['']*5, columns=['']*5).T
            temp_board = temp_df.values.tolist()
            boards_by_column.append(temp_board)
            count = 1
    f.close()  
    return boards_by_row, boards_by_column, drawn




def winningScore():
    filename="day4_input.txt"
    #filename="day4_example_input.txt"
    boards_by_row = []
    boards_by_column = []
    drawn = []

    boards_by_row, boards_by_column, drawn = buildBoards(filename)
    
    # choose first 5 numbers
    drawn_count = len(drawn) + 1
    last_chosen = 0
    winning_board_index = 0

    for i in range(0, drawn_count, 5):
        chosen = drawn[i:i+5]
        print("Numbers chosen: ", chosen)
        #check rows for matches
        for idb,(board) in enumerate(boards_by_row):
            for idr, (row) in enumerate(board):
                for idn, (num) in enumerate(row):
                    if num in chosen:
                        boards_by_row[idb][idr][idn] = '*'
                        boards_by_column[idb][idn][idr] = '*'  #fails with sample data...works if I commnet ths out....
                        #print("Boards with chosen: ", boards_by_row)
                        last_chosen = int(num)
                        
                        # check row counts/ column counts of all boards to see if we have a winner
                        winning_board_index = isBingo(boards_by_row, boards_by_column)
                        if winning_board_index > 0:  
                            for x, (board) in enumerate(boards_by_row):
                                print("Board: ", x)
                                print(pd.DataFrame(board, index=['']*5, columns=['']*5))
                            for y, (board) in enumerate(boards_by_column):
                                print("Board by column: ", y)
                                print(pd.DataFrame(board, index=['']*5, columns=['']*5))    
                            print("WINNING BOARD INDEX: ", winning_board_index)
                            print("Winning board: ", pd.DataFrame(boards_by_row[winning_board_index], index=['']*5, columns=['']*5))
                            print("Last chosen number: ", last_chosen)
                            score = 0
                            # calculate score
                            for row in boards_by_row[winning_board_index]:
                                for num in row:
                                    if num != '*':
                                       score += int(num)  
                            return (score * last_chosen)
  
        #print("Boards with chosen: ", pd.DataFrame(boards_by_row), pd.DataFrame(boards_by_column))

    return 0

def part2WinningScore():
    filename="day4_input.txt"
    boards_by_row = []
    boards_by_column = []
    drawn = []

    boards_by_row, boards_by_column, drawn = buildBoards(filename)
  
    drawn_count = len(drawn) + 1
    last_chosen = 0
    winning_board_index = -1
    winning_boards = []
    win_boards_all = []
    winning_board_snapshot = []
    num_boards = len(boards_by_row)
    
    for i in drawn:
        #check rows for matches
        for idb,(board) in enumerate(boards_by_row):
            for idr, (row) in enumerate(board):
                for idn, (num) in enumerate(row):
                    #if num in chosen:
                    if num == i:
                        #print("[board row number]: [", idb, idr, num, "] ", i )
                        boards_by_row[idb][idr][idn] = '*'
                        boards_by_column[idb][idn][idr] = '*'  #fails with sample data...works if I commnet ths out....
                        if row.count('*') == 5:
                            winning_board_index = idb
                        if boards_by_column[idb][idn].count('*') == 5:
                            winning_board_index = idb
                        #print("WBI found ", winning_board_index)    
                        #print("WBI after isBIngo: ", winning_board_index)
                        if winning_board_index > -1:  
                            if winning_board_index not in winning_boards:
                                winning_boards.append(winning_board_index)
                                win_boards_all.append(copy.deepcopy(boards_by_row[winning_board_index]))
                                winning_board_snapshot = copy.deepcopy(boards_by_row[winning_board_index])
                                last_chosen = int(num)
                              
                                print("Winning boards...tally: ", winning_boards)
                                print("SNAPSHOT: ", pd.DataFrame(winning_board_snapshot, index=['']*5, columns=['']*5))
                                print("LAST DRAWN NUMBER: ", last_chosen)
                            if len(winning_boards) == num_boards:                            
                                print("Winning board index: ", winning_board_index)     
                                print("Winning board: ", pd.DataFrame(boards_by_row[winning_board_index], index=['']*5, columns=['']*5))
                                print("Last chosen number: ", last_chosen)
                                score = 0
                                b = win_boards_all.pop()
                                for row in b:
                                    for num in row:
                                        if num != '*':
                                            score += int(num)  
                                return (score * last_chosen)
                            winning_board_index = -1    
    return 0

def main():

    # # Part 1
    # winning_score = winningScore()
    # print("First Winning score: ", winning_score)

    # Part 2
    winning_score2 = part2WinningScore()
    print("Last Winning score: ", winning_score2)
    return 0  

if __name__ == "__main__":
  main()    