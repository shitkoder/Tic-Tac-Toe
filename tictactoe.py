import os    
import time



cursor = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
adversary = 1    

print("Enter name of player 1:")
pl = input()
print("Enter name of player 2:")
pll = input()

Won = 1    
Draw = -1    
Ongoing = 0    
Stop = 1    

   
Game = Ongoing    
Check = 'X'    
   
#For board   
def board():    
    print(" %c | %c | %c " % (cursor[1],cursor[2],cursor[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (cursor[4],cursor[5],cursor[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (cursor[7],cursor[8],cursor[9]))    
    print("   |   |   ")    
   
#Check position   
def CheckPosition(x):    
    if(cursor[x] == ' '):    
        return True    
    else:    
        return False    
   
#Tells state of the match   
def getwinner():    
    global Game
    #Vertically   
    if(cursor[1] == cursor[4] and cursor[4] == cursor[7] and cursor[1] != ' '):    
        Game = Won    
    elif(cursor[2] == cursor[5] and cursor[5] == cursor[8] and cursor[2] != ' '):    
        Game = Won    
    elif(cursor[3] == cursor[6] and cursor[6] == cursor[9] and cursor[3] != ' '):    
        Game=Won    
    #Diagonally 
    elif(cursor[1] == cursor[5] and cursor[5] == cursor[9] and cursor[5] != ' '):    
        Game = Won    
    elif(cursor[3] == cursor[5] and cursor[5] == cursor[7] and cursor[5] != ' '):    
        Game=Won
    elif(cursor[1]!=' ' and cursor[2]!=' ' and cursor[3]!=' ' and cursor[4]!=' ' and cursor[5]!=' ' and cursor[6]!=' ' and cursor[7]!=' ' and cursor[8]!=' ' and cursor[9]!=' '):    
        Game=Draw 
    #Horizontally
    elif(cursor[1] == cursor[2] and cursor[2] == cursor[3] and cursor[1] != ' '):    
        Game = Won    
    elif(cursor[4] == cursor[5] and cursor[5] == cursor[6] and cursor[4] != ' '):    
        Game = Won    
    elif(cursor[7] == cursor[8] and cursor[8] == cursor[9] and cursor[7] != ' '):    
        Game = Won    
    else:            
        Game=Ongoing    
    

print("%s [X] --- %s [O]\n\n" % (pl, pll))   
print("Please Wait...")    
time.sleep(3)    
while(Game == Ongoing):    
    os.system('cls')    
    board()    
    if(adversary % 2 != 0):    
        print("%s's chance" % pl)    
        Check = 'X'    
    else:    
        print("%s's chance" % pll)    
        Check = 'O'    
    choice = int(input("Enter the position between [1-9] where you want to mark : "))    
    if(CheckPosition(choice)):    
        cursor[choice] = Check    
        adversary+=1    
        getwinner()    
    
os.system('cls')    
board()    
if(Game==Draw):    
    print("Game Draw")    
elif(Game==Won):    
    adversary-=1    
    if(adversary%2!=0):    
        print("%s Won the match!" % pl)    
    else:    
        print("%s Won the match!" % pll)


print("                        GAME OVER\n")


print("Give a star to this repo and follow Vinayak Pandey AKA Harpia-Vieillot")

