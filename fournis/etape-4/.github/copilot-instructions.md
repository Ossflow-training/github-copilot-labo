# Instructions Copilot – projet mysystem-copilot

- Python 3.13 : script/mysystem (psutil, ifaddr) ; environnement virtuel .venv.
- Dépendances : requirements.txt (exécution), requirements-dev.txt (lint, tests, doc).
- Lint : pylint --disable=missing-docstring script/mysystem.
- Tests : unittest dans script/mysystem/tests, lancés avec pytest script/mysystem.
- CI : .github/workflows/ci.yml, à garder au vert.
- Pas de dépendance nouvelle sans validation du tech lead.
- Commentaires et messages en français.
- Messages de commit en français, au format Conventional Commits (`type(portée): résumé`), 10 lignes au plus ;
  le corps explique pourquoi ce commit est nécessaire, pas ce qu'il modifie.
