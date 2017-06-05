from Tkinter import Tk, Label, Button
import serial
from array import *


def readSerial():
    while True:
        c = ser.read()
        global p1scores
        global p1totalInt
        if len(c) == 0:
            break
        if c == "1":
			print "in c ==1"
			
			p1scores[0]+=1
			p1totalInt += 1
			p1rounds[0].config(text = str(p1scores[0]))
			p1total.config(text = str(p1totalInt))
        if c == '2':
			p1scores[0]+=2
			p1totalInt += 2
			p1rounds[0].config(text = str(p1scores[0]))
			p1total.config(text = str(p1totalInt))
    root.after(10, readSerial)
							


root = Tk()

root.title("Shuffle Board")
gameTitle = Label(root, text = "Shuffle Board").grid(row = 0)
round5 = Label(root, text = "Final",padx = 10).grid(row = 0, column = 6)

#Player1
player1 = Label(root, text="Player1").grid(row = 1)
p1total = Label(root, text = "0")
p1total.grid(row = 1, column = 6)

#Player2
player2 = Label(root, text="Player2").grid(row = 2)
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


#close function
close_button = Button(root, text="Close", command=root.quit).grid(row = 3)

#serial init
serialPort = '/dev/ttyUSB0'
baudRate = 9600
ser = serial.Serial(serialPort, baudRate,timeout = 0, writeTimeout = 0)
 
round = 0
throwcount = 0
player1Turn = True
player2Turn = False

p1scores = array('i',[0,0,0,0,0])
p2scores = array('i',[0,0,0,0,0])

p1totalInt = 0
p2totalInt = 0


root.after(10, readSerial)
root.mainloop()
