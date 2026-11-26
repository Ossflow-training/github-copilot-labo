---
applyTo: "script/**/*.py"
description: Conventions du code Python
---
- Annotations de type sur chaque fonction.
- Fichiers ouverts avec `with`, encodage explicite ; gérer OSError sur les lectures système.
- Pas de os.system, ni de subprocess avec shell=True.
- Pas d'except nu ni d'exception avalée en silence.
- Aucun affichage ni traitement au chargement du module : tout passe par main().
