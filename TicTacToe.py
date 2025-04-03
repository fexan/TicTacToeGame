''' 
Author: Ifeoluwa Oyelowo-Paul
Date: Feb 26, 2025
TIC TAC TOE GAME
Requirements: 
- 2 players should be able to play the game (both sitting at the same computer)
- The board should be printed out every time a player makes a move
- Game accepts input of the player position (see position board below) and then place a symbol on the board
 1|2|3
 4|5|6
 7|8|9
 
'''


#Get valid input from players
def valid_input(board): #passing board as param to avoid duplicate entries
    #Variables
    choice = 'initial'
    accepted_values = range(1,10) #1-9
    within_range = False #to track if input is within range
    filled_cell = False #to track if cell is already filled and avoid overwriting cells
    
    #Ask user for valid input - must be a digit and in the acceptable range
    while not choice.isdigit() or not within_range or not filled_cell:
        
        choice = input('Enter a position to play your turn(1-9): ')

        if not choice.isdigit():
            print("Input is not a digit. Try again")
            continue #no need to go to rest of loop. Go to start of loop

        #error message for invalid range
        if int(choice) not in accepted_values:
            print('Input is out of range. Try again.')
        else: 
            within_range = True

        #error message if input has already been entered before
        if board[choice] != '':
            print('The cell has been filled. Try again')
        else:
            filled_cell = True
        

    return int(choice) #return integer version of input


#Accept input of the player position and place the symbol on the board 
#pass the current game board, position to be updated and value to be played as parameters
#return the updated game board
def update_board(curr_board, player_position, value):
    #we will send player_position as an int so cast to a string
    curr_board[str(player_position)] = value
    return curr_board


#Print game board
#pass the game board as a parameter and print
def print_board(board):
    print(
     f'''
      {board['1']:2s} |  {board['2']:2s} |  {board['3']:2s}
    -----------------
      {board['4']:2s} |  {board['5']:2s} |  {board['6']:2s}
    -----------------
      {board['7']:2s} |  {board['8']:2s} |  {board['9']:2s}

    '''   
    )

#Determine if there is a win or tie
def gameover(board):
    #these are all position positions that could result in a win
    #there is likely a more efficient way to do this

    #horizonal wins - also checking that cells are not empty as cells will be equal to each other then
    hor1 = (board['1']==board['2']==board['3'] and '' not in (board['1'],board['2'],board['3'])) 
    hor2 = (board['4']==board['5']==board['6'] and '' not in (board['4'],board['5'],board['6'])) 
    hor3 = (board['7']==board['8']==board['9'] and '' not in (board['7'],board['8'],board['9'])) 
    #vertical wins
    ver1 = (board['1']==board['4']==board['7'] and '' not in (board['1'],board['4'],board['7'])) 
    ver2 = (board['2']==board['5']==board['8'] and '' not in (board['2'],board['5'],board['8']))  
    ver3 = (board['3']==board['6']==board['9'] and '' not in (board['3'],board['6'],board['9'])) 
    #diagonal wins
    diag1 =  (board['1']==board['5']==board['9'] and '' not in (board['1'],board['5'],board['9'])) 
    diag2 = (board['3']==board['5']==board['7'] and '' not in (board['3'],board['5'],board['7'])) 

    #all cells filled. it is a tie
    tie = '' not in board.values()

    return hor1 or hor2 or hor3 or ver1 or ver2 or ver3 or diag1 or diag2 or tie


#Ask players if they want to play the game again
def play_again():
    response = input('Will you like to play again?(Y/N)? ')

    while response.upper() not in ('Y','N'):
        response = input("Answer Y/N depending on if you'll like to try again. ")

    if response.upper() == 'Y':
        return True
    else:
        return False
    
    

#Put everything together.
def tic_tac_toe():
    print("Welcome to the TIC TAC TOE game!")

    #Variables
    gameboard = {'1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':''}
    another_round = True #used to track if players want to play again
    
    #values for player 1 and 2 expecting 'x' or 'o'
    player1_val = 'i' 
    player2_val = 'j' 

    #player 1 and 2 position variables with values btw 1 and 9
    player1_pos = 0 
    player2_pos = 0 
    
    #Ask player 1 if they will be x or o
    player1_val = input("Will Player 1 be x or o? ")
    while player1_val.lower() not in ('x','o'):
        player1_val = input("Answer x/o depending on what player1 will like to be: ")
    player1_val = player1_val.lower()

    if player1_val == 'x':
        player2_val = 'o'
    else:
        player2_val = 'x'
 
    #game over when someone wins or there is a tie and we don't want another round
    #continue looping if game is not over and we want another round
    while not gameover(gameboard) and another_round:


        #player 1 should play
        player1_pos = valid_input(gameboard)

        #update game board
        gameboard = update_board(gameboard,player1_pos,player1_val)

        #print board
        print_board(gameboard)

        #did player 1 win or is it a tie?
        if gameover(gameboard):
            print('Congratulations! Player1 has won the game! or it is a tie.')
             #Ask players if they want to play the game again
            another_round = play_again()
            #continue #go to start of loop
            if another_round: #reset gameboard
                gameboard = {'1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':''}

        else:
            #player 2 should play
            player2_pos = valid_input(gameboard)

            #update game board
            gameboard = update_board(gameboard,player2_pos,player2_val)

            #print board
            print_board(gameboard)

            #did player 2 win or is it a tie?
            if gameover(gameboard):
                print('Congratulations! Player2 has won the game! or it is a tie.')
                #Ask players if they want to play the game again
                another_round = play_again()
                #continue #go to start of loop
                if another_round: #reset gameboard
                    gameboard = {'1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':''}
               
       
    


    #When we break out of while loop, we don't want another round
    print("Hope you enjoyed the game. Play again soon!")


        

#gameboard = {'1':'','2':'','3':'x','4':'','5':'','6':'0','7':'','8':'','9':''}
#valid_input(gameboard)
        
tic_tac_toe()


