---
name: darija-shorts-script
description: Prépare un script prêt à lire, en darija marocaine, pour une vidéo verticale courte (YouTube Shorts, Instagram Reels, Facebook Reels, TikTok), plus un titre et une description à copier-coller. Cherche les informations dans la documentation officielle et les blogs reconnus, choisit un hook adapté au sujet, écrit un script de 30 s à 2 min 30 et vérifie les faits. À utiliser dès que l'utilisateur dit « fais-moi un script pour [sujet] », « prépare un short / un reel / un TikTok sur... », « écris-moi un script en darija », « donne-moi un hook », « titre et description pour ma vidéo », ou qu'il donne un sujet (gaming, nouveau site web, commande en ligne de commande, cloud, concept tech) en demandant une vidéo courte, même sans prononcer le mot « skill ». Also use for "write me a script about X for a short/reel/TikTok".
---

# Script de short en darija

À partir d'un sujet, produit deux fichiers que l'utilisateur utilise tels quels :

- `<slug>-script.md` : le script à lire face caméra, avec les sources en bas.
- `<slug>-description.md` : un titre et une description sans aucune mise en forme, à copier-coller sur les plateformes.

L'utilisateur enregistre en lisant le script. Tout ce dont il a besoin doit se trouver dans ces deux fichiers : il ne doit rien avoir à chercher ailleurs. Un script doit d'abord être facile à lire d'un coup d'œil, en filmant.

## Choix déjà faits (ne pas les redemander)

- **Plateformes** : YouTube Shorts, Instagram Reels, Facebook Reels et TikTok. Une seule version, valable partout.
- **Langue du script** : darija marocaine pure, écrite en alphabet arabe, à lire comme on parle. Les mots qui ne sont pas arabes (termes techniques, noms de produits, commandes) restent dans leur langue d'origine, anglais ou français, sans translittération. Détails dans `references/darija.md`.
- **Titre et description** : darija + mots-clés d'origine, hashtags en lettres latines sauf le premier (voir la règle de direction).
- **Adresse au spectateur** : singulier (كتعرف، شوف).
- **Durée** : de 30 s à 2 min 30, jamais plus. Au-delà, c'est pénible à lire et à suivre.
- **Sujets** : variés et changeants (gaming, nouveaux sites, commandes en ligne de commande, cloud, concepts tech). Ne rien supposer sur le sujet à partir de la vidéo précédente.
- **Sources** : toutes en bas du script, hors de la zone de lecture, pour garder une trace. Elles restent dans leur langue d'origine, sans traduction.
- **Titres du script** : en français ou en anglais, au choix, sans traduction en arabe.

Si l'utilisateur demande autre chose pour une vidéo précise, sa demande du moment l'emporte.

## Règle de direction : l'alignement de chaque ligne

Un lecteur Markdown choisit le sens d'une ligne d'après son premier caractère « fort ». Une ligne qui commence par du français ou de l'anglais s'affiche de gauche à droite et mal alignée : l'utilisateur ne peut plus la lire en filmant.

- **Script** : écris naturellement, sans contorsion pour que chaque phrase commence par un mot arabe. Une fois le fichier écrit, lance `scripts/finalize.py` : il place le caractère invisible RLM (U+200F) au début de chaque ligne à lire, ce qui force l'affichage de droite à gauche. Si Python n'est pas disponible, insère ce caractère à la main devant chaque ligne à lire.
- **Description** : c'est du texte copié-collé tel quel, donc aucun caractère invisible (il serait collé dans les légendes et pourrait empêcher une plateforme de reconnaître un hashtag). Le fichier est en `.md` : chaque ligne s'aligne d'après son premier caractère fort, donc commence chaque ligne par un mot arabe (réécris la phrase, ou mets devant un petit mot arabe : ال، و، ف، ل، هاد) et mets un hashtag arabe en premier (#تقنية، #معلوميات، #ألعاب).
- **Titres, étiquettes et sources** : ils peuvent rester en français, en anglais ou dans la langue d'origine. Ce ne sont pas des lignes à lire.

Les accents graves, `**`, `>`, `-`, `#` et les chiffres sont neutres : ils ne décident pas de la direction.

## Ne pas deviner : demander

L'utilisateur ne veut pas de prédictions. Quand il manque une information ou qu'un choix lui appartient, pose la question avec des options concrètes : utilise l'outil de questions à choix (AskUserQuestion) s'il est disponible, sinon une liste numérotée. 2 à 4 options, ta recommandation en premier, une phrase par option. Regroupe toutes les questions d'un même moment en un seul envoi.

Demande quand :

- le sujet est large : propose 2 à 4 angles possibles ;
- la durée n'est pas donnée : propose des options dans la plage 30 s – 2 min 30, recommande celle qui correspond à la complexité du sujet ;
- les sources sont introuvables, trop anciennes ou se contredisent : expose le désaccord et demande ce qu'il faut retenir ;
- un mot ou une orthographe en darija est vraiment incertain.

Ne demande pas ce que tu peux trancher toi-même : le hook, la structure, le ton, le titre. Choisis, et dis en une ligne pourquoi.

