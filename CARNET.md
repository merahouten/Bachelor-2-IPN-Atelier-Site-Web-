# 📒 Mon carnet de bord

**Nom :** ERAHOUTEN

**Prénom :** Mehdi

**Adresse de mon site :** https://______.pythonanywhere.com

> Modifiez ce fichier directement sur GitHub (icône crayon ✏️) pour répondre aux questions de chaque exercice.
> Écrivez avec vos propres mots : une réponse courte et juste vaut mieux qu'un long copier-coller ! 🙂

---

## 🟢 Exercice 1 — Mon premier déploiement

1. Où se trouve physiquement le code qui fabrique votre page : sur votre ordinateur, sur GitHub ou sur PythonAnywhere ?

   > _Ma réponse :_ Le code se trouve physiquement sur les serveurs de PythonAnywhere, qui l'exécutent en continu. GitHub sert uniquement d'espace de stockage et de gestion de versions pour notre code.

2. Pourquoi votre voisin(e) peut-il voir votre site, alors que vous n'avez rien installé sur son ordinateur ?

   > _Ma réponse :_ Parce que le site est hébergé sur un serveur public accessible via Internet. Son navigateur Web (le client) se connecte simplement à l'URL du site pour demander la page au serveur, sans rien avoir besoin d'installer localement

---

## 🟢 Exercice 2 — Les URL et les routes

