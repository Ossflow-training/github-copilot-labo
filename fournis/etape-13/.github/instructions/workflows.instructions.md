---
applyTo: ".github/workflows/*.yml"
---
- Déclarer des permissions minimales au niveau de chaque job.
- Épingler les actions tierces par SHA complet, avec la version en commentaire.
- Ne jamais insérer ${{ github.event.* }} ni ${{ secrets.* }} dans un run : passer par env.
- Utiliser pull_request, jamais pull_request_target, pour du code non fiable.
- Reprendre l'installation de la CI existante (.github/workflows/ci.yml) : Python 3.13, requirements.txt.
