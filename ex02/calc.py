import tkinter as tk
import tkinter.messagebox as tkm

w,h = 4, 2#ボタンの縦横の長さ

#数字等が押されたとき
def button_click(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo("",f"{num}のボタンがクリックされました。")
    entry.insert(tk.END, num)

#πが押されたとき
def pai_click(event):
    entry.insert(tk.END, 3.14)

#＝が押されたとき
def eql_click(event):
    eql = entry.get()
    res = eval(eql)
    memo = tk.Label(memo_win, text = f"{eql}={res}", font = ("Times New Roman", 10))
    memo.grid()
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

#ACが押されたとき
def ac_click(event):
    entry.delete(0, tk.END)

#％が押された時
def per_click(event):
    eql = entry.get()
    res = eval(eql)
    per_res = res * 0.01
    memo = tk.Label(memo_win, text = f"{eql}={per_res}", font = ("Times New Roman", 10))
    memo.grid()
    entry.delete(0, tk.END)
    entry.insert(tk.END, per_res)

#メイン窓
root = tk.Tk()
root.title("電卓")
root.geometry("400x650")

#履歴窓
memo_win = tk.Tk()
memo_win.title("履歴")
memo_win.geometry("300x300")

#other窓
def high(event):
    high = tk.Tk()
    high.geometry("300x300")

    #小数点ボタン
    eql_btn = tk.Button(high, text = ".", font = ("times New Roman", 30), width = w, height = h)
    eql_btn.bind("<1>", button_click)
    eql_btn.grid(row = 0, column = 0)

    #%ボタン
    eql_btn = tk.Button(high, text = "%", font = ("times New Roman", 30), width = w, height = h)
    eql_btn.bind("<1>", per_click)
    eql_btn.grid(row = 0, column = 1)

    #πボタン
    pai_btn = tk.Button(high,
                        text = "π",
                        font = ("times New Roman", 30),
                        width = w,
                        height = h
                        )
    pai_btn.bind("<1>", pai_click)
    pai_btn.grid(row = 0, column = 2)

entry = tk.Entry(root, justify = "right", width = 10, font = ("Times New Roman", 40))
entry.grid(row = 0, column = 0, columnspan = 3)

r,c = 0,2
for i in range(9,-1,-1):
    button = tk.Button(root,
                    text = f"{i}",
                    font = ("times New Roman", 30),
                    width = w,
                    height = h
                    )
    button.bind("<1>", button_click)
    button.grid(row = r + 1, column = c)
    c -= 1
    if i % 3 == 1:
        r += 1
        c = 2
    if i == 1:
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

#四則演算ボタン
pls_lis = ["/", "*", "-", "+"]
for i in range(4):
    pls_btn = tk.Button(root,
                        text = f"{pls_lis[i]}",
                        font = ("times New Roman", 30),
                        width = w,
                        height = h
                        )
    pls_btn.bind("<1>", button_click)
    pls_btn.grid(row = 1 + i, column = 3)

#高機能ボタン
oth_btn = tk.Button(root,
                    text = "other",
                    font = ("times New Roman", 30),
                    width = w,
                    height = h
                    )
oth_btn.bind("<1>", high)
oth_btn.grid(row = 4, column = 1)

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