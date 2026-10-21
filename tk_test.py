import tkinter as tk
from tkinter import messagebox as msgbox

root = tk.Tk()
root.geometry('320x450')
root.resizable(False, False)


frame = tk.Frame(root, bd=3, relief=tk.RIDGE, width=10, height=10)
frame.pack(expand=False)

label = tk.Label(frame, text='test', bg='lightblue')
label.pack()


label = tk.Label(frame, text='te111111111111111st', bg='lightblue')
label.pack()

root.mainloop()
