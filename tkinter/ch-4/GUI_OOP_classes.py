import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
class OOP():
    def __init__(self):
        ''' create instance '''
        self.win = tk.Tk()

        ''' Add a title '''
        self.win.title("Python GUI")
        self.create_widgets()

    ''' button callback '''
    def click_me(self):
        self.action.configure(text = 'Hello' + self.name.get() + ' '
                            +self.number_chosen.get())
    def _spin(self):
        value = self.spin.get() #get the value
        print(value)            #print the value
        self.scrol.insert(tk.INSERT, value + "\n")

    # ... more call back methods

    def create_widgets(self):
        tabControl = ttk.Notebook(self.win)
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text="Tab 1")
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text = "Tab 2")
        # pack to make visible
        tabControl.pack(expand = 1, fill = "both")

        ''' LabelFrame using tab1 as the parent '''
        lf1 = ttk.LabelFrame(tab1, text = 'Label Frame 1')
        lf1.grid(column = 0, row = 0, padx = 8, pady =4)

        ''' Add a label in lf1 '''
        a_label = ttk.Label(lf1, text="Enter a name")
        a_label.grid(column = 0, row = 0, padx = 5, pady = 2)


        ''' Adding a textbox entry widget in labelframe 1'''
        self.name = tk.StringVar()
        name_entered = ttk.Entry(lf1, width = 12, textvariable = self.name)
        name_entered.grid(column = 0, row = 1)

        ''' Adding a button in labelframe1'''
        self.action = ttk.Button(lf1, text = "Click Me!", command = self.click_me)
        self.action.grid(column = 2, row = 1)

        ttk.Label(lf1, text="choose a no").grid(column=1, row=0)
        self.number = tk.StringVar()    # all variable name should precede with self
        self.number_chosen = ttk.Combobox(lf1, width = 12, textvariable = self.number, state='readonly')
        self.number_chosen['values'] = (1, 2, 4, 42, 100)
        self.number_chosen.grid(column = 1, row = 1)
        self.number_chosen.current(0)

        ''' Adding a Spinbox widget '''
        self.spin = tk.Spinbox(lf1, values = (1, 2, 4, 42, 100), width = 5, bd = 9, command = self._spin)
        self.spin.grid(column = 0, row = 2)

        ''' Adding a scrol text '''
        scrol_w = 30
        scrol_h = 3
        self.scrol = scrolledtext.ScrolledText(lf1, width = scrol_w, height = scrol_h, wrap = tk.WORD)
        self.scrol.grid(column = 0, columnspan = 3)


oop = OOP()
screen_width = oop.win.winfo_screenwidth()
screen_height = oop.win.winfo_screenheight()
print(str(screen_width) + "x" + str(screen_height))             #window size
winSize = str(screen_width) + "x" + str(screen_height)
oop.win.geometry(winSize)
# oop.win.geometry(str(oop.win.winfo_screenwidth()) + "x" + str(oop.win.winfo_screenheight))
oop.win.mainloop()
