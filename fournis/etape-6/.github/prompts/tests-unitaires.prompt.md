---
name: tests-unitaires
description: Écrit les tests unitaires d'une fonction
argument-hint: nom de la fonction à tester, par exemple is_supported_os
agent: agent
---
Écris les tests unitaires de la fonction indiquée après la commande, définie dans ${file} :
- avec unittest, dans script/mysystem/tests/test_system.py
- un test par comportement : cas nominal, valeurs limites, type invalide
- sans modifier le code de production
- lance pytest script/mysystem et corrige jusqu'au vert
