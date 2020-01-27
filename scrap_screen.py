from requests_html import AsyncHTMLSession, HTMLSession
from bs4 import BeautifulSoup
import tkinter as tk
import sqlite3


def comence_scrapping(root):
    conn = sqlite3.connect('scrap.db')
    c = conn.execute("SELECT * FROM scraps;")
    for row in c:
        asession = HTMLSession()
        page = asession.get(row[1])
        try:
            if int(row[3]) == 1:
                result = page.html.find('#' + str(row[2]), first=True).text
            else:
                result = page.html.find('.' + str(row[2]), first=True).text
        except AttributeError as ex:
            result = "...Error..."
        frame = tk.Frame(root)                
        frame.pack()
        name = tk.Label(frame, text=row[0])
        name.grid(row=0,column=0)
        value = tk.Label(frame, text=result)
        value.grid(row=0,column=1)


root = tk.Tk()
root.title("scrap")
root.geometry('1200x700')
comence_scrapping(root)

root.mainloop()
