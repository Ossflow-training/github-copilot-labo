---
applyTo: "script/**/*.py"
---
Lors d'une revue de code de ce dossier :
- Signaler tout fichier ouvert sans `with`, et toute lecture système sans gestion d'OSError.
- Signaler tout os.system, subprocess avec shell=True, except nu ou exception avalée.
- Signaler tout mot de passe, jeton ou adresse de serveur écrit en dur.
- Vérifier les conversions d'unités (octets, Go, pourcentages).
- Ne pas commenter la mise en forme : seul le fond compte.
- Pour chaque remarque, proposer la correction sous forme de suggestion de code applicable.
