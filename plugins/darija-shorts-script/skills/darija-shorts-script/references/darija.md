# Écrire en darija marocaine pour être lu à voix haute

L'utilisateur lit le script tel quel, comme s'il parlait. Si une phrase sonne « livre » ou « journal télévisé », réécris-la comme on la dirait à un ami ou à un collègue.

## Principes

- **Alphabet arabe**, sans voyelles (pas de tashkeel).
- **Phrases courtes** : une idée par ligne, 6 à 10 mots, une respiration par ligne.
- **Ordre des mots de l'oral**, sans incise longue ni subordonnée en cascade.
- **Ponctuation arabe** : `،` et `؟`, et `...` pour une pause.
- **Registre** : un collègue qui explique, énergique mais naturel. Pas de jargon inutile, pas d'insulte, un humour léger est bienvenu.
- **Chiffres** en chiffres latins (30 ثانية, pas ثلاثون).

## Mots qui ne sont pas arabes

- Termes techniques, noms de produits, commandes, sigles : **langue d'origine, lettres latines, jamais translittérés** (écrire `DNS`, pas دي إن إس).
- Forme à utiliser : celle de la documentation officielle, le plus souvent l'anglais. Pour les mots courants du quotidien tech d'origine française (serveur, commande, entretien), les deux formes sont acceptables : reste cohérent dans tout le script. Préférence de l'utilisateur : écrire `entretien` en lettres latines, jamais `interview`.
- **Préposition devant un mot latin** : sépare-la par une espace (`ف Git`, `ب Linux`, `ل AWS`).
- **Début de ligne** : dans le script, écris naturellement, même si une ligne commence par un mot latin ou une commande. `scripts/finalize.py` place ensuite un caractère invisible au début de chaque ligne pour garder l'alignement de droite à gauche. Seule la description, copiée-collée telle quelle, doit commencer chaque ligne par un mot arabe. Détails dans la règle de direction de `SKILL.md`.
- **Commandes et code** : entre accents graves (`ls -la`), pour qu'ils se distinguent à la lecture.
- **Prononciation** : si un sigle peut se lire de deux façons, ajoute une courte indication dans « À ne pas lire », pas dans le texte lu.

## Éviter l'arabe standard

La darija varie selon les régions et cette liste n'est ni exhaustive ni normative. Elle donne les réflexes les plus utiles.

| Arabe standard (à éviter) | Darija (à écrire) |
|---|---|
| ماذا | شنو |
| لماذا | علاش |
| كيف | كيفاش |
| أين | فين |
| متى | فوقاش |
| هل | واش |
| كم | شحال |
| هذا / هذه | هاد / هادي |
| الآن | دابا |
| دائما | ديما |
| جدا / كثيرا | بزاف |
| قليلا | شوية |
| فقط | غير |
| يوجد | كاين / كاينة |
| لا يوجد | ماكاينش |
| يجب / عليك | خاصك |
| يمكنك | تقدر |
| لأن / حيث | حيت |
| لكن | ولاكن |
| مثل | بحال |
| أيضا | حتى |
| سوف | غادي |
| أريد | بغيت |
| ثم / بعد ذلك | من بعد |
| مشكلة | مشكل |
| سهل / صعب | ساهل / صعيب |
| ملك / خاص بـ | ديال (الموقع ديالك) |

Rappels de grammaire orale :

- Présent avec préfixe : كيدير، كتكتب، كنشوف، كيخدم.
- Futur : غادي + verbe (غادي تفهم).
- Négation : ما ... ش (ما كيخدمش).
- Mots de liaison : ملي (quand), إلا (si), باش (pour), حيت (parce que), ولا (ou), ماشي (n'est pas).

## Corrections de l'utilisateur

Quand l'utilisateur corrige un mot ou une orthographe, applique-le pour tout le reste de la conversation et propose d'ajouter cette préférence ici. En cas de vrai doute sur un mot, choisis la forme la plus répandue au Maroc, ou demande à l'utilisateur plutôt que de trancher au hasard.
