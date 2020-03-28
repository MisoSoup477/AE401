# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 02:27:40 2020

@author: 學生
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create();
x,y,z=mc.player.getTilePos()
mc.setBlocks(x-2,y-1,z,x+2,y-1,z,1,1)
mc.setBlocks(x-1,y-1,z+1,x+1,y-1,z+1,1,2)
mc.setBlock(x,y-1,z+2,1,3)