from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(score.get())
        if(value < 80):
            edu.set("硕士以下")
        elif(value <90):
            edu.set("硕士")
        else:
            edu.set("博士")
    except ValueError:
        pass

root = Tk()
root.title("分数 to 学历")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

score = StringVar()
score_entry = ttk.Entry(mainframe, width=7, textvariable=score)
score_entry.grid(column=2, row=1, sticky=(W, E))

edu = StringVar()
ttk.Label(mainframe, textvariable=edu).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="结果", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="分数").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="是").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="学历").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

score_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()