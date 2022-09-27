import random
Toi = ["サザエの旦那の名前は","カツオの妹の名前は","タラオはカツオから見てどんな関係"]
Kai = [["マスオ","ますお"],["ワカメ","わかめ"],["おい","甥","おいっこ","甥っ子"]]

def shutudai():
    num = random.randint(2)
    mondai = (Toi[num],Kai(num))
    print(Toi[num])
    
def kaito(kai):
    ans = input("kotae:")
    if kai in kai:
        print("yoi")
    else:
        print("not")


if __name__ == "__main__":
    print("mondai:")
    shutudai()
    

