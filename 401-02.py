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
    mc.postTo('You rae located on X:'+str(x)
                               +',Y:'+str(y)
                               +',Z:'+str(z))
#說出You rae located on x,y,z
