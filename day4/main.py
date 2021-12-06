#gets boards and number sequence from input file
input = open('input', 'r')
sequence = input.readline().split(",")
sequence[len(sequence) - 1] = sequence[(len(sequence) - 1)].split("\n")[0]

boards = [[["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""]]]
boardsMarked = [[[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]]]

def getRowValues(row):
    completeRow = ["", "", "", "", ""]
    valuePosition = 0
    for i in range(len(row)):
        if row[i] == " " or row[i] == "\n":
            if completeRow[valuePosition] != "":
                valuePosition += 1
            continue
        completeRow[valuePosition] +=  row[i]
    return completeRow

currentBoard = -1
boardsValues = input.readlines()
currentRow = -1
for row in boardsValues:
    if(row == "\n"):
        currentBoard += 1
        currentRow = -1
        continue
    else:
        currentRow += 1
    if(currentBoard >= len(boards)):
        boards.append([["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""]])
        boardsMarked.append([[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]])
    boards[currentBoard][currentRow] = getRowValues(row)

def checkForWinner(board):
    hasWon = True
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[j][i] == False:
                hasWon = False
                break
        if hasWon:
            return True
        for j in range(len(board[0])):
            if board[i][j] == False:
                hasWon = False
                break
    return hasWon

def calculateWinnerResult(markedResults, values, numberCalled):
    sumOfUnmarkedNumbers = 0
    print(values)
    print(markedResults)
    print(numberCalled)
    for i in range(len(markedResults)):
        for j in range(len(markedResults[0])):
            if(not markedResults[i][j]):
                sumOfUnmarkedNumbers += int(values[i][j])
    return sumOfUnmarkedNumbers * numberCalled

for number in sequence:
    for boardNumber in range(len(boards) ):
        for i in range(len(boards[boardNumber])):
            for j in range(len(boards[boardNumber])):
                if boards[boardNumber][i][j] == number:
                    boardsMarked[boardNumber][i][j] = True
                    if checkForWinner(boardsMarked[boardNumber]):
                        print("Winner is " + str(boardNumber) + " with result " + str(calculateWinnerResult(boardsMarked[boardNumber], boards[boardNumber], int(number))))
                        break
            else:
                continue
            break
        else:
            continue
        break
    else:
        continue
    break