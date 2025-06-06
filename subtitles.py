
import time
import threading
import tkinter as tk
file='menace_fantome.srt'


def timer():
    timer = 0
    while True:
        print(timer)
        timer+=1
        time.sleep(1)

def time_to_sec(t):
    h=int(t[:2])
    m=int(t[3:5])
    s=int(t[6:8])
    return h * 3600 + m * 60 + s

def afficher_texte(texte,s_time):



    win  = tk.Tk()
    win.overrideredirect(True)

    texte = tk.Label(win, text=texte, font=("Arial", 12))

    largeur_fenetre = len(texte.cget("text").split('\n')[0]) * 10 + 5  # Ajuster la largeur en fonction du texte
    hauteur_fenetre = len(texte.cget("text").split('\n')) * 20 + 5 # Ajuster la hauteur en fonction du nombre de lignes

    ecran_largeur = win.winfo_screenwidth()
    ecran_hauteur = win.winfo_screenheight()

    # Calculer les coordonnées pour centrer en bas
    x = (ecran_largeur - largeur_fenetre) // 2
    y = ecran_hauteur - hauteur_fenetre - 50

    win.geometry(f"{largeur_fenetre}x{hauteur_fenetre}+{x}+{y}")

    texte.pack() 
    win.after(s_time, win.destroy) 
    win.mainloop()




def read(delay,curseur):
    threading.Thread(target=timer, daemon=True).start()
    

    time.sleep(delay)

    t0= time_to_sec(time.strftime("%H:%M:%S", time.localtime())) + time_to_sec(curseur)
    prev = None
    cursed = False


    with open(file, 'r', encoding='1252') as f:
        
        ligne = next(f, None)
    
        while ligne:
           
            if not cursed :
                while curseur not in ligne:
                    print(ligne)
                    ligne = next(f, None)
                    cursed = True

            print(ligne)
            next_ligne = next(f, None)
        
            if "-->" in ligne:
                t1=time_to_sec(ligne[:8]) + t0
                t2=time_to_sec(ligne[17:25]) + t0
                s_time=(t2 - t1)*1000
                if next_ligne != "":
                    s_time = s_time//2

                prev = "fleche"

            if (not ligne.strip().isdigit()) and "-->" not in ligne:
                #if prev == "fleche":
                    #time.sleep(t1 - time_to_sec(time.strftime("%H:%M:%S", time.localtime())))
                while time_to_sec(time.strftime("%H:%M:%S", time.localtime())) < t1:
                    time.sleep(0.001)
                    
                afficher_texte(ligne,s_time)
                prev = "texte"

            ligne = next_ligne
           

read(0,"00:00:19")

