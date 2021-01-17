                        # Space Invader 
                        
            # Travail fourni par COEZ Raphael, CLEMENT Charles   
    
     # import des objets necessaires

from tkinter import Tk,Canvas,StringVar, Label, Button, Menu, Menubutton
from random import randint

    # classe : vaisseau spatial

class spaceship:
    def __init__(self,pos_x,pos_y,pv):
        self.__pos_x=pos_x
        self.__pos_y=pos_y
        self.__pv=pv
        self.__formes=[]
    
    def get_pos_x(self):
        return self.__pos_x

    def get_pos_y(self):
        return self.__pos_y
    
    def get_pv(self):
        return self.__pv
    
    def get_formes(self):
        return self.__formes
    
    def set_pos_x(self,newpos):
        self.__pos_x=newpos

    def set_pos_y(self,newpos):
        self.__pos_y=newpos
    
    def set_pv(self,newpv):
        self.__pv=newpv
    
    def set_forme(self,newf): # methode permettant d'ajouter a la liste des formes tkinter une forme faisant partie du vaisseau
        self.__formes.append(newf)

    def check_pv(self): # methode permettant de vérifier et d'afficher en permanence le nombre correct de points de vies
        global pv, pv_label
        if pv!=vaisseau.get_pv():
            pv=vaisseau.get_pv()
            pv_label.destroy()
            pv_label=Label(interface,text='Pv = '+str(pv),fg='black')
            pv_label.pack()
        if self.__pv==0:
            game_over()
        else:
            interface.after(1,self.check_pv)

    # classe : alien

class alien :
    def __init__(self,pos_x,pos_y,pv,_type):
        self.__pos_x=pos_x
        self.__pos_y=pos_y
        self.__pv=pv
        self.__type=_type
        self.__formes=[]

    def set_pos_x(self,newpos):
        self.__pos_x=newpos

    def set_pos_y(self,newpos):
        self.__pos_y=newpos

    def set_pv(self,newpv):
        self.__pv=newpv
    
    def get_pos_x(self):
        return self.__pos_x

    def get_pv(self):
        return self.__pv
    
    def get_pos_y(self):
        return self.__pos_y
    
    def get_type(self):
        return self.__type

    def set_formes(self,newform): # methode permettant d'ajouter a la liste des formes tkinter une forme faisant partie de l'alien
        self.__formes.append(newform)

    def get_formes(self):
        return self.__formes
    
    def tir_alien(self): # methode permettant de creer un tir a l'endroit ou se trouve l'alien
        X=canvas.coords(self.get_formes()[3])[2]
        Y=canvas.coords(self.get_formes()[3])[3]
        canvas.create_line(X,Y+10,X,Y+30,width=3,fill='blue',tag='tir_alien')


def generer_forme_alien(alien): # fonction permettant de generer les formes qui composent les aliens
    global canvas
    type_alien=alien.get_type()
    pos_x=alien.get_pos_x()
    pos_y=alien.get_pos_y()
    if type_alien==1:
        forme_1=canvas.create_rectangle(pos_x, pos_y, pos_x +15, pos_y +15,fill="blue")
        pos_x+=17
        forme_2=canvas.create_rectangle(pos_x,pos_y,pos_x +15,pos_y +15,fill="blue")
        pos_x+=17
        forme_3=canvas.create_rectangle(pos_x,pos_y,pos_x +15,pos_y +15,fill="blue")
        pos_y+=17
        pos_x+=(-17)
        forme_4=canvas.create_rectangle(pos_x,pos_y,pos_x +15,pos_y +15,fill="blue")
        alien.set_formes(forme_1)
        alien.set_formes(forme_2)
        alien.set_formes(forme_3)
        alien.set_formes(forme_4)

def attaque_alien(): # fonction permettant l'envoi aléatoire d'un tir alien régulièrement
    global liste_aliens
    n=len(liste_aliens) 
    numero=randint(0,n-1) 
    dt=randint(500,2000) 
    liste_aliens[numero].tir_alien() 
    interface.after(dt,attaque_alien) 

def mouvement_alien_1(): # fonction controlant le mouvement des aliens de la première ligne
    global canvas, liste_aliens_1, dx, dy
    if len(liste_aliens_1) != 0 :
        first_alien=liste_aliens_1[0]
        last_alien=liste_aliens_1[-1]
        x1_f=canvas.coords(first_alien.get_formes()[0])[0]
        x2_l=canvas.coords(last_alien.get_formes()[2])[2]
        if x2_l>950:
            dx=-5
        elif x1_f<50:
            dx=5
            dy=10
        elif x1_f>50:
            dy=0
        for i in liste_aliens_1 :
            formes=i.get_formes()
            for j in formes :
                canvas.move(j,dx,dy)
                perte_par_descente()
        canvas.after(20,mouvement_alien_1)

