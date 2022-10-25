import pygame as pg
import sys
from random import randint

def check_bound(obj_rct, scr_rct):#obj_ret:鳥rct, 弾rct
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1

    return yoko, tate


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()

    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    #爆弾１
    bomb_sfc = pg.Surface((20,20))
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 5)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0, 1600)
    bomb_rct.centery = randint(0, 900)

    #爆弾２
    bomb2_sfc = pg.Surface((20,20))
    bomb2_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb2_sfc, (255, 0, 0), (10, 10), 5)
    bomb2_rct = bomb2_sfc.get_rect()
    bomb2_rct.centerx = randint(0, 1600)
    bomb2_rct.centery = randint(0, 900)

    #爆弾３
    bomb3_sfc = pg.Surface((20,20))
    bomb3_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb3_sfc, (255, 0, 0), (10, 10), 5)
    bomb3_rct = bomb3_sfc.get_rect()
    bomb3_rct.centerx = randint(0, 1600)
    bomb3_rct.centery = randint(0, 900)

    font = pg.font.Font(None, 30)
    txt = font.render(str("auto:on"), True, (0, 0, 0))

    vx, vy = +1.0, +1.0
    vx2, vy2 = +1.0, +1.0
    vx3, vy3 = +1.0, +1.0
    vt, vt2, vt3 = 1.0, 1.0, 1.0 #加速

    auto = False #Trueの時は自動

    clock = pg.time.Clock()
    

    while True:
        scrn_sfc.blit(bg_sfc, bg_rct)

        if auto:
            scrn_sfc.blit(txt, (1500, 15))
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key_state = pg.key.get_pressed()
        if key_state[pg.K_UP]:
            auto = False
            tori_rct.centery -= 1
        if key_state[pg.K_DOWN]:
            auto = False
            tori_rct.centery += 1
        if key_state[pg.K_LEFT]:
            auto = False
            tori_rct.centerx -= 1
        if key_state[pg.K_RIGHT]:
            auto = False
            tori_rct.centerx += 1

        yoko, tate = check_bound(tori_rct, scrn_rct)
        if yoko == -1:
            if key_state[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_state[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        if tate == -1:
            if key_state[pg.K_UP]:
                tori_rct.centery += 1 
            if key_state[pg.K_DOWN]:
                tori_rct.centery -= 1

        if key_state[pg.K_a]:
            auto = True
        scrn_sfc.blit(tori_sfc, tori_rct)

        #爆弾１
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        if yoko == -1:
            vt += 0.0001
            vx *= -1.0
        if tate == -1:
            vt += 0.0001
            vy *= -1.0
        if vt < 1.002:
            vx *= vt
            vy *= vt
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct)

        #爆弾２
        yoko, tate = check_bound(bomb2_rct, scrn_rct)
        if yoko == -1:
            vt2 += 0.0001
            vx2 *= -1.0
        if tate == -1:
            vt2 += 0.0001
            vy2 *= -1.0
        if vt2 < 1.002:
            vx2 *= vt2
            vy2 *= vt2
        bomb2_rct.move_ip(vx2, vy2)
        scrn_sfc.blit(bomb2_sfc, bomb2_rct)

        #爆弾３
        yoko, tate = check_bound(bomb3_rct, scrn_rct)
        if yoko == -1:
            vt3 += 0.0001
            vx3 *= -1.0
        if tate == -1:
            vt3 += 0.0001
            vy3 *= -1.0
        if vt3 < 1.002:
            vx3 *= vt3
            vy3 *= vt3
        bomb3_rct.move_ip(vx3, vy3)
        scrn_sfc.blit(bomb3_sfc, bomb3_rct)

        #衝突判定。auto時はランダムに移動。
        if tori_rct.colliderect(bomb_rct) or tori_rct.colliderect(bomb2_rct) or tori_rct.colliderect(bomb3_rct):
            if auto:
                tori_rct.center = (randint(0, 1500), randint(100, 800))
                scrn_sfc.blit(tori_sfc, tori_rct)
            else:
                return

        pg.display.update()

        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()