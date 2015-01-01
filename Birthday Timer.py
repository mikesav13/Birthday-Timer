from Tkinter import Tk, Frame, BOTH #To Hangle Frameing
from ttk import Frame, Button, Style #To handle Window, Theming and Buttons
from PIL import Image, ImageTk #To handle Images, SOMETHING WRONG HERE

import datetime
time = datetime.datetime.now()

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Buttons")
        self.style = Style()
        self.style.theme_use("default")
        
        self.pack(fill=BOTH, expand=1)
        
        closeButton = Button(self, text="Close")
        closeButton.pack(padx=5, pady=30)
        okButton = Button(self, text="OK")
        okButton.pack()

def main():

    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()  

	

if __name__ == '__main__':
    main()  

print
print
print 
 
print ("Current Date =  %s/%s/%s" % (time.day, time.month, time.year) )
 
 
print ("Time = %s:%s:%s" % (time.hour, time.minute, time.second) )
print
print
print

while True:

	dt  = datetime.datetime
	now = dt.now()
	# This gives timedelta in days
	delta = dt(year=2015,month=02,day=04,hour=7,minute=0,second=0) - dt(year=now.year, month=now.month, day=now.day, hour = now.hour, minute = now.minute, second = now.second)
	alpha = str(delta).split(":")
	beta = str(alpha).split(" ")
	beta = str(beta).strip("[") #Take out the [ for every reading of 33
	daysL = beta[3] + beta[4]   #Number of days to event
	hoursL = beta[18] + beta[19]
	minutesL = beta[27] + beta[28]
	secondsL = beta[36] + beta[37]
	
	#print("Time Left: " int(daysL) + "Days, " + int(hoursL) + "Hours, " + int(minutesL) + "Minutes, " + int(secondsL) + "Seconds")
	print("Time Left: " + daysL + " Days, " + hoursL + " Hours, " + minutesL + "  Minutes, " + secondsL + " Seconds")
	# This gives timedelta in days & seconds


	#	startCounting = datetime.combine(now.date(), time(0))
	#	print (time - startCounting).seconds