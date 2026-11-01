---
name: darija-shorts-script
description: Prepares a ready-to-read script in Moroccan Darija for a short vertical video (YouTube Shorts, Instagram Reels, Facebook Reels, TikTok), plus a copy-paste title and description. Researches the topic in official documentation and recognized blogs, picks a hook suited to the subject, writes a 30 s to 2 min 30 script and fact-checks it. Use whenever the user says "write me a script about [topic]", "prepare a short / a reel / a TikTok about...", "write me a script in darija", "give me a hook", "title and description for my video", or gives a topic (gaming, new website, command-line command, cloud, tech concept) and asks for a short video, even without saying the word "skill". Also triggers on French requests such as « fais-moi un script pour [sujet] », « prépare un short / un reel / un TikTok sur... », « écris-moi un script en darija », « donne-moi un hook », « titre et description pour ma vidéo ».
---

# Darija short script

From a topic, produce two files the user uses as-is:

- `<slug>-script.md`: the script to read to the camera, with the sources at the bottom.
- `<slug>-description.md`: a title and a description with no formatting at all, to copy-paste onto the platforms.

The user records by reading the script. Everything they need must be in these two files: they should not have to look anything up elsewhere. A script must first of all be easy to read at a glance while filming.

## Decisions already made (do not ask again)

- **Platforms**: YouTube Shorts, Instagram Reels, Facebook Reels and TikTok. A single version, valid everywhere.
- **Script language**: pure Moroccan Darija, written in Arabic script, to be read the way people speak. Words that are not Arabic (technical terms, product names, commands) stay in their original language, English or French, without transliteration. Details in `references/darija.md`.
- **Title and description**: Darija + original-language keywords, hashtags in Latin letters except the first (see the direction rule).
- **Addressing the viewer**: singular (كتعرف، شوف).
- **Length**: from 30 s to 2 min 30, never more. Beyond that, it is tiresome to read and to follow.
- **Topics**: varied and changing (gaming, new websites, command-line commands, cloud, tech concepts). Assume nothing about the topic from the previous video.
- **Sources**: all at the bottom of the script, outside the reading area, to keep a record. They stay in their original language, untranslated.
- **Script headings**: in French or English, either one, with no translation into Arabic.

If the user asks for something else for a specific video, their request of the moment takes precedence.

## Direction rule: the alignment of each line

A Markdown reader picks the direction of a line from its first "strong" character. A line that starts with French or English is displayed left to right and badly aligned: the user can no longer read it while filming.

