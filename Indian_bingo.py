import random

available = [i for i in range(1, 26)]

# SETTNGS
REMOVED_NUMBER = "█"  # "֍"  "•"  "Ø"
SHOW_COMPUTER_BOARD = False  # see how computer play.


def intro():
    # simple intro.
    print("       << WELCOME TO >>       ")
    print("+----------------------------+")
    print("|   B    I    N    G    O    |")
    print("+----------------------------+")

    if input("need 'instructions' (y/n): ") == "y":
        instructions()


def instructions():
    instruction = """

    Bingo is a 2 player game which has so many versions.The instructions for this version are   
given below :-

1. Create a board with  5 rows and 5 columns which have numbers from 1-25 placed randomly.
   Note:
    each player must hide their board through out the game until finish
    player1's board may or may not be same as player2's board
    
2. player1 will tell a number which is not marked in the board,
   then both players mark that number in their board.

3. then, player2 will tell a number which is not marked in the board,
   then both players mark that number in their board.

4. repeat 2 and 3 until some one wins

5. if every number in a row or column or diagonal is marked,player get a point 
   which is represented as 'B I N G O'
   eg:-
     given board =
        [
            ["█", "█", "█", "█", "█"],
            [13 , 15 , 20 , "█", "█" ],
            [11 , 12 , "█", 14 , "█"],
            [16 , "█", 18 , 19 , "█"],
            ["█", 22 , 23 , 24 , "█"],
        ]
    Here, player with this board gets 3 points(1 row, 1 col, 1 diagonal)
    which is represented as 'B I N'
    
6. "Whoever gets 5 points AKA 'B I N G O' first WINS"
    ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
    """
    print(instruction)
    input("Press Enter to continue :)")
    print()


def create_board():
    # create a 2D board to play

    # 1. create an array of 1-25 numbers : nums
    # 2. create a 2D array, initialize it with 0s : board
    # 3. iterate below steps 25 times (2 for loops 5x5)
    #  3.1. randomly select one number from nums : x
    #  3.2. put it in board
    #  3.3. remove the x from the nums so that we don't select same number again
    # 4. return board : a 2D array contains randomly placed numbers from 1-25 without repetition

    nums = [i for i in range(1, 26)]
    board = [[0 for _ in range(5)] for _ in range(5)]

    for i in range(5):
        for j in range(5):
            x = random.choice(nums)
            board[i][j] = x
            nums.remove(x)

    return board


def print_board(board):
    # print the 2D board
    print('+----------------------------+')

    for i in range(5):
        for j in range(5):
            sp = ' ' if (len(str(board[i][j])) < 2) else ''  # to make the board alignment correct
            print(f'| {board[i][j]}{sp} |', end='')

        print('')
        print('+----------------------------+')


def player_board():
    # create a board for player

    # 1.inside an infinite loop
    #  1.1. create a player board using create_board() : plyr_board
    #  1.2. shows the plyr_board to player/user
    #  1.3. ask if user likes it
    #  1.4. if yes we return the plyr_board, else we repeat step 1 again

    print("Please select a board : ")
    while True:
        plyr_board = create_board()
        print_board(plyr_board)
        x = input('you like it? (y/n) :')
        if x == 'y':
            return plyr_board


def find_key_mark(b1, b2, key):
    # marking number selected by players in both tables
    for i in range(5):
        for j in range(5):
            if b1[i][j] == key:
                b1[i][j] = REMOVED_NUMBER

            if b2[i][j] == key:
                b2[i][j] = REMOVED_NUMBER


def ask_player():
    # ask player for a number to mark
    print()
    while True:
        x = input("Player   : ")
        if x.isdigit() and int(x) in available:
            available.remove(int(x))
            return int(x)


