import numpy as np
import matplotlib.pyplot as plt
from control import matlab

# remplace matlab.tf par tf, matllab.step par step,....
from control.matlab import impulse, step, bode, dcgain, initial
from control.matlab import  tf, poles, damp, series, feedback, zpk, pzmap, linspace, logspace
k=13
M=0.062
h_v = 0.5 #coeff d'amortissement (doit etre inférieur à 1)
omega_0 = np.sqrt(k/M)
Q = np.sqrt(k*M)/h_v

# Définition du numérateur et du dénominateur
num = [1,0,0] #ordre s décroissant 
denom = [1, (omega_0/Q), omega_0**2] # ordre s décroissant
# Création de la fonction de transfert H=(s+2)/(3s^2+4s+5)
H=tf(num,denom)
impulse(H)
# #Réponse impulsionnelle
yimp,t = impulse(H)

# Affichage de la réponse
plt.plot(t, yimp)
plt.grid(True)
plt.xlabel("Temps (s)")
plt.ylabel("Position (m))")
plt.title("Réponse impulsionnelle")
plt.tight_layout()
plt.savefig("reponse_imp_test.pdf", format="pdf")
#plt.xticks(fontsize=14)
plt.show()

#%% rep impulsionnelle 
import numpy as np
import matplotlib.pyplot as plt
from control.matlab import impulse, step, bode, dcgain, initial
from control.matlab import tf, poles, damp, series, feedback, zpk, pzmap, linspace, logspace

# Paramètres du système
k = 13
M = 0.062
h_v = 0.5  # Coefficient d'amortissement (doit être inférieur à 1)
omega_0 = np.sqrt(k/M)
Q = np.sqrt(k*M)/h_v

# Définition du numérateur et du dénominateur
num = [1, 0, 0]  # Ordre s décroissant
denom = [1, (omega_0/Q), omega_0**2]  # Ordre s décroissant

# Création de la fonction de transfert
H = tf(num, denom)

# Réponse impulsionnelle
yimp, t = impulse(H)

# Affichage de la réponse
plt.plot(t, yimp)
plt.grid(True)
plt.xlabel("Temps (s)")
plt.ylabel("Position (m)")
plt.title("Réponse impulsionnelle")
plt.tight_layout()
plt.savefig("reponse_imp_test.pdf", format="pdf")
plt.show()


#%%

k = 2
m = 0.062
h = 0.50

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, bode

# Paramètres du filtre
omega_0 = np.sqrt(k/m)  # Fréquence propre en rad/s
Q = np.sqrt(k*m)/h  # Facteur de qualité
print(f"Facteur de qualité Q: {Q:.2f}")

# Définition de la fonction de transfert H(s) = s^2 / (w0^2 + (w0/Q) s + s^2)
numerator = [1, 0, 0]  # s^2
denominator = [1, omega_0/Q, omega_0**2]

# Création de la fonction de transfert
system = TransferFunction(numerator, denominator)

# Calcul de la réponse en fréquence
w, mag, phase = bode(system)

# Fréquence de référence (16.5 Hz)
f_ref = 16.5  # Hz
w_ref = 2 * np.pi * f_ref  # Conversion en rad/s

# Tracé du diagramme de Bode
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

# Gain
ax1.semilogx(w, mag, label=f"k={k}, m={m}, h={h}, Q={Q:.2f}" )  
ax1.axvline(f_ref, color='red', linestyle='--', label=f"f = {f_ref} Hz")  # Ligne verticale
ax1.set_title("Diagramme de Bode - Gain")
ax1.set_ylabel("Gain (dB)")
ax1.set_xlabel("Fréquence (Hz)")

ax1.grid(which="both", linestyle="--", linewidth=0.5)
ax1.legend()

# Phase


# Affichage
plt.tight_layout()
plt.show()
