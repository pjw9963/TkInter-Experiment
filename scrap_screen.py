import requests
from bs4 import BeautifulSoup
import tkinter as tk
import sqlite3


def comence_scrapping(root):
    headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'}
    conn = sqlite3.connect('scrap.db')
    c = conn.execute("SELECT * FROM scraps;")
    for row in c:
        page = requests.get(row[1], headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        try:
            print(row[3])
            if int(row[3]) == 1:
                result = soup.find(id=str(row[2])).get_text().strip()
            else:
                print("'" + str(row[2]) + "'")
                result = soup.find_all("html_element", class_=str(row[2])).get_text().strip()
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
