import tkinter as tk

from tkinter import filedialog
from main import *

# Function for opening the
# file explorer window

heights = ""
edges = ""

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.json*"),
                                                       ("all files",
                                                        "*.*")))
    return filename


def show_entry_fields():
    global heights, edges
    heights = e1.get()
    edges = e2.get()
    return heights, edges


master = tk.Tk()

master.title("network-visualizer")
master.geometry("400x150")
tk.Label(master,
         text="Heights").grid(row=0)
tk.Label(master,
         text="Edges").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=3,
                                    column=3,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master,
          text='Select File',
          command=lambda: [show_entry_fields(), master.quit()]).grid(
                           row=3,
                           column=0,
                           sticky=tk.W,
                           pady=4)

tk.mainloop()

filename = browseFiles()

run_program(filename, heights, edges)




