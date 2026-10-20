# userfind

Cherche un pseudo sur plusieurs plateformes et dit où un profil public semble
exister. C'est une version très réduite de Sherlock : on construit l'URL du
profil et on regarde si la page répond 200.

Sur soi-même ou sur un pseudo de test. Le but est de montrer comment marche
l'énumération de comptes en OSINT, pas de traquer des gens.

## Install

```
pip install -r requirements.txt
```

## Utilisation

```
python userfind.py monpseudo
```

Attention : certains sites (Instagram, TikTok) renvoient parfois 200 même pour
un profil inexistant, ou bloquent les requêtes automatiques. Donc le résultat
n'est pas fiable à 100%, c'est une limite connue de la méthode « juste le code
HTTP ».

## Pour aller plus loin

- vérifier le contenu de la page (texte "page not found") au lieu du seul code HTTP
- lancer les requêtes en parallèle
- ajouter d'autres sites, charger la liste depuis un fichier JSON