Ne jamais inventer un fait technique (commande, option, prix, date, nom de fonctionnalité, version). Si les sources ne le confirment pas, ne l'écris pas dans le texte lu.

## Workflow

### 1. Cadrage

Relève dans le message le sujet et, s'il est donné, la durée. Pose uniquement les questions qui manquent (angle, durée), en un seul envoi. Si tout est clair, passe directement à la recherche.

### 2. Recherche

Cherche d'abord dans la documentation officielle, puis dans les blogs et ressources reconnus pour compléter (exemples concrets, erreurs fréquentes, contexte). Utilise WebSearch et WebFetch. Si tu n'as pas d'accès web, demande à l'utilisateur de te fournir les sources.

Où chercher selon le sujet :

| Type de sujet | Sources à privilégier |
|---|---|
| Concept tech, cloud | Documentation du fournisseur (AWS, Google Cloud, Azure, Cloudflare...), MDN, RFC |
| Commande en ligne de commande | Page man, `--help`, documentation officielle de l'outil, dépôt GitHub officiel |
| Nouveau site ou outil | Site officiel, documentation, changelog, page de tarifs |
| Gaming | Site de l'éditeur, notes de mise à jour, page Steam ou de la plateforme |

Ce que tu dois en sortir : l'idée centrale en une phrase, les points essentiels (voir plus bas combien), un exemple concret ou une analogie, et le piège ou l'erreur fréquente si elle existe. Écarte le reste : la durée décide de ce qui reste.

- Reformule toujours avec tes mots, ne recopie aucune phrase d'une source.
- Vérifie la date et la version : une commande, un prix ou une fonctionnalité peut avoir changé.
- Note le titre et l'URL de chaque source réellement consultée pour la fin du script.

### 3. Hook

Il y a toujours un hook. Lis `references/hooks.md`, choisis le type qui correspond au sujet et écris-le en darija. Prévois aussi 2 hooks alternatifs de types différents pour le bas du script.

### 4. Écriture

Budget de mots, à raison d'environ 130 mots par minute en comptant les pauses (estimation à ajuster, voir plus bas) :

| Durée | Mots (environ) | Points à traiter |
|---|---|---|
| 30 s | 65 | 1 |
| 45 s | 100 | 1 à 2 |
| 1 min | 130 | 2 |
| 1 min 30 | 195 | 2 à 3 |
| 2 min | 260 | 3 à 4 |
| 2 min 30 (maximum) | 325 | 3 à 5 |

Structure :

1. **Hook** : première ligne de 10 mots maximum, aucune formule d'introduction avant.
2. **Contexte** : pourquoi ça compte, en 1 à 2 phrases.
3. **Idées** : une par point, chacune avec un titre court visible dans le script pour se repérer en filmant.
4. **Clôture** : résume l'idée en une phrase, puis un seul appel à l'action simple (suivre, enregistrer, commenter). Si le hook était une question, la réponse est donnée ici, clairement.

Écris en suivant `references/darija.md`. Lis-le avant d'écrire : le script doit sonner comme quelqu'un qui parle, pas comme un texte.

Le débit de 130 mots par minute vient de sources anglophones. Si l'utilisateur donne son rythme réel (par exemple « 100 mots, c'est 48 s »), passe-le au script avec `--wpm` et signale-lui qu'il peut le garder comme référence.

### 5. Finalisation

Écris les deux fichiers, puis lance le script fourni avec le skill. `scripts/` se trouve dans le dossier de ce skill (celui qui contient ce SKILL.md), pas dans le dossier de travail : utilise son chemin complet. Selon le système, la commande est `python` ou `python3`.

```
python <dossier du skill>/scripts/finalize.py <slug>-script.md <slug>-description.md
```

Il fait trois choses dans le script : ajouter les marques de direction, calculer les repères de temps de chaque titre et la ligne « Durée », compter les mots par section. Il contrôle aussi la description. Corrige tout ce qu'il signale (ATTENTION), puis relance-le jusqu'à ce qu'il n'y ait plus de problème.

### 6. Vérification

Relis le script avec cette liste avant de livrer :

1. **Faits** : chaque affirmation technique vient d'une source consultée. Commandes, options, chiffres, dates et noms exacts. Ce que tu n'as pas pu confirmer va dans « À vérifier » en bas, jamais dans le texte lu. Pour une commande, distingue une option en ligne de commande (avec ses tirets exacts : `-x`, `--exclude`) d'une touche dans une interface (sans tiret : `d`, `q`) : vérifie dans la documentation laquelle c'est, et écris « ضغط على » devant une touche pour que ce soit clair à l'oral.
2. **Durée** : entre 65 et 325 mots (le script de finalisation le contrôle).
3. **Hook** : 10 mots maximum, on comprend de quoi parle la vidéo, et le contenu tient la promesse.
4. **Darija** : aucune tournure d'arabe standard, ponctuation arabe, mots techniques dans leur langue d'origine, adresse au singulier.
5. **Lisibilité** : une idée par ligne, une ligne vide entre deux lignes, titre principal et résumé des idées en haut, titres de section en H4.
6. **Description** : les règles de la section suivante sont respectées.

### 7. Titre et description

