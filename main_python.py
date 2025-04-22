# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 15:33:30 2025

@author: jules, anna, nicola, salma
"""

#%% VERSION QUI AFFICHE LA VALEUR DU CAPTEUR SEULEMENT  sans conversion 
import serial
import time      
# Configuration du port série
port = 'COM7'  # port série utilisé par la carte Arduino
baudrate = 115200  #débit en bauds, la vitesse de communication utilisée dans une connexion série, exprimée en bits par seconde 
try:
    # Ouvrir la connexion série
    arduino = serial.Serial(port, baudrate)
    print(f"Connexion établie avec {port}")
    time.sleep(2)  # Attendre que l'Arduino soit prêt

    while True:
        # Lire une ligne de données envoyée par l'Arduino
        data = arduino.readline().decode('utf-8').strip()
        if data:
            print(f"Valeur du capteur : {data}")

except serial.SerialException as e: #arret du programme dans le cas d'une erreur de connexion, exemple: carte pas branchée 
    print(f"Erreur de connexion : {e}")

except KeyboardInterrupt: #arret du programme dans le cas d'une interruption clavier 
    print("\nArrêt du programme.")

finally: # Fermeture sécurisée de la connexion série avec l'Arduino, même en cas d'erreur

    if 'arduino' in locals() and arduino.is_open:
        arduino.close()
        print("Connexion série fermée.")
#%% VERSION QUI AFFICHE LA VALEUR DU CAPTEUR SEULEMENT 
import serial
import time      

# Configuration du port série
port = 'COM7'  # port série utilisé par la carte Arduino
baudrate = 115200  #débit en bauds, la vitesse de communication utilisée dans une connexion série, exprimée en bits par seconde 

try:
    # Ouvrir la connexion série
    arduino = serial.Serial(port, baudrate)
    print(f"Connexion établie avec {port}")
    time.sleep(2)  # Attendre que l'Arduino soit prêt

    while True:
        # Lire une ligne de données envoyée par l'Arduino
        data = arduino.readline().decode('utf-8').strip()
        value = (int(data[:3])*5)/1023 #pourquoi ce calcul ?????
        if data:
            print(f"Valeur du capteur : {value}")

except serial.SerialException as e:
    print(f"Erreur de connexion : {e}")

except KeyboardInterrupt:
    print("\nArrêt du programme.")

finally:
    if 'arduino' in locals() and arduino.is_open:
        arduino.close()
        print("Connexion série fermée.")


#%% VERSION QUI TRACE SUR UN GRAPHIQUE MATPLOTLIB APRES MESURES RELEVEES 

import serial
import time
import matplotlib.pyplot as plt 

# Configuration du port série
port = 'COM7'  # Remplace COM3 par le port série utilisé par ton Arduino
baudrate = 115200  # Le baudrate doit correspondre à celui défini dans le code Arduino
#débit en bauds, la vitesse de communication utilisée dans une connexion série, exprimée en bits par seconde 
def exp_graph():
    time_exp = int(input('Quelle est la durée de l expérience souhaitée en secondes :' ))
    data_list = []
    time_list = []
    try:
        # Ouvrir la connexion série
        arduino = serial.Serial(port, baudrate)
        print(f"Connexion établie avec {port}")
        time.sleep(2)  # Attendre que l'Arduino soit prêt
        start_time = time.time()
        while time.time()-start_time<=time_exp:
            # Lire une ligne de données envoyée par l'Arduino
            data = arduino.readline().decode('utf-8').strip()
            value = (int(data)*5)/1023 #pourquoi ce calcul ?????
            if data:
                print(f"Valeur du capteur : {value}")
                data_list.append(value)
                time_list.append(time.time()-start_time)
    
    except serial.SerialException as e:
        print(f"Erreur de connexion : {e}")
    
    except KeyboardInterrupt:
        print("\nArrêt du programme.")
    
    finally:
        if 'arduino' in locals() and arduino.is_open:
            arduino.close()
            print("Connexion série fermée.")
            
    #tracé du graphe 
    plt.plot(time_list, data_list, label ='Tension éléctrique après le capteur ' )
    plt.title('Tension après le capteur en fonction du temps ')
    plt.xlabel('Temps (en s)')
    plt.ylabel('Tension (en V)')
    plt.legend()
    plt.show()
    

exp_graph()



#%% VERSION QUI TRACE SUR UN GRAPHIQUE MATPLOTLIB EN DIRECT 


import serial
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuration du port série
port = 'COM7'  # Remplacez par le port série utilisé par votre Arduino
baudrate = 115200  # Le baudrate doit correspondre à celui défini dans le code Arduino

def exp_graph():
    time_exp = int(input('Quelle est la durée de l\'expérience souhaitée en secondes : '))
    data_list = []
    time_list = []

    try:
        # Ouvrir la connexion série
        arduino = serial.Serial(port, baudrate)
        print(f"Connexion établie avec {port}")
        time.sleep(2)  # Attendre que l'Arduino soit prêt
    
        # Configuration du graphique
        fig, ax = plt.subplots()
        line, = ax.plot([], [], 'b-', label='Tension électrique après le capteur')
        ax.set_title('Tension après le capteur en fonction du temps')
        ax.set_xlabel('Temps (en s)')
        ax.set_ylabel('Tension (en V)')
        ax.legend()
        ax.set_xlim(0, time_exp)
        ax.set_ylim(0, 5)  # Ajustez selon la plage de tension attendue

        start_time = time.time()

        def update_data(frame):
            nonlocal data_list, time_list, start_time
            if time.time() - start_time <= time_exp:
                # Lire une ligne de données envoyée par l'Arduino
                data = int(arduino.readline().decode('utf-8').strip()[:3])
                if data:
                    value = (data* 5) / 1023  # Convertir la valeur lue en tension
                    print(f"Valeur du capteur : {value} V")
                    data_list.append(value)
                    time_list.append(time.time() - start_time)

            line.set_data(time_list, data_list)
            ax.set_xlim(0, max(time_list) if time_list else time_exp)
            return line,

        # Animation
        ani = animation.FuncAnimation(fig, update_data, frames=200, interval=50, blit=True, repeat=False)
        plt.show()

    except serial.SerialException as e:
        print(f"Erreur de connexion : {e}")

    except KeyboardInterrupt:
        print("\nArrêt du programme.")

    finally:
        if 'arduino' in locals() and arduino.is_open:
            arduino.close()
            print("Connexion série fermée.")

exp_graph()

####LE CODE COMMENCE ICI 

#%% VERSION QUI AFFICHE LA VALEUR DE LA DISTANCE AIMANT-CAPTEUR SEULEMENT 
import serial
import time      

# Configuration du port série
port = 'COM7'  # Remplace COM3 par le port série utilisé par ton Arduino
baudrate = 115200  # Le baudrate doit correspondre à celui défini dans le code Arduino
#débit en bauds, la vitesse de communication utilisée dans une connexion série, exprimée en bits par seconde 

def enregistrer_liste_dans_fichier(liste1,liste2,freq,periode, nom_fichier='results.txt'):
    
    with open(nom_fichier, 'w') as f: # on ouvre le fichier avec droits d'écriture
        f.write("Mesures de la distance aimant-capteur relevées en fonction du temps : (temps,distance) \n")
        for i in range(len(liste1)): 
            f.write(f"Temps : {liste1[i]}") # on écrit chaque temps 
            f.write(f"Distance : {liste2[i]}\n") # on écrit chaque distance et on passe à la ligne 
        f.write(f"Fréquence expérimentale : {freq} Hz \n")
        f.write(f"Période expérimentale : {periode} s \n")



def detecte_maxima(data_list,time_list):
    maximas = []
    time_maxima = []
    for i in range(1,len(data_list)-1):
        if data_list[i]>data_list[i-1] and data_list[i]>data_list[i+1]:
            maximas.append(data_list[i])
            time_maxima.append(time_list[i])
    return maximas,time_maxima
    
def period_freq(time_maxima):
    som = 0
    for i in range(1,len(time_maxima)-1):
        som+=time_maxima[i+1]-time_maxima[i]
    return (som/len(time_maxima),1/(som/len(time_maxima)))
        

def trouver_x(u):
    return -1.56*u+2.46 + 1.70 #on rajoute 1.70 pour se remettre au zero 
    # Aucune solution réelle trouvée

try:
    # Ouvrir la connexion série
    arduino = serial.Serial(port, baudrate)
    print(f"Connexion établie avec {port}")
    time.sleep(2)  # Attendre que l'Arduino soit prêt

    while True:
        # Lire une ligne de données envoyée par l'Arduino
        data = arduino.readline().decode('utf-8').strip()
        u = (int(data[:3])*5)/1023 #pourquoi ce calcul ?????
        if u:
            dist= trouver_x(u)
            print(f"Valeur de la distance aimant-capteur : {dist}")            
            
except serial.SerialException as e:
    print(f"Erreur de connexion : {e}")

except KeyboardInterrupt:
    print("\nArrêt du programme.")

finally:
    if 'arduino' in locals() and arduino.is_open:
        arduino.close()
        print("Connexion série fermée.")


#%% VERSION QUI AFFICHE LA DISTANCE AIMANT-CAPTEUR  et un graphe 
import serial
import time      
import matplotlib.pyplot as plt 

# Configuration du port série
port = 'COM7'  # Remplace COM3 par le port série utilisé par ton Arduino
baudrate = 115200  # Le baudrate doit correspondre à celui défini dans le code Arduino
#débit en bauds, la vitesse de communication utilisée dans une connexion série, exprimée en bits par seconde 

def detecte_maxima(data_list,time_list):
    maximas = []
    time_maxima = []
    for i in range(1,len(data_list)-1):
        if data_list[i]>data_list[i-1] and data_list[i]>data_list[i+1]:
            maximas.append(data_list[i])
            time_maxima.append(time_list[i])
    return maximas,time_maxima
    
def period_freq(time_maxima):
    som = 0
    for i in range(1,len(time_maxima)-1):
        som+=time_maxima[i+1]-time_maxima[i]
    return (som/len(time_maxima),1/(som/len(time_maxima)))


def trouver_x(u):
    return -1.56*u+2.46+ 1.70 #on rajoute 1.70 pour se remettre au zero 
    # Aucune solution réelle trouvée
    
def enregistrer_liste_dans_fichier(liste1,liste2,freq,periode, nom_fichier='results.txt'):
    
    with open(nom_fichier, 'w') as f: # on ouvre le fichier avec droits d'écriture
        f.write("Mesures de la distance aimant-capteur relevées en fonction du temps : (temps,distance) \n")
        for i in range(len(liste1)): 
            f.write(f"Temps : {liste1[i]} s") # on écrit chaque temps 
            f.write(f" Distance : {liste2[i]} cm \n") # on écrit chaque distance et on passe à la ligne 
        f.write(f"----------FIN DE L'ENREGISTREMENT DEES DONNEES----------\n")
        f.write(f"Fréquence expérimentale : {freq} Hz \n")
        f.write(f"Période expérimentale : {periode} s \n")

def exp_graph():
    time_exp = int(input('Quelle est la durée de l expérience souhaitée en secondes :' ))
    data_list = []
    time_list = []
    try:
        # Ouvrir la connexion série
        arduino = serial.Serial(port, baudrate)
        print(f"Connexion établie avec {port}")
        time.sleep(2)  # Attendre que l'Arduino soit prêt
        start_time = time.time()
        while time.time()-start_time<=time_exp:
            # Lire une ligne de données envoyée par l'Arduino
            data = arduino.readline().decode('utf-8').strip()
            
            if data and data != "":
                u = (int(data)*5)/1023 #pourquoi ce calcul ?????
                distance = trouver_x(u)
                print(f"Valeur de la distance-capteur : {distance}")
                data_list.append(distance)
                time_list.append(time.time()-start_time)
            else:
                pass
    
    except serial.SerialException as e:
        print(f"Erreur de connexion : {e}")
    
    except KeyboardInterrupt:
        print("\nArrêt du programme.")
    
    finally:
        if 'arduino' in locals() and arduino.is_open:
            arduino.close()
            print("Connexion série fermée.")
            
    print(data_list)
    
    #calcul de frequence et periode
    
    maximas,time_maxima = detecte_maxima(data_list,time_list)
    periode, freq = period_freq(time_maxima)
    print("Période des oscilliations : ",periode," s")
    print("Fréquence des oscilliations : ",freq, " Hz")
    
    #enregistrement dans fichier texte des données relevées 
    enregistrer_liste_dans_fichier(time_list,data_list,freq,periode,'results.txt')
    
    #tracé du graphe 
    plt.plot(time_list, data_list, label ='évolution de la distance aimant-capteur ' )
    plt.title('évolution de la distance aimant-capteur en fonction du temps')
    plt.xlabel('Temps (en s)')
    plt.ylabel('Distance aimant-capteur (en cm)')
    plt.legend()
    plt.show()
    
    #enregistrement du graphe dans l'ordi 
    plt.savefig("mesures_simsographe.png")
    
exp_graph()

#%% VERSION QUI TRACE SUR UN GRAPHIQUE MATPLOTLIB EN DIRECT DE LA DISTANCE EN FONCTION DU TEMPS 


import serial
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np 

# Configuration du port série
port = 'COM7'  # Remplacez par le port série utilisé par votre Arduino
baudrate = 115200  # Le baudrate doit correspondre à celui défini dans le code Arduino

def trouver_x(u):
    return -1.56*u+2.46+ 1.70 #on rajoute 1.70 pour se remettre au zero 
    # Aucune solution réelle trouvée

def detecte_maxima(data_list,time_list):
    maximas = []
    time_maxima = []
    for i in range(1,len(data_list)-1):
        if data_list[i]>data_list[i-1] and data_list[i]>data_list[i+1]:
            maximas.append(data_list[i])
            time_maxima.append(time_list[i])
    return maximas,time_maxima
    
def period_freq(time_maxima):
    som = 0
    for i in range(1,len(time_maxima)-1):
        som+=time_maxima[i+1]-time_maxima[i]
    return (som/len(time_maxima),1/(som/len(time_maxima)))

# Exemple d'utilisation
y = 1.5  # Valeur de y en volt
x = trouver_x(y)
print(f"Pour y = {y}, x ≈ {x}")

def exp_graph():
    time_exp = int(input('Quelle est la durée de l\'expérience souhaitée en secondes : '))
    data_list = []
    time_list = []
    

    try:
        # Ouvrir la connexion série
        arduino = serial.Serial(port, baudrate)
        print(f"Connexion établie avec {port}")
        time.sleep(2)  # Attendre que l'Arduino soit prêt

        # Configuration du graphique
        fig, ax = plt.subplots()
        line, = ax.plot([], [], 'b-', label='Distance aimant-capteur')
        ax.set_title('Distance aimant-capteur en fonction du temps')
        ax.set_xlabel('Temps (en s)')
        ax.set_ylabel('Distance aimant-capteur (en cm)')
        ax.legend()
        ax.set_xlim(0, time_exp)
        ax.set_ylim(-3, 3)  # Ajustez selon la plage de tension attendue

        start_time = time.time()

        def update_data(frame):
            nonlocal data_list, time_list, start_time
            if time.time() - start_time <= time_exp:
                # Lire une ligne de données envoyée par l'Arduino
                data = int(arduino.readline().decode('utf-8').strip())
                #print(data)
                if data:
                    u = (data* 5) / 1023  # Convertir la valeur lue en tension
                    dist = trouver_x(u)
                    print(f"distance aimant-capteur : {dist} cm")
                    data_list.append(dist)
                    time_list.append(time.time() - start_time)

            line.set_data(time_list, data_list)
            ax.set_xlim(0, max(time_list) if time_list else time_exp)
            return line,

        # Animation
        ani = animation.FuncAnimation(fig, update_data, frames=200, interval=50, blit=True, repeat=False)
        plt.show()
        
        #calcul de frequence et periode
        
        maximas,time_maxima = detecte_maxima(data_list,time_list)
        periode, freq = period_freq(time_maxima)
        print("Période des oscilliations : ",periode," s")
        print("Fréquence des oscilliations : ",freq, " Hz")


    

    except serial.SerialException as e:
        print(f"Erreur de connexion : {e}")

    except KeyboardInterrupt:
        print("\nArrêt du programme.")

    finally:
        if 'arduino' in locals() and arduino.is_open:
            arduino.close()
            print("Connexion série fermée.")

exp_graph()