def mouvement_alien_2(): # fonction controlant le mouvement des aliens de la seconde ligne
    global canvas, liste_aliens_2, dx, dy
    if len(liste_aliens_2) != 0 :
        first_alien=liste_aliens_2[0]
        last_alien=liste_aliens_2[-1]
        x1_f=canvas.coords(first_alien.get_formes()[0])[0]
        x2_l=canvas.coords(last_alien.get_formes()[2])[2]
        if x2_l>950:
            dx=-5
        elif x1_f<50:
            dx=5
        for i in liste_aliens_2 :
            formes=i.get_formes()
            for j in formes :
                canvas.move(j,dx,dy)
        canvas.after(20,mouvement_alien_2)

def mouvement_alien_3(): # fonction controlant le mouvement des aliens de la troisième ligne 
    global canvas, liste_aliens_3, dx
    if len(liste_aliens_3) != 0 :
        first_alien=liste_aliens_3[0]
        last_alien=liste_aliens_3[-1]
        if len(first_alien.get_formes())==4:
            x1_f=canvas.coords(first_alien.get_formes()[0])[0]
        if len(last_alien.get_formes())==4:
            x2_l=canvas.coords(last_alien.get_formes()[2])[2]
        if x2_l>950:
            dx=-5
        elif x1_f<50:
            dx=5
        for i in liste_aliens_3 :
            formes=i.get_formes()
            for j in formes :
                canvas.move(j,dx,dy)
        canvas.after(20,mouvement_alien_3)


def generer_vaisseau(X,Y,l=15,h=15): # fonction permettant de générer les formes composant le vaisseau allié
    global canvas, vaisseau
    vaisseau.set_forme(canvas.create_rectangle(X, Y, X + l, Y + h, fill='red'))
    X+=l+2
    vaisseau.set_forme(canvas.create_rectangle(X, Y, X + l, Y + h, fill='red'))
    Y-=h+2
    vaisseau.set_forme(canvas.create_rectangle(X, Y, X + l, Y + h, fill='red'))
    Y += h+2
    X+= l+2
    vaisseau.set_forme(canvas.create_rectangle(X, Y, X + l, Y + h, fill='red'))

def mouvement_vaisseau_droite(event): # fonction gérant le mouvement horizontal droite du vaisseau
    global canvas, vaisseau
    if canvas.coords(vaisseau.get_formes()[3])[2]<970:
        for i in vaisseau.get_formes() :
            canvas.move(i,5,0)
    

def mouvement_vaisseau_gauche(event): # fonction gérant le mouvement horizontal gauche du vaisseau
    global canvas, vaisseau
    if canvas.coords(vaisseau.get_formes()[0])[0]>30:
        for i in vaisseau.get_formes() :
            canvas.move(i,-5,0)

def mouvement_tir_alien(): # fonction gérant le mouvement de tous les tirs aliens actuellement affichés sur le canvas
    global canvas
    canvas.move('tir_alien', 0, 10)
    canvas.update()
    interface.after(100,mouvement_tir_alien)

def check_tir_alien():  # fonction vérifiant a tout instant si un tir alien touche le vaisseau
    global vaisseau, canvas
    for i in canvas.find_withtag('tir_alien'):
        x1,y1=canvas.coords(vaisseau.get_formes()[0])[0],canvas.coords(vaisseau.get_formes()[0])[1]-17
        x2,y2=canvas.coords(vaisseau.get_formes()[2])[2],canvas.coords(vaisseau.get_formes()[2])[3]
        if i in canvas.find_overlapping(x1,y1,x2,y2):
            canvas.delete(i)
            vaisseau.set_pv(vaisseau.get_pv()-1)
    interface.after(1,check_tir_alien)

def generer_aliens(): # fonction permettant de génerer tous les objets de type alien avant le début de la partie
    global canvas
    pos_xb=40
    pos_yb=30
    for i in range(18):
        if i < 6 :
            liste_aliens_1.append(alien(pos_xb,pos_yb,1,1))
            pos_xb+=80
        if i==6 :
            pos_yb+=50
            pos_xb=40
        if i > 5 and i < 12 :
            liste_aliens_2.append(alien(pos_xb,pos_yb,1,1))
            pos_xb+=80
        if i==11 :
            pos_xb=40
            pos_yb+=50
        if i > 11 :
            liste_aliens_3.append(alien(pos_xb,pos_yb,1,1))
            pos_xb+=80
    for a in liste_aliens_1:
        generer_forme_alien(a)
        liste_aliens.append(a)
    for a in liste_aliens_2:
        generer_forme_alien(a)
        liste_aliens.append(a)
    for a in liste_aliens_3:
        generer_forme_alien(a)
        liste_aliens.append(a)
        
def start_game(): # fonction permettant de lancer le jeu par l'intermédiaire du bouton start
    global start
    if start ==0 :
        start=1
        generer_vaisseau(470,500)
        vaisseau.check_pv()
        generer_aliens()
        mouvement_alien_1()
        mouvement_alien_2()
        mouvement_alien_3()
        interface.bind('<Right>', mouvement_vaisseau_droite )
        interface.bind('<Left>', mouvement_vaisseau_gauche)
        interface.bind('<space>',debut_tir)
        attaque_alien()
        mouvement_tir_alien()
        check_tir_alien()
        actualiser_tir_vaisseau()
        supprimer_tir_vaisseau()
        supprimer_tir_alien()
        touche_alien()
        placer_boucliers(400,110)