- **Script**: write naturally, without contortions to make every sentence start with an Arabic word. Once the file is written, run `scripts/finalize.py`: it places the invisible RLM character (U+200F) at the start of each line to be read, which forces right-to-left display. If Python is not available, insert that character by hand in front of each line to be read.
- **Description**: this is copy-pasted text, so no invisible characters (they would be pasted into the captions and could stop a platform from recognizing a hashtag). The file is `.md`: each line aligns according to its first strong character, so start each line with an Arabic word (rewrite the sentence, or put a small Arabic word in front: ال، و، ف، ل، هاد) and put an Arabic hashtag first (#تقنية، #معلوميات، #ألعاب).
- **Headings, labels and sources**: they may stay in French, English or their original language. They are not lines to be read.

Backticks, `**`, `>`, `-`, `#` and digits are neutral: they do not decide the direction.

## Do not guess: ask

The user does not want predictions. When information is missing or a choice belongs to them, ask the question with concrete options: use the multiple-choice question tool (AskUserQuestion) if it is available, otherwise a numbered list. 2 to 4 options, your recommendation first, one sentence per option. Group all the questions of a given moment into a single message.

Ask when:

- the topic is broad: suggest 2 to 4 possible angles;
- the length is not given: suggest options within the 30 s – 2 min 30 range, and recommend the one that fits the complexity of the topic;
- the sources cannot be found, are too old or contradict each other: lay out the disagreement and ask what to keep;
- a Darija word or spelling is truly uncertain.

Do not ask what you can decide yourself: the hook, the structure, the tone, the title. Choose, and say in one line why.

Never invent a technical fact (command, option, price, date, feature name, version). If the sources do not confirm it, do not write it in the text that is read.

## Workflow

### 1. Scoping

Pick out the topic and, if given, the length from the message. Ask only the questions that are missing (angle, length), in a single message. If everything is clear, go straight to research.

### 2. Research

Search the official documentation first, then recognized blogs and resources to fill in (concrete examples, common mistakes, context). Use WebSearch and WebFetch. If you have no web access, ask the user to provide the sources.

Where to search depending on the topic:

| Topic type | Sources to favor |
|---|---|
| Tech concept, cloud | Provider documentation (AWS, Google Cloud, Azure, Cloudflare...), MDN, RFCs |
| Command-line command | man page, `--help`, the tool's official documentation, official GitHub repository |
| New website or tool | Official site, documentation, changelog, pricing page |
| Gaming | Publisher's site, patch notes, Steam or platform page |

What you must come away with: the central idea in one sentence, the essential points (see below for how many), a concrete example or an analogy, and the pitfall or common mistake if there is one. Discard the rest: the length decides what stays.

- Always rephrase in your own words, never copy a sentence from a source.
- Check the date and the version: a command, a price or a feature may have changed.
- Note the title and the URL of each source actually consulted, for the end of the script.

### 3. Hook

There is always a hook. Read `references/hooks.md`, choose the type that fits the topic and write it in Darija. Also prepare 2 alternative hooks of different types for the bottom of the script.

### 4. Writing

Word budget, at about 130 words per minute counting pauses (an estimate to adjust, see below):

| Length | Words (approx.) | Points to cover |
|---|---|---|
| 30 s | 65 | 1 |
| 45 s | 100 | 1 to 2 |
| 1 min | 130 | 2 |
| 1 min 30 | 195 | 2 to 3 |
| 2 min | 260 | 3 to 4 |
| 2 min 30 (maximum) | 325 | 3 to 5 |

Structure:

1. **Hook**: first line of 10 words maximum, no introductory phrase before it.
2. **Context**: why it matters, in 1 to 2 sentences.
3. **Ideas**: one per point, each with a short heading visible in the script to find your place while filming.
4. **Closing**: sum up the idea in one sentence, then a single simple call to action (follow, save, comment). If the hook was a question, the answer is given here, clearly.

Write following `references/darija.md`. Read it before writing: the script must sound like someone talking, not like a text.

The rate of 130 words per minute comes from English-language sources. If the user gives their actual pace (for example "100 words is 48 s"), pass it to the script with `--wpm` and tell them they can keep it as a reference.

### 5. Finalization

Write the two files, then run the script bundled with the skill. `scripts/` is in the folder of this skill (the one containing this SKILL.md), not in the working folder: use its full path. Depending on the system, the command is `python` or `python3`.

```
python <skill folder>/scripts/finalize.py <slug>-script.md <slug>-description.md
```

It does three things in the script: add the direction marks, compute the time marks of each heading and the « Durée » line, count the words per section. It also checks the description. Fix everything it flags (WARNING), then run it again until there is no problem left.

### 6. Verification

Reread the script with this list before delivering:

1. **Facts**: every technical claim comes from a source you consulted. Exact commands, options, figures, dates and names. What you could not confirm goes under « À vérifier » at the bottom, never in the text that is read. For a command, tell apart a command-line option (with its exact dashes: `-x`, `--exclude`) from a key in an interface (no dash: `d`, `q`): check in the documentation which one it is, and write « ضغط على » in front of a key so that it is clear when spoken.
2. **Length**: between 65 and 325 words (the finalization script checks it).
3. **Hook**: 10 words maximum, you understand what the video is about, and the content keeps the promise.
4. **Darija**: no Standard Arabic phrasing, Arabic punctuation, technical words in their original language, singular address.
5. **Readability**: one idea per line, one blank line between two lines, main title and summary of the ideas at the top, section headings in H4.
6. **Description**: the rules of the next section are followed.

### 7. Title and description

A `.md` file so that each line displays right to left, but **with no Markdown formatting at all** (no `#` headings, no `**`, no bullets, no labels like "Titre :"), because the user copies and pastes directly. Separate each line from the next with a blank line: without it, Markdown merges them into a single paragraph and the copy-paste loses the line breaks. Exact structure:

```
<Title>

<Teaser line>

<One or two lines of context, each separated by a blank line>

#<Arabic word> #<keyword> #<keyword>
```

Rules:

- **Title**: 60 characters maximum, starts with an Arabic word with the main keyword in the first few words, faithful to the content, no ALL CAPS, no emoji. YouTube allows 100 characters, but a short title stays readable on mobile.
- **Teaser line**: 125 characters maximum. This is what stays visible before "more" on several platforms. It must make people want to watch, not repeat the title.
- **Context**: one or two short lines. In total, about 300 characters excluding hashtags, which works on all four platforms.
- **Hashtags**: 3 to 5, no space inside a hashtag, related to the topic. The first is in Arabic (direction rule), the following ones in Latin letters. No misleading hashtag. No `#Shorts` by default: YouTube classifies a video as a Short according to its format (vertical or square, 3 minutes maximum), not according to a hashtag.
- **Keywords**: 1 or 2 main keywords present in both the title and the teaser line.
- **Direction**: each line starts with an Arabic word, and no invisible character.

The first line is used as the YouTube title. Everything that follows is used as the description on YouTube and as the caption on Instagram, Facebook and TikTok. Tell the user this in your reply.

The platforms' limits and tips are in `references/plateformes.md`, with their reliability level. Do not quote them as certainties if they are marked "Unconfirmed".

### 8. Delivery

The two files are in the current working folder, or in the one the user indicates. The slug is in lowercase Latin letters, without accents, with hyphens.

Then reply in a few lines: estimated length and word count, the type of hook chosen and why, links to the two files, and what is left to verify if anything. Do not copy the script into the reply: the user reads it in the file.

## Script template

Follow this structure. It is made to be read while filming: a big title and a summary to skim the script, then short lines, one idea per line. The words between angle brackets are to be replaced.

The labels (`Durée`, `mots`, `Hook`, `Idées`, `Contexte`, `Idée`, `Clôture`, `Écran`, `À ne pas lire`, `Sources`, `Hooks alternatifs`, `À vérifier`) are written in French in the generated file, on purpose: `scripts/finalize.py` relies on `Durée` and `mots`, and the generated scripts keep the same look. Copy them exactly. In English: Durée = Duration, mots = words, Idées = Ideas, Contexte = Context, Clôture = Closing, Écran = Screen, À ne pas lire = Do not read, Hooks alternatifs = Alternative hooks, À vérifier = To verify.

```markdown
# <Topic in a few words>

Durée : ~<n> s · <n> mots · Hook : <type>

Idées : <idea 1> · <idea 2> · <idea 3>

---

#### Hook · 0-6 s

**<first line, 10 words maximum>**

<line>

#### Contexte · 6-16 s

<line>

<line>

#### Idée 1 · <short title> · 16-28 s

<line>

<line>

> Écran : <what is displayed, for example the command>

#### Idée 2 · <short title> · 28-41 s

<line>

<line>

#### Clôture · 41-46 s

<summary line>

<call to action>

---

#### À ne pas lire

**Sources**
- <page title> : <URL>

**Hooks alternatifs**
- <type> : <line>
- <type> : <line>

**À vérifier**
- <unconfirmed fact, only if there is one>
```

Layout rules:

- **Top of the file**: a single H1 title (the topic), then the length and the hook type, then the « Idées » line that sums up the content in 3 to 5 cues of a few words each. This lets you skim the script without reading all of it.
- **Separator**: a `---` line between this summary and the text to be read, and another before the « À ne pas lire » part.
- **Section headings**: in H4 (`####`), never H1, H2 or H3 (except the title at the top). They are discreet landmarks.
- **One idea = one line.** One sentence per line, 6 to 12 words, never a paragraph. Put a blank line between two lines: without it, Markdown merges them into a single dense block of text.
- Put in **bold** the 1 or 2 words to stress in the line, no more.
- The time marks of the headings and the « Durée » line are recomputed by `scripts/finalize.py`: write approximate values, the script corrects them.
- The `> Écran :` lines are optional and are not read. Add them only when a visual helps (a command, a menu name), with little text: Instagram reduces the visibility of videos mostly made of text.
- Commands and code go between backticks.
- Everything that is not to be read is under « À ne pas lire » or on a `>` line.
