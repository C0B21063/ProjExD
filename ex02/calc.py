import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo("",f"{num}のボタンがクリックされました。")
    entry.insert(tk.END, num)

root = tk.Tk()
root.geometry("300x600")

entry = tk.Entry(root, justify = "right", width = 10, font = ("Times New Roman", 40))
entry.grid(row = 0, column = 0, columnspan = 3)

r,c = 0,0
for i in range(9,-1,-1):
    button = tk.Button(root,
                    text = f"{i}",
                    font = ("times New Roman", 30),
                    width = 4,
                    height = 2
                    )
    button.bind("<1>", button_click)
    button.grid(row = r + 1, column = c)
    c += 1
    if i % 3 == 1:
        r += 1
        c = 0

ano_btn = tk.Button(root,
                    text = "+",
                    font = ("times New Roman", 30),
                    width = 4,
                    height = 2
                    )
ano_btn.bind("<1>", button_click)
ano_btn.grid(row = 4, column = 1)

root.mainloop()

