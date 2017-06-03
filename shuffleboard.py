from Tkinter import Tk, Label, Button
import serial


def readSerial():
    while True:
        print "trying to read"
        c = ser.read()
        print c
        
        if len(c) == 0:
			break
        if c == "1":
            print "in c ==1"
            p1total.config(text='1') 
        if c == '2':
            p2total.config(text='2')
    root.after(10, readSerial)
							


root = Tk()

root.title("Shuffle Board")
gameTitle = Label(root, text = "Shuffle Board").grid(row = 0)
round1 = Label(root, text = "Round 1",padx = 10).grid(row = 0, column = 1)
round2 = Label(root, text = "Round 2",padx = 10).grid(row = 0, column = 2)
round3 = Label(root, text = "Round 3",padx = 10).grid(row = 0, column = 3)
round4 = Label(root, text = "Round 4",padx = 10).grid(row = 0, column = 4)
round5 = Label(root, text = "Round 5",padx = 10).grid(row = 0, column = 5)
round5 = Label(root, text = "Final",padx = 10).grid(row = 0, column = 6)
#Player1
player1 = Label(root, text="Player1").grid(row = 1)
p1round1 = Label(root, text = "0").grid(row = 1, column = 1)
p1round2 = Label(root, text = "0").grid(row = 1, column = 2)
p1round3 = Label(root, text = "0").grid(row = 1, column = 3)
p1round4 = Label(root, text = "0").grid(row = 1, column = 4)
p1round5 = Label(root, text = "0").grid(row = 1, column = 5)
p1total = Label(root, text = "0")
p1total.grid(row = 1, column = 6)
#Player2
player2 = Label(root, text="Player2").grid(row = 2)
p1round1 = Label(root, text = "0").grid(row = 2, column = 1)
p2round2 = Label(root, text = "0").grid(row = 2, column = 2)
p3round3 = Label(root, text = "0").grid(row = 2, column = 3)
p4round4 = Label(root, text = "0").grid(row = 2, column = 4)
p5round5 = Label(root, text = "0").grid(row = 2, column = 5)
p2total = Label(root, text = "0")
p2total.grid(row = 2, column = 6)

#close function
close_button = Button(root, text="Close", command=root.quit).grid(row = 3)


serialPort = '/dev/ttyUSB0'
baudRate = 9600
ser = serial.Serial(serialPort, baudRate,timeout = 0, writeTimeout = 0)
# 

round = 0;
player1Turn = True;
player2Turn = False;

root.after(10, readSerial)
root.mainloop()
