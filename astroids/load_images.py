import pygame as pg
import settings as S
import player
import roids


def load_player():
    ######## Loading images ##########

    #player_image = pg.image.load("ship.png")
    #scaled_player = pg.transform.scale(player_image, S.PLAYER_SIZE)
    #scaled_player.convert_alpha()
    #return scaled_player

    #player_image2 = pg.image.load("ship2.png")
    #scaled_player2 = pg.transform.scale(player_image2, S.PLAYER_SIZE)
    #return scaled_player2
    
    player_image3 = pg.image.load("ship3.png")
    scaled_player3 = pg.transform.scale(player_image3, S.PLAYER_SIZE)
    return scaled_player3
    
    #player_images = [scaled_player2, scaled_player3]
    #return player_images

def load_background():

    background_image = pg.image.load("bkg.png")
    scaled_background = pg.transform.scale(background_image, (S.WIDTH, S.HEIGHT))
    return scaled_background

def load_astroid():

    small_astroid_image = pg.image.load("astroid.png")
    scaled_small_astroid = pg.transform.scale(small_astroid_image, (S.SMALL_ASTROID * 2, S.SMALL_ASTROID * 2))

    medium_astroid_image = pg.image.load("astroid.png")
    scaled_medium_astroid = pg.transform.scale(medium_astroid_image, (S.MEDIUM_ASTROID * 2, S.MEDIUM_ASTROID * 2))

    big_astroid_image = pg.image.load("astroid.png")
    scaled_big_astroid = pg.transform.scale(big_astroid_image, (S.BIG_ASTROID * 2, S.BIG_ASTROID * 2))

    astroid_images = [scaled_small_astroid, scaled_medium_astroid, scaled_big_astroid]
    return astroid_images
