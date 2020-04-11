from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setBlocks(x-3,y+3,z+3,x+3,y,z-3,4)
mc.setBlocks(x-2,y+3,z+2,x+2,y,z-2,0)
mc.setBlocks(x-3,y+3,z+3,x+3,y+3,z-3,169)
mc.setBlocks(x-2,y+3,z+2,x+2,y+3,z-2,0)
mc.setBlocks(x-1,y+3,z+3,x,y+1,z+3,0)