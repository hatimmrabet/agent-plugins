# Choosing and writing the hook

The hook is the first line of the script. It has three seconds to say what the video is about and why to keep watching. The examples below illustrate each type: do not copy them, invent a hook tied to the real topic.

The type names are kept in French (with an English gloss) on purpose: they are written as-is in the `Hook : <type>` line and in the "Hooks alternatifs" section of the generated script.

## Rules

1. **It talks about the real content** of the video, and the content keeps its promise. YouTube says this about titles: a title that does not represent the video makes viewers leave.
2. **10 words maximum** for the first line.
3. **Nothing before the hook**: no greeting and no self-introduction (community advice, unofficial). If the user wants a greeting, put it after the hook.
4. **One promise = one answer**: if the hook asks a question, the closing answers it clearly.

## Hook types

### Question d'entretien
*Interview question.* Put yourself in the shoes of the recruiter asking the question. Very good for a concept everyone should be able to explain (DNS, GCP, API, Docker...). Give a concrete stake: what you gain from knowing how to answer.

> إلا سقساوك ف entretien: شنو هو DNS؟ شنو غادي تجاوب؟

### Ce qui se passe derrière
*What happens behind the scenes.* Take an action everyone knows and reveal what goes on behind it. Good for concepts that explain a mechanism (network, cloud, browser).

> كتكتب google.com وكتضغط Enter. شنو كيوقع من ورا؟

### Question avec réponse à la fin
*Question answered at the end.* Ask a question and keep the answer for the closing. Use it when the answer is short and satisfying. Less suited to a step-by-step tutorial, where the value is in the demonstration itself. In that case, choose another type.

> علاش الموقع ديالك بطيء؟ الجواب فالأخير.

### Erreur courante
*Common mistake.* Point out a mistake many people make. Good for commands, settings and best practices.

> هاد الغلطة كيديرها بزاف ديال الناس ف Git.

### Ce que personne ne connaît
*What nobody knows.* A little-known command, setting or trick. Good for the command line and tools. Only write it if it is true: check that the trick is not already in the first results of the documentation.

> كاينة commande ف Linux قليل لي كيعرفها.

### Résultat concret
*Concrete result.* Announce what the viewer will know or be able to do at the end, with the duration if it is short.

> ف 30 ثانية غادي تفهم شنو هو cloud.

### Idée reçue
*Misconception.* Contradict a widespread belief. Only use it if the sources confirm the belief is false.

> كيقولو ليك هاد الشي، ولاكن ماشي صحيح.

### Nouveauté
*What's new.* For a new website, tool, game or an update. Mention the name and what it changes.

> خرج site جديد غادي يوفر ليك بزاف د الوقت.

### Mise en situation
*Scenario.* Make the viewer imagine a situation. Good for showing what is at stake with a concept.

> تخيل server ديالك طاح ف نص الليل. شنو غادي تدير؟

## Choosing by topic

These pairings are starting points, not obligations.

| Topic | Types to consider first |
|---|---|
| Concept (cloud, DNS, API...) | Question d'entretien, Ce qui se passe derrière, Mise en situation |
| Command-line command | Ce que personne ne connaît, Erreur courante, Résultat concret |
| New website or tool | Nouveauté, Résultat concret, Erreur courante |
| Gaming | Nouveauté, Idée reçue, Ce que personne ne connaît |

Choose a type, write the hook, then write two alternative hooks of a different type for the "Hooks alternatifs" section of the script.
