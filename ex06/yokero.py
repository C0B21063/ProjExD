import pygame as pg
import sys
from random import randint


class Screen:
    def __init__(self, title, wh, bgimg):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()

        # 背景画像１
        self.bg1_sfc = pg.image.load(bgimg)
        self.bg1_rct = self.bg1_sfc.get_rect()
        self.bg1_rct.centerx = 0

        # 背景画像２
        self.bg2_sfc = pg.image.load(bgimg)
        self.bg2_rct = self.bg2_sfc.get_rect()
        self.bg2_rct.centerx = 1600

        self.bg_speed = 5 # 背景移動速度

    def blit(self):
        self.sfc.blit(self.bg1_sfc, self.bg1_rct)
        self.sfc.blit(self.bg2_sfc, self.bg2_rct)

    # 背景スライド処理
    def slide(self):
        self.bg1_rct.centerx -= self.bg_speed
        self.bg2_rct.centerx -= self.bg_speed

        if self.bg1_rct.centerx <= -800:
            self.bg1_rct.centerx = 1600
        if self.bg2_rct.centerx <= -800:
            self.bg2_rct.centerx = 1600
        
        self.blit()


class Chara:
    JUMP_NO = 0 # 接地状態
    JUMP_UP = 1 # ジャンプ状態

    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img)
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

        self.jump_state = Chara.JUMP_NO # 接地判定
        self.jump = -30 # ジャンプの大きさ

    def update(self, scr:Screen):
        self.base_y = 600 # 自機初期位置

        # スペースが押されたときの処理
        key_states = pg.key.get_pressed()
        if key_states[pg.K_SPACE]:
            if self.jump_state == Chara.JUMP_NO: # 接地状態の時
                self.jump_state = Chara.JUMP_UP

        # ジャンプ状態の時
        if self.jump_state == Chara.JUMP_UP:
            self.jump += 1
            self.rct.centery += self.jump

            # 接地したら
            if self.rct.centery >= self.base_y:
                self.jump_state = Chara.JUMP_NO
                self.rct.centery = self.base_y
                self.jump = -30 # リセット

        scr.sfc.blit(self.sfc, self.rct)
        
        
class Enemy:
    def __init__(self, ene_list, zoom, x, y):
        self.num = len(ene_list) # 敵画像リストの数を記録
        self.sfc = [0] * self.num
        self.rct = [0] * self.num

        # 敵画像作成
        for i in range(self.num):
            print(i)
            self.sfc[i] = pg.image.load(ene_list[i])
            self.sfc[i] = pg.transform.rotozoom(self.sfc[i], 0, zoom)
            self.rct[i] = self.sfc[i].get_rect()
            self.rct[i].centerx = (x + i*1000 + (randint(1,10)*100)) # 適当な間隔で
            self.rct[i].centery = y

        self.ene_speed = 7  # 敵移動速度

    def blit(self, scr:Screen):
        for i in range(self.num):
            scr.sfc.blit(self.sfc[i], self.rct[i])

    def update(self, scr:Screen):
        for i in range(self.num):
            self.rct[i].centerx -= self.ene_speed

        self.blit(scr)


def main():
    # タイトル表示
    scr = Screen("避けろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")

    # こうかとん表示
    me = Chara("fig/2.png", 2.0, (300, 600)) #ファイル、倍率、場所

    # 敵表示
    ene_list = ["fig/3.png", "fig/4.png", "fig/5.png"] # 敵画像リスト
    ene = Enemy(ene_list, 2.0, 1700, 600)

    clock = pg.time.Clock()
    while True:
        scr.slide() # 背景画像blit

        # xが押された時
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                return

        me.update(scr) # こうかとん移動
        ene.update(scr) # 敵移動

        # 敵画像ループ用
        if ene.rct[2].centerx <= -100:
            ene = Enemy(ene_list, 2.0, 1700, 600)
    
        # 終了判定
        for i in range(3):
            if me.rct.colliderect(ene.rct[i]):
                return

        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()