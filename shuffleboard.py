from Tkinter import Tk, Label, Button
import serial

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Shuffle Board")
		
	self.gameTitle = Label(master, text = "Shuffle Board").grid(row = 0)
	self.round1 = Label(master, text = "Round 1",padx = 10).grid(row = 0, column = 1)
	self.round2 = Label(master, text = "Round 2",padx = 10).grid(row = 0, column = 2)
	self.round3 = Label(master, text = "Round 3",padx = 10).grid(row = 0, column = 3)
	self.round4 = Label(master, text = "Round 4",padx = 10).grid(row = 0, column = 4)
	self.round5 = Label(master, text = "Round 5",padx = 10).grid(row = 0, column = 5)
	self.round5 = Label(master, text = "Final",padx = 10).grid(row = 0, column = 6)
#Player1
	self.player1 = Label(master, text="Player1").grid(row = 1)
	self.p1round1 = Label(master, text = "0").grid(row = 1, column = 1)
	self.p1round2 = Label(master, text = "0").grid(row = 1, column = 2)
	self.p1round3 = Label(master, text = "0").grid(row = 1, column = 3)
	self.p1round4 = Label(master, text = "0").grid(row = 1, column = 4)
	self.p1round5 = Label(master, text = "0").grid(row = 1, column = 5)
	self.p1total = Label(master, text = "0").grid(row = 1, column = 6)
#Player2
	self.player2 = Label(master, text="Player2").grid(row = 2)
        self.p1round1 = Label(master, text = "0").grid(row = 2, column = 1)
        self.p2round2 = Label(master, text = "0").grid(row = 2, column = 2)
        self.p3round3 = Label(master, text = "0").grid(row = 2, column = 3)
        self.p4round4 = Label(master, text = "0").grid(row = 2, column = 4)
        self.p5round5 = Label(master, text = "0").grid(row = 2, column = 5)
        self.p2total = Label(master, text = "0").grid(row = 2, column = 6)




	self.close_button = Button(master, text="Close", command=master.quit).grid(row = 3)
def readSerial():
	while True:
		c = ser.read()
		print c
		if len(c) == 0:
			break
		if c == "1":
			print "in c ==1"
			my_gui.p1total['text']=1
		if c == 2:
			self.p1total['text']=2
		root.after(10, readSerial)
							

ser = serial.Serial('/dev/ttyUSB0', 9600)


round = 0;
player1Turn = True;
player2Turn = False;

root = Tk()
my_gui = MyFirstGUI(root)
root.after(100, readSerial)
root.mainloop()
