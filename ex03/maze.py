import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key, state
    state = 1
    key = event.keysym


def key_up(event):
    global key
    key = ""


def main_proc():
    global cx, cy
    global mx, my
    global state, num_tori
    if key == "Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1
    if maze_lst[my][mx] == 0:
        cx = mx * 100 + 50
        cy = my * 100 + 50
    else: #壁なら
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1
    canv.coords("tori", cx, cy)

    if mx == 13 and my == 7:
        state = 2
        canv.create_text(750, 450, text="finish", font=("", 30))

    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    
    canv = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canv.pack()

    maze_lst = mm.make_maze(15, 9)
    mm.show_maze(canv, maze_lst);

    tori = tk.PhotoImage(file = "fig/3.png")
    mx, my = 1, 1
    cx = mx * 100 + 50
    cy = my * 100 + 50
    canv.create_image(cx, cy, image = tori, tag = "tori")

    state = 0
    tmr = 0
    key = "" #現在押されているキーを表す

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()
    
    root.mainloop()