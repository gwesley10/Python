
def printboard(board):
    print "\t"+board[0][0]+"\t|\t"+board[0][1]+"\t|\t"+board[0][2]
    print "-----------------------"
    print "\t" + board[1][0] + "\t|\t" + board[1][1] + "\t|\t" + board[1][2]
    print "-----------------------"
    print "\t" + board[2][0] + "\t|\t" + board[2][1] + "\t|\t" + board[2][2]

def makeboard():
    board=[["-","-","-"],["-","-","-"],["-","-","-"]]
    return board

def placemarker(move,player,board):
    row=0
    if move==4 or move==5 or move==6:
        row=1
    if move==7 or move==8 or move==9:
        row=2
    column=2
    if move%3==1 or move%3==2:
        column=move%3-1
    board[row][column]=player
    return board

def checkboard(board):
    if board[0][0]!="-":
        if board[0][1]==board[0][0] and board[0][2]==board[0][0]:
            return True
        if board[1][0]==board[0][0] and board[2][0]==board[0][0]:
            return True
        if board[1][1] == board[0][0] and board[2][2] == board[0][0]:
            return True
    if board[1][0]!="-":
        if board[1][1]==board[1][0] and board[1][2]==board[1][0]:
            return True
    if board[2][0]!="-":
        if board[2][1]==board[2][0] and board[2][2]==board[2][0]:
            return True
        if board[0][1]!="-":
            if board[0][1] == board[0][1] and board[2][1] == board[0][1]:
                return True
    if board[0][2]!="-":
        if board[1][1]==board[0][2] and board[2][0]==board[0][2]:
            return True
        if board[1][2]==board[0][2] and board[2][2]==board[0][2]:
            return True
    return False

board=makeboard()
printboard(board)
check=False
counter=1
player="X"
stop="stop"
while(check==False):
    if counter%2==0:
        player="O"
    else:
        player="X"
    move=input("What move would you like to take?(1-9 or stop to end game)")
    if move==stop:
        check=True
        break
    else:
        placemarker(move,player,board)
    printboard(board)
    check=checkboard(board)
    counter+=1;
print "Congradulations Player %s! you have won!" %(player)