def ask_computer(computer_b):
    # ask computer for a number to mark

    # ------------------------------------------------------
    # 1.EASY (select a random number from available numbers)

    # x = random.choice(available)
    # available.remove(x)
    # return x
    # ------------------------------------------------------

    # 2.MEDIUM (calculate a score for every element return best number)

    """
    ============================================================================
    WE TRY TO RETURN THE BEST POSSIBLE NUMBER/MOVE FROM THE GIVEN BOARD.

    1. if middle number is not marked :

       return number in the middle(computer_b[2][2]) of the board
       as 'first move' to improve chances.

    2. if middle number is already marked :

       we check if any row/column contains 4 "█"(or REMOVED_NUMBER)
       if yes return the 5th number
       eg :-
        ["█",3,"█","█","█"]  --> return 3

    3. if middle number is already marked and there is no row/column
       contains 4 "█"(or REMOVED_NUMBER) :

       we calculate a score for every number in the board
       and return the number with high score

       eg:-
       given board =
        [
            [1, "█", "█", 4, 5],
            [6, "█", "█", "█", 10],
            [11, 12, 13, 14, "█"],
            [16, 17, 18, 19, "█"],
            [21, 22, 23, 24, "█"],
        ]

        here 10 is best option,
        [
            [  ,   ,    ,    , 5  ],
            [6 ,"█", "█", "█", 10 ],
            [  ,   ,    ,    , "█"],
            [  ,   ,    ,    , "█"],
            [  ,   ,    ,    , "█"],
        ]

        no. of "█"(or REMOVED_NUMBER) in the row of 10 = 3
        no. of "█"(or REMOVED_NUMBER) in the col of 10 = 3

        Total no. of "█"(or REMOVED_NUMBER) corresponding 10 = 3+3 = 6
        Total no. of number spaces corresponding 10 = 9
          --> [6 ,"█", "█", "█", 10 ] row corresponding 10
          --> [5 , 10, "█", "█", "█"] column corresponding 10
          --> total 9 number spaces(number 10 exist in both row and col)

        score calculation for number 10 = 6/9 = 0.6666666666666666
        (this score is the best when comparing with the score of other numbers)
    ============================================================================
    """

    # -------------------------------------
    def score(x, p, q):
        # score calculation for computer
        count = 0
        for k in range(5):
            if x[k][q] == REMOVED_NUMBER:
                count += 1
            if x[p][k] == REMOVED_NUMBER:
                count += 1
        return count / 9

    # -------------------------------------

    # cross the middle element as first move to improve chances
    if computer_b[2][2] in available:
        return computer_b[2][2]

    else:

        # 1.check for any rows/cols have 4 "█"(or REMOVED_NUMBER) if yes select the 5th number
        y = [[computer_b[j][i] for j in range(5)] for i in range(5)]

        for i in range(5):
            if (computer_b[i].count(REMOVED_NUMBER)) == 4:
                for j in range(5):
                    if computer_b[i][j] != REMOVED_NUMBER:
                        return computer_b[i][j]

            if (y[i].count(REMOVED_NUMBER)) == 4:
                for j in range(5):
                    if y[i][j] != REMOVED_NUMBER:
                        return y[i][j]

        # 2.if there is no row which have 4 "█"(or REMOVED_NUMBER)
        # we will return best number by calculating the high_score
        high_score = -1
        best = -1

        for i in range(5):
            for j in range(5):

                if computer_b[i][j] == REMOVED_NUMBER:
                    continue

                temp = score(computer_b, i, j)

                if temp >= high_score:
                    high_score = temp
                    best = computer_b[i][j]

        # print(high_score, best)

        return best


def check_bingo(b):
    # if every element in the row/column == REMOVED NUMBER: increment count

    count = 0
    # row
    for i in range(5):
        if all([spot == REMOVED_NUMBER for spot in b[i]]):
            # print("row")
            count += 1

    # column
    column = [[b[i][j] for i in range(5)] for j in range(5)]
    for i in range(5):
        if all([spot == REMOVED_NUMBER for spot in column[i]]):
            # print("column")
            count += 1

    # # diagonals (not considered in bingo at my school :))

    diagonal1 = [b[i][i] for i in range(5)]
    if all([spot == REMOVED_NUMBER for spot in diagonal1]):
        # print("dia1")
        count += 1

    diagonal2 = [b[i][5 - i - 1] for i in range(5)]
    if all([spot == REMOVED_NUMBER for spot in diagonal2]):
        # print("dia2")
        count += 1

    return count


def print_bingo(index):
    # print bingo according to the count in check_bingo()
    BINGO = "BINGO"

    if index <= 0:
        pass
    else:
        if index >= 5:
            index = 5

        print('+----------------------------+')

        print("| ", end=" ")
        for i in range(index):
            print(f"{BINGO[i]}   ", end=" ")
        print(" |", end="")

        print('\n+----------------------------+')


def print_all_boards(player_b, count_p, computer_b, count_c, player_first=True):
    # print all boards

    if player_first:
        print("      -- PLAYER BOARD --")
        print_bingo(count_p)
        print_board(player_b)

        print("     -- COMPUTER BOARD --")
        print_bingo(count_c)
        print_board(computer_b)

    else:
        print("     -- COMPUTER BOARD --")
        print_bingo(count_c)
        print_board(computer_b)

        print("      -- PLAYER BOARD --")
        print_bingo(count_p)
        print_board(player_b)


def main():
    # create boards for computer and player
    computer_b = create_board()
    player_b = player_board()

    while True:

        # PLAYER
        player_n = ask_player()

        # AUTOMATION -> Computer vs Computer

        # player_n = ask_computer(player_b)
        # available.remove(player_n)
        # print(f"\nplayer   : {player_n}")

        find_key_mark(player_b, computer_b, player_n)

        count_p = check_bingo(player_b)
        count_c = check_bingo(computer_b)

        if count_p >= 5:
            print("\n@@@@@@@ PLAYER WON @@@@@@@\n")
            print_all_boards(player_b, count_p, computer_b, count_c, player_first=True)
            break

        if count_c >= 5:
            print("\n@@@@@@@ COMPUTER WON @@@@@@@\n")
            print_all_boards(player_b, count_p, computer_b, count_c, player_first=False)
            break

        # COMPUTER
        computer_n = ask_computer(computer_b)
        print(f"Computer : {computer_n}\n")

        # removing that number from available to prevent user say the same number again.
        available.remove(computer_n)

        find_key_mark(computer_b, player_b, computer_n)

        count_c = check_bingo(computer_b)
        count_p = check_bingo(player_b)

        if count_c >= 5:
            print("\n@@@@@@@ COMPUTER WON @@@@@@@\n")
            print_all_boards(player_b, count_p, computer_b, count_c, player_first=False)
            break

        if count_p >= 5:
            print("\n@@@@@@@ PLAYER WON @@@@@@@\n")
            print_all_boards(player_b, count_p, computer_b, count_c, player_first=True)
            break

        # --
        print("      -- PLAYER BOARD --")
        print_bingo(count_p)
        print_board(player_b)

        if SHOW_COMPUTER_BOARD:
            print("     -- COMPUTER BOARD --")
            print_bingo(count_c)
            print_board(computer_b)


if __name__ == '__main__':
    intro()
    main()
