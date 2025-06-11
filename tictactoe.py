from colorama import Fore
print(Fore.RED + "X" + Fore.RESET)  # Colored X
board= ["1","2","3","4","5","6","7","8","9"]
def printboard():
      for i in range(len(board)):
        if ((int(i)+1)%3==0):
            print("|",board[i],"\n")
        else:
            print("|",board[i], end="")
        

def winner():
    win_conditions=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for n in win_conditions:
        if board[n[0]]==board[n[1]]==board[n[2]]:
          print("player",board[n[0]], "wins")
          exit()

           
def game():
    player=1
    history= []
    printboard()
    while True:
        winner()
        if (len(history)==9):
              print("Oops!Draw")
              exit()
        move =int(input("enter the place you need to insert:"))
        if move in history:
               print("The move is already used,please enter another move")
               continue
        else:
             if player==1:
                  board[move-1]= "X"
                  printboard()
                  player=2
                  history.append(move)
             elif player == 2:
                  board[move-1]= "O"
                  printboard()
                  player=1
                  history.append(move)
      
game()
            

