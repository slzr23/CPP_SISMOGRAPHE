# 📁 Projet Sismographe - CPP 2024-2025
![Photo du sismographe](mesures_simsographe.png)
## 👥 Groupe A9
- Nicola Tromelin  
- Jules Guillaume  
- Anna Haxaire  
- Salma Mamoun  
- Nathan Viel  
- **Tuteur** : Géraldine Davis  

---

## 🛍 Objectif du projet
Concevoir un **sismographe fonctionnel** capable de mesurer des vibrations verticales simulées à l'aide d'une plaque vibrante. Ce dispositif repose sur un **système masse-ressort** amorti par un **tube en cuivre** (courants de Foucault) et mesure les déplacements via un **capteur à effet Hall** connecté à une **carte Arduino**.

---

## 🧠 Démarche scientifique

### 🔬 Étude théorique
- Modélisation d’un oscillateur amorti
- Détermination de la **fonction de transfert** \( H(\omega) \)
- Recherche du **facteur de qualité optimal** \( Q \approx 0{,}707 \)

### 🔧 Construction
- Réalisation de la plaque vibrante
- Assemblage du sismographe en Lego avec masse suspendue
- Amortissement des oscillations avec **aimants** et **tube de cuivre**

### 📀 Calibration et expérimentation
- Étude du **coefficient de frottement h** via mesures dans un tube de cuivre
- Choix optimal des paramètres \(k\) (raideur du ressort) et \(m\) (masse)
- **Calibrage du capteur** : lien tension-distance validé expérimentalement

---

## 💻 Mesures et traitement

### Composants électroniques :
- **Arduino UNO**
- **Capteur à effet Hall**

### Code développé :
- Acquisition de données (Arduino + Python)
- Conversion tension → distance
- Détection automatique des oscillations
- Calcul de la fréquence et de la période
- **Affichage en direct** + sauvegarde dans un fichier `.txt`

## 🌱 Impact et éco-conception
- Matériaux majoritairement récupérés ou recyclables
- Démarche respectueuse de l’environnement

## 🚀 Améliorations possibles
- Utilisation d’une carte **ESP32** ou **Raspberry Pi** pour l’autonomie
- Envoi des données en temps réel via Wi-Fi/Bluetooth
- Ajout d’une **détection automatique de séisme**

## 📸 Aperçu

![Sismographe en fonctionnement](mesures_simsographe.png)
![Sismographe en fonctionnement](mesures_simsographe.png)
![Sismographe en fonctionnement](mesures_simsographe.png)
![Sismographe en fonctionnement](mesures_simsographe.png)
![Sismographe en fonctionnement](mesures_simsographe.png)
