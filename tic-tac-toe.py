#Tic Tac Toe

import random
import pyttsx3
engine = pyttsx3.init(driverName='sapi5')
import speech_recognition as sr
r = sr.Recognizer()



numbers = {'one': 1,'on':1, 'too':2, 'to':2, 'two': 2, 'three': 3,'tree':3, 'four':4,'for':4, 'fore':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

def drawBoard(board):
    #this function prints out the board that it was passed

    #"board is a list of 10 strings representing the board(ignore index 0)"
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    #lets the player type which letter they want to be.
    #returns a list with the player's letter as the first item, and 2nd as computer
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        engine.say('Do you want to be X or O?')
        engine.runAndWait()
        try:
            with sr.Microphone() as source:
                user_input = r.listen(source)
                text = r.recognize_google(user_input)
                print(text)
                if text[0].lower() == 'x' or text[0].lower() == 'o':
                    letter = text[0].upper()
        except:
            print('Sorry but we couldn\'t hear you. Please try via keyboard')
            engine.say('Sorry but we couldn\'t hear you. Please try via keyboard')
            engine.runAndWait()
            letter = input().upper()

        #the first element in the list id the player's letter, the second is the computer's letter
        if letter == 'X':
            return ['X', 'O']
        elif letter == 'O':
            return ['O', 'X']

def whoGoesFirst():
    #randomly choos the player who goes first.
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    #this function returns true if the player wamts to play again, otherwise it returns false
    print('Do you want to play again? (yes or no)')
    engine.say('Do you want to play again? (yes or no)')
    engine.runAndWait()
    try:
        with sr.Microphone() as source:
            user_input = r.listen(source)
            text = r.recognize_google(user_input)
            print(text)
            if text == 'yes':
                return True
            elif text[0].lower == 'y':
                return True
            elif text == 'no':
                return False
            elif text[0].lower == 'n':
                return False
            else:
                raise ValueError
    except:
        print('Sorry but we couldn\'t hear you. Please try via keyboard')
        engine.say('Sorry but we couldn\'t hear you. Please try via keyboard')
        engine.runAndWait()
        return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinnner(bo, le):
    #givven a board and a player's letter, this function returns true if that player has won
    #here i used bo instead of board and le instead of letter
    return ((bo[7]== le and bo[8]== le and bo[9]== le) or
            (bo[4]== le and bo[5]== le and bo[6]== le) or
            (bo[1]== le and bo[2]== le and bo[3]== le) or
            (bo[7]== le and bo[4]== le and bo[1]== le) or
            (bo[8]== le and bo[5]== le and bo[2]== le) or
            (bo[9]== le and bo[6]== le and bo[3]== le) or
            (bo[7]== le and bo[5]== le and bo[3]== le) or
            (bo[9]== le and bo[5]== le and bo[1]== le))

def getBoardCopy(board):
    #make a duplicate of the board list and return its duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    #returns true if space is free
    return board[move] == ' '

def getPlayerMove(board):
    #let the player type in their move.
    move = 0
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('what is your next move? (1-9)')
        engine.say('what is your next move? say number from 1 to 9')
        engine.runAndWait()
        try:
            with sr.Microphone() as source:
                user_input = r.listen(source)
                text = r.recognize_google(user_input)
                print(text)
            if text in 'one on two too to three tree four for fore five six seven eight nine'.split():
                move = str(numbers[text])
            elif 0 < int(text) < 10:
                move = str(int(text))
            else:
                raise NameError
        except:
            print('Sorry but we couldn\'t hear you. Please try via keyboard')
            engine.say('Sorry but we couldn\'t hear you. Please try via keyboard')
            engine.runAndWait()
            move = input()
    return int(move)

def chooseRandomMoveFromList(board, moveList):
    #returns a valid move from the passed list on the passed board.
    #returns none if there is no valid move
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    #given a board and the computer's letter
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    #here is algorithm for our tic tac toe AI
    #first check if we can win in next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinnner(copy, computerLetter):
                return i

    #check if the player can win in their next move, and block them
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinnner(copy, playerLetter):
                return i

    #try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    #rtry to take center if it is free
    if isSpaceFree(board, 5):
        return 5

    #move on one of the sides.
    move = chooseRandomMoveFromList(board, [2, 4, 6, 8])
    if isBoardFull(theBoard):
        drawBoard(theBoard)
        print('The game is Tie!!')
        engine.say('The game is Tie!')
        engine.runAndWait()
    else:
        if move != None:
            return move

def isBoardFull(board):
    #return true if every space on the bord has been taken otherwise return false
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe')
engine.say('Welcome to Tic Tac Toe')
engine.runAndWait()
while True:
    #Reset the board
    theBoard = [' '] * 20
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    engine.say('The ' + turn + ' will go first.')
    engine.runAndWait()
    gameisPlaying = True

    while gameisPlaying:
        if turn == 'player':
            #player's turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinnner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray!! You have won the game!')
                engine.say('Hooray! You have won the game')
                engine.runAndWait()
                gameisPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is Tie!!')
                    engine.say('The game is Tie!')
                    engine.runAndWait()
                    break
                else:
                    turn = 'computer'

        else:
            #computer's turn
            move = getComputerMove(theBoard, computerLetter)
            if move == None:
                for i in range(1, 10):
                    if theBoard[i] == ' ':
                        move = int(i)
                        break
            makeMove(theBoard, computerLetter, move)

            if isWinnner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you!! You lose.!!')
                engine.say('The computerhas beaten you!. You lose')
                engine.runAndWait()
                gameisPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a Tie!!!')
                    engine.say('The game is Tie!')
                    engine.runAndWait()
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
