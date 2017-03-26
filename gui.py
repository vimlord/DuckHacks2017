from tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master):
        
        self.master = master
        master.minsize(width=666, height=666)
        master.title("A simple GUI")
        
        self.label = Label(master, text="Current Mood: " + mood, font=("Helvetica", 20))
        self.label.pack()
        
        self.label = Label(master, text="Current Genre: " + genre, font=("Helvetica", 20))
        self.label.pack()
        
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()


def disp(mood, genre):