1. Dans l'URL `https://www.google.com/maps`, quel est le nom de domaine ? Quel est le chemin ?

   > _Ma réponse :_ [www.google.com](https://www.google.com) (le serveur) et le chemin est /maps (la page spécifique demandée).

2. Que veut dire le message *Not Found* ? Qui l'a envoyé : votre navigateur ou le serveur ?

   > _Ma réponse :_ 

3. Que se passe-t-il si deux fonctions portent le même nom dans `flask_app.py` ? (Indice : essayez, puis lisez l'Error log.)

   > _Ma réponse :_ Cela signifie que la page ou la ressource demandée n'existe pas à cette adresse. C'est le serveur qui envoie ce message au navigateur.

---

## 🔵 Exercice 3 — Le langage HTML

1. Quelle est la différence entre ce que le serveur **envoie** et ce que le navigateur **affiche** ?

   > _Ma réponse :_ Flask n'arrive plus à s'y retrouver et plante (erreur 500 Internal Server Error). L'Error log montre qu'une fonction tente d'écraser une route déjà existante.

🔵 Exercice 3 — Le langage HTML

2. À quoi servent les balises `<h1>`, `<p>`, `<ul>` et `<li>` ?

   > _Ma réponse :_ <h1> définit le titre principal de la page, <p> un paragraphe de texte, <ul> crée une liste à puces non ordonnée, et <li> définit chaque élément de cette liste.

3. Pourquoi l'image s'affiche-t-elle alors qu'elle n'est pas sur votre serveur ?

   > _Ma réponse :_ L'attribut src de l'image contient l'URL exacte d'un autre serveur (Wikimedia). Le navigateur de l'utilisateur va directement télécharger l'image depuis ce serveur externe pour l'afficher.

---

## 🔵 Exercice 4 — Les templates

1. Pourquoi est-ce une bonne idée de séparer le code Python et le HTML ? (Pensez à une équipe avec un développeur et un graphiste.)

   > _Ma réponse :_ Cela permet de séparer la logique du design. Un développeur peut gérer les données en Python pendant qu'un webdesigner modifie l'interface en HTML, sans risquer de casser le travail de l'autre.

2. Les `{{ prenom }}` sont-ils remplacés par le serveur ou par le navigateur ? Comment l'avez-vous vérifié ?

   > _Ma réponse :_ Ils sont remplacés par le serveur (via Flask/Jinja) avant l'envoi de la page. On peut le vérifier en regardant le code source (Ctrl+U) dans le navigateur : les accolades ont disparu et seul le prénom final est visible.

---

## 🔵 Exercice 5 — Le CSS et les liens

1. Quelle est la différence de rôle entre le HTML et le CSS ?

   > _Ma réponse :_ Le HTML définit la structure et le contenu de la page (titres, textes), tandis que le CSS s'occupe de l'habillage visuel (couleurs, polices, marges).

2. Pour afficher votre page `/presentation`, combien de fichiers le navigateur doit-il télécharger ? (Vous pourrez le vérifier à l'exercice suivant !)

   > _Ma réponse :_ Le navigateur doit télécharger 2 fichiers : la page HTML elle-même, puis le fichier style.css qui y est lié.

3. Pourquoi faut-il parfois faire **Ctrl + F5** pour voir les changements de CSS ?

   > _Ma réponse :_ Pour forcer le navigateur à vider sa mémoire cache. Sinon, pour aller plus vite, il réutilise l'ancienne version du fichier CSS qu'il avait déjà sauvegardée localement.

---

## 🟣 Exercice 6 — Espionner le navigateur

1. Que signifie HTTP ? Qui envoie la **requête** et qui envoie la **réponse** ?

   > _Ma réponse :_ HTTP signifie HyperText Transfer Protocol. Le navigateur (client) envoie la requête, et le serveur hébergeant le site envoie la réponse.

2. Combien de requêtes votre page `/presentation` a-t-elle déclenchées ? Lesquelles ?

   > _Ma réponse :_ Trois requêtes : le fichier HTML de la page, le fichier style.css, et une requête générée automatiquement pour l'icône de l'onglet (favicon.ico).

3. Que signifie le code `200` ? Et le code `404` de la favicon ?

   > _Ma réponse :_ Le code 200 (OK) signifie que la requête a réussi et que le fichier a été envoyé. Le code 404 (Not Found) signifie que le fichier demandé n'a pas été trouvé sur le serveur.

4. Pourquoi les modifications faites dans l'onglet Éléments ne sont-elles pas visibles par les autres visiteurs ?

   > _Ma réponse :_ Ces modifications n'altèrent que l'interprétation locale du code source dans la mémoire de notre propre navigateur, pas le fichier original stocké sur le serveur.

---

## 🟣 Exercice 7 — Envoyer des informations dans l'URL

1. Dans l'URL `https://www.youtube.com/results?search_query=chat`, quel est le nom du paramètre ? Quelle est sa valeur ?

   > _Ma réponse :_ Le paramètre s'appelle search_query et sa valeur est chat.

2. Pourquoi le serveur plante-t-il avec `a=bonjour` ? Que faudrait-il faire pour l'éviter ?

   > _Ma réponse :_ Il plante car le code Python essaie de convertir le texte "bonjour" en nombre entier avec int(). Pour l'éviter, il faut utiliser un bloc try/except pour capturer l'erreur et afficher un message d'avertissement.

3. Pourquoi est-il dangereux d'afficher **tel quel** ce que l'utilisateur envoie ?

   > _Ma réponse :_ Cela permet l'injection de code (faille XSS). Un pirate pourrait envoyer un lien contenant un script malveillant qui s'exécuterait sur l'ordinateur des autres utilisateurs.

---

## 🟣 Exercice 8 — Les formulaires

1. Quelle est la différence visible entre GET et POST ?

   > _Ma réponse :_ En GET, les données saisies sont visibles à la fin de l'URL. En POST, elles sont invisibles dans l'URL car elles sont envoyées dans le corps (Payload) de la requête.

2. Pour un formulaire de **recherche**, quelle méthode choisiriez-vous ? Et pour un formulaire de **connexion avec mot de passe** ? Pourquoi ?

   > _Ma réponse :_ GET pour la recherche, car cela permet de partager le lien ou de le mettre en favori. POST pour la connexion, afin que le mot de passe n'apparaisse pas dans l'URL ni dans l'historique du navigateur.

3. Les données envoyées en POST sont-elles vraiment « secrètes » ? (Pensez à ce que vous avez vu dans l'onglet Réseau.)

   > _Ma réponse :_ Non, elles transitent en clair et sont lisibles si on intercepte la requête (comme dans l'onglet Réseau). C'est le protocole HTTPS qui se charge de chiffrer et sécuriser ces données.

---

## 🔴 Exercice 9 — Les codes de statut

1. Quelle est la différence entre une erreur `4xx` et une erreur `5xx` ? Qui est « fautif » dans chaque cas ?

   > _Ma réponse :_ Les erreurs 4xx sont la faute du client (ex: mauvaise URL tapée, accès non autorisé). Les erreurs 5xx sont la faute du serveur (ex: bug dans le code Python, base de données inaccessible).

2. Comment fonctionne une redirection ? Qui fait la deuxième requête : le serveur ou le navigateur ?

   > _Ma réponse :_ Le serveur renvoie un code 3xx avec la nouvelle adresse de destination. C'est ensuite le navigateur qui effectue automatiquement une seconde requête vers cette nouvelle adresse.

3. Donnez un exemple de situation où un vrai site utilise une redirection.

   > _Ma réponse :_ Rediriger un utilisateur non connecté vers la page de login, ou rediriger la version http:// d'un site vers sa version sécurisée https://.

---

## 🔴 Exercice 10 — Ce que le serveur sait de vous

1. Citez trois informations que le serveur connaît sur vous, sans que vous ayez rien rempli.

   > _Ma réponse :_ L'adresse IP publique, le système d'exploitation de la machine, et le type/version du navigateur Web (via le User-Agent).

2. À quoi peut servir l'en-tête `Accept-Language` pour un site comme Wikipédia ?

   > _Ma réponse :_ À détecter automatiquement la langue de l'utilisateur pour le rediriger vers la version du site qui correspond à sa langue (ex: fr.wikipedia.org).

3. Dans l'Access log, retrouvez une requête qui a reçu un code `404`. Quelle page était demandée ?

   > _Ma réponse :_ Il s'agit très souvent de la requête automatique du navigateur cherchant le fichier /favicon.ico qui n'a pas encore été créé sur le serveur.

4. Après cet exercice, que pensez-vous de la notion de « navigation anonyme » ?

   > _Ma réponse :_ La "navigation privée" empêche juste le navigateur d'enregistrer l'historique sur l'ordinateur. Sur le réseau, le serveur et le fournisseur d'accès voient toujours l'adresse IP et les pages consultées.

---

## 🔴 Exercice 11 — Le Web des machines : API et JSON

1. Quelle est la différence entre une page HTML et une réponse JSON ? À qui chacune est-elle destinée ?

   > _Ma réponse :_ Le HTML sert à structurer visuellement une page destinée à être lue par un humain. Le JSON est un format de données brutes destiné à être lu et traité par une machine (un autre programme).

2. Dans la page `/horloge`, quel code s'exécute sur le **serveur** et quel code s'exécute dans le **navigateur** ?

   > _Ma réponse :_ Le code Python (Flask) s'exécute sur le serveur pour fournir l'heure en JSON. Le code JavaScript (avec fetch()) s'exécute dans le navigateur pour interroger l'API et mettre à jour l'affichage de la page.

3. Citez une application de votre téléphone qui, selon vous, utilise une API. Quelles données échange-t-elle ?

   > _Ma réponse :_ L'application Météo. Elle envoie la position GPS au serveur, et l'API lui renvoie en JSON les températures et prévisions brutes, que l'application met ensuite en forme à l'écran.

---

## 🏁 Pour conclure

En quelques phrases, expliquez à un ami ce qui se passe entre le moment où il tape une adresse dans son navigateur et celui où la page s'affiche :

> _Ma réponse :_ Quand tu tapes une adresse Web, ton navigateur (le client) envoie une requête via Internet à un ordinateur distant allumé en permanence (le serveur). Ce serveur utilise un programme (comme Flask) pour fabriquer une réponse sur mesure. Il renvoie ensuite des données (JSON) ou du code (HTML/CSS) que ton navigateur télécharge et interprète pour afficher visuellement le site sur ton écran.
