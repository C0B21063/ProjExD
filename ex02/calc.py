import tkinter as tk
import tkinter.messagebox as tkm

w,h = 4, 2#ボタンの縦横の長さ

def button_click(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo("",f"{num}のボタンがクリックされました。")
    entry.insert(tk.END, num)


def eql_click(event):
    eql = entry.get()
    res = eval(eql)
    memo = tk.Label(memo_win, text = f"{eql}={res}", font = ("Times New Roman", 10))
    memo.grid()
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

def ac_click(event):
    entry.delete(0, tk.END)



root = tk.Tk()
root.title("電卓")
root.geometry("400x600")

memo_win = tk.Tk()
memo_win.title("履歴")
memo_win.geometry("300x300")

entry = tk.Entry(root, justify = "right", width = 10, font = ("Times New Roman", 40))
entry.grid(row = 0, column = 0, columnspan = 3)

r,c = 0,0
for i in range(9,-1,-1):
    button = tk.Button(root,
                    text = f"{i}",
                    font = ("times New Roman", 30),
                    width = w,
                    height = h
                    )
    button.bind("<1>", button_click)
    button.grid(row = r + 1, column = c)
    c += 1
    if i % 3 == 1:
        r += 1
        c = 0

#ここから手作業
#acボタン
cle_btn = tk.Button(root,
                    text = "AC",
                    font = ("times New Roman", 30),
                    width = w,
                    height = h
                    )
cle_btn.bind("<1>", ac_click)
cle_btn.grid(row = 0, column = 3)

#+ボタン
pls_lis = ["+", "-", "/", "*"]
for i in range(4):
    pls_btn = tk.Button(root,
                        text = f"{pls_lis[i]}",
                        font = ("times New Roman", 30),
                        width = w,
                        height = h
                        )
    pls_btn.bind("<1>", button_click)
    pls_btn.grid(row = 1 + i, column = 3)

#=ボタン
eql_btn = tk.Button(root,
                    text = "=",
                    font = ("times New Roman", 30),
                    width = w,
                    height = h
                    )
eql_btn.bind("<1>", eql_click)
eql_btn.grid(row = 4, column = 2)

root.mainloop()