Fichier `.md` pour que chaque ligne s'affiche de droite à gauche, mais **sans aucune mise en forme Markdown** (pas de `#` de titre, pas de `**`, pas de puces, pas d'étiquettes comme « Titre : »), parce que l'utilisateur copie et colle directement. Sépare chaque ligne de la suivante par une ligne vide : sans elle, Markdown les fusionne en un seul paragraphe et le copier-coller perd les retours à la ligne. Structure exacte :

```
<Titre>

<Phrase d'accroche>

<Une ou deux lignes de contexte, chacune séparée par une ligne vide>

#<mot arabe> #<mot-clé> #<mot-clé>
```

Règles :

- **Titre** : 60 caractères maximum, commence par un mot arabe avec le mot-clé principal dans les premiers mots, fidèle au contenu, pas de MAJUSCULES intégrales, pas d'emoji. YouTube limite à 100 caractères, mais un titre court reste lisible sur mobile.
- **Phrase d'accroche** : 125 caractères maximum. C'est ce qui reste visible avant « plus » sur plusieurs plateformes. Elle doit donner envie de regarder, pas répéter le titre.
- **Contexte** : une ou deux lignes courtes. En tout, environ 300 caractères hors hashtags, ce qui passe sur les quatre plateformes.
- **Hashtags** : 3 à 5, sans espace dans un hashtag, liés au sujet. Le premier est en arabe (règle de direction), les suivants en lettres latines. Pas de hashtag trompeur. Pas de `#Shorts` par défaut : YouTube classe en Short selon le format (vertical ou carré, 3 min maximum), pas selon un hashtag.
- **Mots-clés** : 1 ou 2 mots-clés principaux présents dans le titre et dans la phrase d'accroche.
- **Direction** : chaque ligne commence par un mot arabe, et aucun caractère invisible.

La première ligne sert de titre YouTube. Tout ce qui suit sert de description sur YouTube et de légende sur Instagram, Facebook et TikTok. Précise-le à l'utilisateur dans ta réponse.

Les limites et conseils des plateformes sont dans `references/plateformes.md`, avec leur niveau de fiabilité. Ne les cite pas comme des certitudes si elles sont marquées « Non confirmé ».

### 8. Livraison

Les deux fichiers sont dans le dossier de travail courant, ou dans celui que l'utilisateur indique. Le slug est en minuscules latines, sans accent, avec des tirets.

Réponds ensuite en quelques lignes : durée estimée et nombre de mots, type de hook choisi et pourquoi, liens vers les deux fichiers, et ce qui reste à vérifier s'il y en a. Ne recopie pas le script dans la réponse : l'utilisateur le lit dans le fichier.

## Modèle du script

Respecte cette structure. Elle est faite pour être lue en filmant : un grand titre et un résumé pour survoler le script, puis des lignes courtes, une idée par ligne. Les mots entre chevrons sont à remplacer.

```markdown
# <Sujet en quelques mots>

Durée : ~<n> s · <n> mots · Hook : <type>

Idées : <idée 1> · <idée 2> · <idée 3>

---

#### Hook · 0-6 s

**<première ligne, 10 mots maximum>**

<ligne>

#### Contexte · 6-16 s

<ligne>

<ligne>

#### Idée 1 · <titre court> · 16-28 s

<ligne>

<ligne>

> Écran : <ce qui s'affiche, par exemple la commande>

#### Idée 2 · <titre court> · 28-41 s

<ligne>

<ligne>

#### Clôture · 41-46 s

<ligne de résumé>

<appel à l'action>

---

#### À ne pas lire

**Sources**
- <titre de la page> : <URL>

**Hooks alternatifs**
- <type> : <ligne>
- <type> : <ligne>

**À vérifier**
- <fait non confirmé, seulement s'il y en a>
```

Règles de mise en page :

- **Haut du fichier** : un seul titre en H1 (le sujet), puis la durée et le type de hook, puis la ligne « Idées » qui résume le contenu en 3 à 5 repères de quelques mots chacun. Ça permet de survoler le script sans le lire en entier.
- **Séparateur** : une ligne `---` entre ce résumé et le texte à lire, et une autre avant la partie « À ne pas lire ».
- **Titres de section** : en H4 (`####`), jamais en H1, H2 ou H3 (sauf le titre du haut). Ce sont des repères discrets.
- **Une idée = une ligne.** Une phrase par ligne, 6 à 12 mots, jamais de paragraphe. Mets une ligne vide entre deux lignes : sans elle, Markdown les fusionne en un seul bloc de texte chargé.
- Mets en **gras** les 1 ou 2 mots à appuyer dans la ligne, pas plus.
- Les repères de temps des titres et la ligne « Durée » sont recalculés par `scripts/finalize.py` : écris des valeurs approximatives, le script les corrige.
- Les lignes `> Écran :` sont facultatives et ne sont pas lues. Mets-en seulement quand un visuel aide (une commande, un nom de menu), avec peu de texte : Instagram réduit la visibilité des vidéos surtout composées de texte.
- Les commandes et le code vont entre accents graves.
- Tout ce qui n'est pas à lire est sous « À ne pas lire » ou sur une ligne `>`.
