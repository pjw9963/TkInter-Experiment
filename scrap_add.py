import tkinter as tk 
import sqlite3

def addToTable(name, url, id, isID):
    conn = sqlite3.connect('scrap.db')
    c = conn.cursor()
    c.execute(f"INSERT INTO scraps VALUES ('{name}', '{url}', '{id}', {isID});")
    conn.commit()
    conn.close()


def addScrap(name, url, id, isID, root):
    string = f"{name} {url} {id} {isID}"
    label = tk.Label(root, text=string)
    label.pack()
    addToTable(name, url, id, isID)


root = tk.Tk()
root.title("scrap")
root.geometry('1400x700')

grid = tk.Frame()
grid.pack()

text_name = tk.Entry(grid, width=25)
text_name.grid(row=0,column=0)

text_url = tk.Entry(grid,width=75)
text_url.grid(row=0, column=1, columnspan=3)

text_id = tk.Entry(grid, width=25)
text_id.grid(row=0,column=4)

v = tk.IntVar()

tk.Radiobutton(grid, 
              text="ID",
              padx = 20, 
              variable=v, 
              value=1).grid(row=0,column=5)
tk.Radiobutton(grid, 
              text="Class",
              padx = 20, 
              variable=v, 
              value=0).grid(row=0,column=6)


button = tk.Button(grid, 
    text='Add Scrap Material', 
    bg="#3f3f8f", 
    fg='white', 
    activebackground='#6b6bc9', 
    activeforeground="white",
    command= lambda: 
        addScrap(text_name.get() ,text_url.get(), text_id.get(), v.get(), root))
button.grid(row=0,column=7)

root.mainloop()
