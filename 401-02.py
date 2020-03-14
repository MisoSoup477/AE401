# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 02:27:40 2020

@author: 學生
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create();

while True:
    x,y,z=mc.player.getTilePos()
    mc.postTo('You rae located on X:'+str(x)
                               +',Y:'+str(y)
                               +',Z:'+str(z))