def perte_par_descente(): # fonction gérant le game over dans le cas ou les aliens tombent trop bas
    global vaisseau
    if liste_aliens_3 != []:
        y2=canvas.coords(liste_aliens_3[0].get_formes()[3])[3]
    elif liste_aliens_2 != []:
        y2=canvas.coords(liste_aliens_2[0].get_formes()[3])[3]
    else :
        y2=canvas.coords(liste_aliens_1[0].get_formes()[3])[3]
    if y2 >= canvas.coords(vaisseau.get_formes()[2])[1]:
        game_over()


def game_over(): # fonction gérant le programme en cas d'activation d'une condition de défaite
        global interface, canvas, start_button
        canvas.destroy()
        start_button.destroy()
        perdu= Label(interface, text="Game Over : ")
        perdu.pack()


def placer_boucliers(debut_ligne, debut_colonne): # fonction générant le bouclier 
    global bouclier, canvas
    taille = 10 
    blocs = []
    rangee=1
    colonne=1
    for rangee in range(6) :
        for colonne in range(10):
            debut_colonne += taille
            for ligne in range(4):
                Y = debut_ligne + ((1 + ligne) * taille)
                blocs.append(canvas.create_rectangle(debut_colonne, Y, debut_colonne + taille, Y + taille, fill = 'grey'))
            bouclier.append(blocs)
        debut_colonne += 30

def debut_tir(event): # fonction permettant la création des tirs alliés
    global vaisseau, canvas
    r = 3
    x1,y1,x2=canvas.coords(vaisseau.get_formes()[2])[0],canvas.coords(vaisseau.get_formes()[2])[1],canvas.coords(vaisseau.get_formes()[2])[2]
    canvas.create_oval((x2+x1)/2-r,y1-2*r,(x2+x1)/2+r,y1,fill='grey',tag='tirvaisseau')


def actualiser_tir_vaisseau(): # fonction permettant le mouvement des tirs alliés actuellement affichés sur le canvas
    global canvas
    canvas.move('tirvaisseau', 0, -10)
    canvas.update()
    interface.after(100,actualiser_tir_vaisseau)

def supprimer_tir_vaisseau(): # fonction gérant la suppression des tirs alliés dans le cas ou ils quittent l'interface
    global canvas
    for i in canvas.find_withtag('tirvaisseau'):
        y1=canvas.coords(i)[1]
        if y1 < 20:
            canvas.delete(i)
            canvas.update()
    interface.after(100,supprimer_tir_vaisseau)

def supprimer_tir_alien():  # fonction gérant la suppression des tirs aliens dans le cas ou ils quittent l'interface
    global canvas
    for i in canvas.find_withtag('tir_alien'):
        y1=canvas.coords(i)[1]
        if y1 < 20:
            canvas.delete(i)
            canvas.update()
    interface.after(100,supprimer_tir_alien)

        
def touche_alien():  # fonction permettant de vérifier a tout moment si un alien est touché par un tir allié (inachevée)
    global canvas, score, liste_aliens
    for alien in liste_aliens :
        if len(alien.get_formes())==4:
            x1,y1=canvas.coords(alien.get_formes()[0])[0],canvas.coords(alien.get_formes()[0])[1]
            x2,y2=canvas.coords(alien.get_formes()[2])[2],canvas.coords(alien.get_formes()[2])[3]+17
        k=0
        for val in canvas.find_withtag('tirvaisseau'):
            if val in canvas.find_overlapping(x1,y1,x2,y2):
                for h in alien.get_formes():
                    liste_aliens=liste_aliens[0:k]+liste_aliens[k+1:]
                    canvas.delete(h)
                    canvas.delete(val) 
                    canvas.update()
                    score+=100    
            k+=1
    interface.after(1,touche_alien)

        # génération des objets necessaires au bon fonctionnement du programme
start=0
liste_aliens=[]
liste_aliens_1=[]
liste_aliens_2=[]
liste_aliens_3=[]
vaisseau=spaceship(470,500,3)
pv=vaisseau.get_pv()
bouclier=[]
score=0
interface= Tk()
interface.title("Space Invader")
interface.geometry('1200x700')
canvas = Canvas(interface,width=1000,height=600,bg='white')
canvas.pack(side="left")
start_button=Button(interface,text="Start Game",fg="black",command=start_game)
start_button.pack()
quit_button=Button(interface,text="Quit Game",fg="black",command=interface.destroy)
quit_button.pack()
score_label= Label(interface,text='Score = '+str(score),fg="black")
score_label.pack()
pv_label=Label(interface,text='Pv = '+str(pv),fg='black')
pv_label.pack()
menu_barre= Menu(interface)
diff_menu=Menu(menu_barre,tearoff=0)
menu_barre.add_cascade(label="Difficulté")
interface.config(menu= menu_barre)

        # programme principal 

interface.mainloop()