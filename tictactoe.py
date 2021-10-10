import os    
import time



marker = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
competitor = 1    

print("Enter name of player 1:")
pl = input()
print("Enter name of player 2:")
pll = input()

Won = 1    
Draw = -1    
Still = 0    
Stop = 1    

   
Match = Still    
Mark = 'X'    
   
#For board   
def board():    
    print(" %c | %c | %c " % (marker[1],marker[2],marker[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (marker[4],marker[5],marker[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (marker[7],marker[8],marker[9]))    
    print("   |   |   ")    
   
#Check position   
def CheckPosition(x):    
    if(marker[x] == ' '):    
        return True    
    else:    
        return False    
   
#Tells state of the match   
def getwinner():    
    global Match
    #Vertically   
    if(marker[1] == marker[4] and marker[4] == marker[7] and marker[1] != ' '):    
        Match = Won    
    elif(marker[2] == marker[5] and marker[5] == marker[8] and marker[2] != ' '):    
        Match = Won    
    elif(marker[3] == marker[6] and marker[6] == marker[9] and marker[3] != ' '):    
        Match=Won    
    #Diagonally 
    elif(marker[1] == marker[5] and marker[5] == marker[9] and marker[5] != ' '):    
        Match = Won    
    elif(marker[3] == marker[5] and marker[5] == marker[7] and marker[5] != ' '):    
        Match=Won
    elif(marker[1]!=' ' and marker[2]!=' ' and marker[3]!=' ' and marker[4]!=' ' and marker[5]!=' ' and marker[6]!=' ' and marker[7]!=' ' and marker[8]!=' ' and marker[9]!=' '):    
        Match=Draw 
    #Horizontally
    elif(marker[1] == marker[2] and marker[2] == marker[3] and marker[1] != ' '):    
        Match = Won    
    elif(marker[4] == marker[5] and marker[5] == marker[6] and marker[4] != ' '):    
        Match = Won    
    elif(marker[7] == marker[8] and marker[8] == marker[9] and marker[7] != ' '):    
        Match = Won    
    else:            
        Match=Still    
    

print("%s [X] --- %s [O]\n\n" % (pl, pll))   
print("Please Wait...")    
time.sleep(3)    
while(Match == Still):    
    os.system('cls')    
    board()    
    if(competitor % 2 != 0):    
        print("%s's chance" % pl)    
        Mark = 'X'    
    else:    
        print("%s's chance" % pll)    
        Mark = 'O'    
    choice = int(input("Enter the position between [1-9] where you want to mark : "))    
    if(CheckPosition(choice)):    
        marker[choice] = Mark    
        competitor+=1    
        getwinner()    
    
os.system('cls')    
board()    
if(Match==Draw):    
    print("Match Draw")    
elif(Match==Won):    
    competitor-=1    
    if(competitor%2!=0):    
        print("%s Won the match!" % pl)    
    else:    
        print("%s Won the match!" % pll)


print("                        GAME OVER\n")


print("Give a star to this repo and follow Vinayak Pandey AKA Harpia-Vieillot")
