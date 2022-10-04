import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    tkm.showinfo("",f"{num}のボタンがクリックされました。")

root = tk.Tk()
root.geometry("300x500")

r,c = 0,0
for i in range(9,-1,-1):
    button = tk.Button(root,
                    text = f"{i}",
                    font = ("times New Roman", 30),
                    width = 4,
                    height = 2
                    )
    button.bind("<1>", button_click)
    button.grid(row = r, column = c)
    c += 1
    if i % 3 == 1:
        r += 1
        c = 0
    
root.mainloop()