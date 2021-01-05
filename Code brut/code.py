

import tkinter

    # classe vaisseau spatial

class spaceship:
    def __init__(self,_pos,_pv,_image):
        self.__pos=_pos
        self.__pv=_pv
        self.__image=_image
    
    def get_pos(self):
        return self.__pos

    def get_pv(self):
        return self.__pv
    
    def get_image(self):
        return self.__image
    
    def set_pos(self,newpos):
        self.__pos=newpos
    
    def set_pv(self,newpv):
        self.__pv=newpv
    
    def set_image(self,newimage):
        self.__image=newimage

mon_vaisseau=spaceship([1,2],20,"none")
mon_vaisseau.set_pv(10)
print(mon_vaisseau.get_pv())
print("bjr")