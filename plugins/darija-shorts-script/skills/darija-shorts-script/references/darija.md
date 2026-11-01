# Writing Moroccan Darija to be read aloud

The user reads the script as-is, as if speaking. If a sentence sounds "bookish" or like the TV news, rewrite it the way you would say it to a friend or a colleague.

## Principles

- **Arabic script**, without vowels (no tashkeel).
- **Short sentences**: one idea per line, 6 to 10 words, one breath per line.
- **Spoken word order**, with no long asides or cascading subordinate clauses.
- **Arabic punctuation**: `،` and `؟`, and `...` for a pause.
- **Register**: a colleague explaining, energetic but natural. No needless jargon, no insults, light humor is welcome.
- **Numbers** in Latin digits (30 ثانية, not ثلاثون).

## Words that are not Arabic

- Technical terms, product names, commands, acronyms: **original language, Latin letters, never transliterated** (write `DNS`, not دي إن إس).
- Form to use: the one in the official documentation, most often English. For everyday tech words of French origin (serveur, commande, entretien), both forms are acceptable: stay consistent throughout the script. User preference: write `entretien` in Latin letters, never `interview`.
- **Preposition in front of a Latin word**: separate it with a space (`ف Git`, `ب Linux`, `ل AWS`).
- **Start of line**: in the script, write naturally, even if a line starts with a Latin word or a command. `scripts/finalize.py` then places an invisible character at the start of each line to keep the right-to-left alignment. Only the description, copy-pasted as-is, must start each line with an Arabic word. Details in the direction rule of `SKILL.md`.
- **Commands and code**: in backticks (`ls -la`), so they stand out when reading.
- **Pronunciation**: if an acronym can be read in two ways, add a short note under "À ne pas lire" (the "Do not read" section of the script), not in the text that is read.

## Avoiding Standard Arabic

Darija varies from region to region, and this list is neither exhaustive nor normative. It gives the most useful reflexes.

| Standard Arabic (avoid) | Darija (write) |
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

Spoken grammar reminders:

- Present tense with prefix: كيدير، كتكتب، كنشوف، كيخدم.
- Future: غادي + verb (غادي تفهم).
- Negation: ما ... ش (ما كيخدمش).
- Linking words: ملي (when), إلا (if), باش (in order to), حيت (because), ولا (or), ماشي (is not).

## User corrections

When the user corrects a word or a spelling, apply it for the rest of the conversation and offer to add that preference here. If you are truly unsure about a word, choose the form most common in Morocco, or ask the user rather than deciding at random.
