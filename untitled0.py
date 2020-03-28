# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 10:27:07 2020

@author: Administrator
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create();
x,y,z=mc.player.getTilePos()
a=mc.getBlock(x,y-1,z+1)
b=mc.getBlock(x,y-1,z-1)
c=mc.getBlock(x-1,y-1,z)
d=mc.getBlock(x+1,y-1,z)
while True:
    if(a==8 or a==9):
        mc.setBlocks(x+1,y,z+1,x-1,y,z-1,1,1)
    if(b==8 or b==9):
        mc.setBlocks(x+1,y,z+1,x-1,y,z-1,1,1)
    if(c==8 or c==9):
        mc.setBlocks(x+1,y,z+1,x-1,y,z-1,1,1)
    if(d==8 or d==9):
        mc.setBlocks(x+1,y,z+1,x-1,y,z-1,1,1)