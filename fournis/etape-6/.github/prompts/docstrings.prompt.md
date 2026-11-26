---
name: docstrings
description: Ajoute les docstrings des fonctions sélectionnées
agent: agent
---
Ajoute une docstring Google à chaque fonction de la sélection, et à elles seules :
${selection}

- en français : résumé d'une ligne, puis Args, Returns et, si besoin, Raises
- ne modifie rien d'autre : ni le code, ni les autres fonctions du fichier
- sans docstring sur les fonctions de test
- si la sélection est vide, demande quelles fonctions documenter au lieu de traiter tout le fichier
