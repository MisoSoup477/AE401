# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 02:27:40 2020

@author: 學生
"""

from mcpi.minecraft import Minecraft
#導入minecraft模組
mc = Minecraft.create();

while True:
#while 迴圈
    x,y,z=mc.player.getTilePos()
#玩家座標有3個值,所以開3個變數
    mc.postTo('You rae located on X:'+str(x)
                               +',Y:'+str(y)
                               +',Z:'+str(z))
#說出You rae located on x,y,z(x,y,z是玩家座標)
