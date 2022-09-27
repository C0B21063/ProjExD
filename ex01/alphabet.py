import random
import datetime

num = 10
nnum = 2
num_try = 2

def syutudai(alpha):
    taisyo = random.sample(alpha,num)
    print("対象文字:")
    for c in taisyo:
        print(c, end="")
    print("")
    print("表示文字:")
    kesson = random.sample(taisyo,nnum)
    for c in taisyo:
        if c not in kesson:
            print(c,end="")
    print("")
    return kesson

def kotae(kesson):
    ans_num = int(input("欠損文字はいくつ？："))
    if ans_num != nnum:
        print("文字数が不正解")
    else:
        print("正解。欠損文字を1つずつ入力してください。")
        for i in range(nnum):
            ans = input(f"{i+1}文字目:")
            if ans in kesson:
                kesson.remove(ans)
            else:
                print("不正解")
                break
        else:
            return 1
    return 0


if __name__ == "__main__":
    alpha = [chr(i+65) for i in range(26)]
    for i in range(num_try):
        kesson = syutudai(alpha)
        re = kotae(kesson)
        if re == 0:
            print("不正解です。またチャレンジしてください。")
            print("-"*20)
        else:
            break
        