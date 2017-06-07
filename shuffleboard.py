from Tkinter import Tk, Label, Button
import serial
from time import sleep
from array import *

#1 is a shot
#2 is a score
def readSerial():
    while True:
        global p1scores
        global p1totalInt
        global p2scores
        global p2totalInt
        global round
        global throwCount
        global player1Turn
        global player2Turn
        global player1
        global player2
        global shotsCounter
        
        c = ser.read()
        if len(c) == 0:
            break
        #a puck has been shot
        if c == "1":
            print "Shot made"
            throwCount += 1
            shotsCounter.config(text = str(throwCount) + '/5')
            print 'throwCount = ' + str(throwCount)
            #shot has been missed
            print "Missed shot"
            #Check if players turn is over
            if throwCount > 4:
                throwCount = 0
                shotsCounter.config(text = str(throwCount) + '/5')
                print 'players turn is over'
            #Players turn is over Switch players
            #TODO check if game is over
                if player1Turn:
                    player1Turn = False
                    player2Turn = True
                    player1.config(bg = 'light grey')
                    player2.config(bg = 'red')
                else:
                    player1Turn = True
                    player2Turn = False
                    player1.config(bg = 'red')
                    player2.config(bg = 'light grey')
                    round += 1
                    rounds[round].config(bg = 'red')
                    rounds[round-1].config(bg = 'light grey')
 
            
        #shot has been made find how many points to add to player
        if c == '2':
            print 'player has scored'
            
            if player1Turn:
                p1scores[round] += 1
                p1rounds[round].config(text = str(p1scores[round]))
                                   
                p1totalInt += 1
                p1total.config(text = str(p1totalInt))

            #Player2 made a point    
            else:
                p2scores[round] += 1
                p2rounds[round].config(text = str(p2scores[round]))
                                   
                p2totalInt += 1
                p2total.config(text = str(p2totalInt))
            #Check if players turn is over
            if throwCount > 4:
                throwCount = 0
                print 'players turn is over'
                #Players turn is over Switch players
                #TODO check if game is over
                
                if player1Turn:
                    player1Turn = False
                    player2Turn = True
                    player1.config(bg = 'light grey')
                    player2.config(bg = 'red')
                    
                else:
                    player1Turn = True
                    player2Turn = False
                    player1.config(bg = 'red')
                    player2.config(bg = 'light grey')
                    round += 1
                    rounds[round].config(bg = 'red')
                    rounds[round-1].config(bg = 'light grey')
    root.after(10, readSerial)
							


root = Tk()

root.title("Shuffle Board")
gameTitle = Label(root, text = "Shuffle Board").grid(row = 0)
round5 = Label(root, text = "Final",padx = 10).grid(row = 0, column = 6)

#Player1
player1 = Label(root, text="Player1", bg = 'red')
player1.grid(row = 1)
p1total = Label(root, text = "0")
p1total.grid(row = 1, column = 6)

#Player2
player2 = Label(root, text="Player2")
player2.grid(row = 2)
p2total = Label(root, text = "0")
p2total.grid(row = 2, column = 6)

#Create player 1 and 2 rounds
p1rounds = []
p2rounds = []
rounds = []
for x in range(0,5):
    #round labels
    rounds.append(Label(root, text = "Round " + str(x+1),padx = 10))
    rounds[x].grid(row = 0, column = x+1)
    #p1
    p1rounds.append(Label(root, text = "0"))
    p1rounds[x].grid(row = 1, column = x+1)
    #p2
    p2rounds.append(Label(root, text = "0"))
    p2rounds[x].grid(row = 2, column = x+1)
    print "creating rounds" + str(x)
rounds[0].config(bg = 'red')

#label to show how many shots have been taken
shotsLabel = Label(root, text = "Shots Taken")
shotsLabel.grid(row = 3, column = 0)
shotsCounter = Label(root, text = "0/5")
shotsCounter.grid(row = 3, column = 1)

#close function
close_button = Button(root, text="Close", command=root.quit).grid(row = 3,column = 6)

#serial init
serialPort = '/dev/ttyUSB0'
baudRate = 9600
ser = serial.Serial(serialPort, baudRate,timeout = 0, writeTimeout = 0)
 
round = 0
throwCount = 0
player1Turn = True
player2Turn = False


p1scores = array('i',[0,0,0,0,0])
p2scores = array('i',[0,0,0,0,0])

p1totalInt = 0
p2totalInt = 0


root.after(10, readSerial)
root.mainloop()
