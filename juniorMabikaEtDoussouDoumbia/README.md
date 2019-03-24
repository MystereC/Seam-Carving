## Rapport du projet de Seam Carving

### Sommaire
1. Introduction
2. Luminosité et energie
3. Calcul du chemin
4. Suppression
5. Interface graphique
6. Quelques tests sur des images
7. Références

### Introduction

 Le seam carving ou recadrage intelligent est un algorithme qui consiste a redimensionner une image non pas par modification 
 de l’échelle de celle-ci , mais par suppression de chemins de pixels de moindre énergie .  Pour notre projet nous avons implémenté 5 méthodes : 
*Luminosité() 
*Energy()
*EnergyImage()
*Seam()
*SupprimerSeam()
Librairie utilisé : PIL, math et numpy .

### Luminosité-Energie 

La méthode luminosité()  permet de calculer l’intensité  d’un pixel ( On définit l’intensité d’un pixel comme la moyenne arithmétique de ses composantes Rouge Vert Bleu) elle retourne cette dernière qui va nous permettre de calculer l’énergie d’un pixel grâce à la méthode énergie(). Ensuite nous ferons une boucle sur l’image  pour calculer l’énergie de chaque pixel  grâce à la méthode energyImage() , mais on omettons de calculer celle des bordures de l’image, que nous avons remplis avec une énergie élever.

### Calcul du chemin

L’approche par programmation dynamique nous permet de déterminer le chemin (le seam) d´energieminimale grâce à la notion d’´energie cumulative. Calcul des énergies cumulatives
On définit l´énergie cumulative de chaque pixel comme :
Ec(x, y) = E(x, y) pour la première ligne
Ec(x, y) = E(x, y) + min(Ec(x - 1, y - 1),Ec(x, y - 1),Ec(x + 1, y - 1)) pour les lignes 2 et plus
**Bactrack :** Afin de déterminer le chemin d’´energie minimale, on part du bas de l’image, on trouve le pixel d’énergie cumulative minimale, et on remonte récursivement en prenant a chaque fois le pixel d’au dessus d’énergie cumulative minimale (haut-gauche, haut ou haut-droit) jusqu’a atteindre le haut de l’image. A la fin de cette étape, nous avons un ensemble de pixels d’energie minimale que nous pouvons enlever de l’image afin de réduire sa largeur d’une unité, et cela ayant un impact minimal sur les informations importantes de l’image. Ainsi, l’´energie cumulative d’un pixel est son énergie plus le minimum d’énergie cumulative des trois pixels d’au dessus (haut-gauche, haut et haut-droit).

### La Suppression 

Pour supprimer le seam minimal , la méthode supprimerSeam() copie l’image originel pixel par pixel (sauf les pixel du seam) vers une image de largeur inferieur d’une unité.

### Interface Graphique  

L’interface graphique présente un barre de menu permettant d’ouvrir une image , et un bouton pour reduire la taille de l’image .
 Imports de l’interface graphique : 
1. from tkinter import *
2. import tkinter.messagebox
3. import tkinter.filedialog
4. from PIL import Image, ImageTk

### Quelques tests sur des images

![ Chats][1]
[1]: chat1.jpg "Avant"

![ Chats][2]
[2]: chat2.jpg "Après"

![ tigres][3]
[3]: tigre1.jpg "Avant"

![ tigres][4]
[4]: tigre2.jpg "Après"

![ dés][5]
[5]: de1.jpg "Avant"

![ dés][6]
[6]: de2.jpg "Après"

### Références

Seam Carving for content-Aware Image Resizing Shai Avidan, Ariel Shamir

Seam-carving and content-driven Retargeting of images (and video) Michael Rubinstein MIT
