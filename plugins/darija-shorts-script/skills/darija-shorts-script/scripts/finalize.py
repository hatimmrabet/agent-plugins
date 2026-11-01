#!/usr/bin/env python3
"""Finalise le script d'un short en darija et contrôle la description.

Sur <script.md> le programme :
  1. place le caractère invisible RLM (U+200F) au début de chaque ligne à lire,
     pour que le lecteur Markdown l'affiche de droite à gauche même quand la
     ligne commence par du français ou de l'anglais ;
  2. compte les mots lus, section par section ;
  3. réécrit les repères de temps des titres et la ligne « Durée : ... ».

Sur <description.md> il ne modifie rien : il contrôle les règles (longueurs,
hashtags, absence de Markdown, première lettre arabe). Pas de RLM ici, parce
que ce texte est copié-collé tel quel sur les plateformes.

Usage :
    python finalize.py script.md [description.md] [--wpm 130] [--dry-run]
"""
import argparse
import re
import sys
import unicodedata

RLM = "‏"
SEPARATOR = "---"
MIN_WORDS = 65   # environ 30 s
MAX_WORDS = 325  # environ 2 min 30
HOOK_MAX_WORDS = 10
TITLE_MAX = 60
HOOK_LINE_MAX = 125
BODY_MAX = 300


def count_words(text):
    text = re.sub(r"[`*‏]", "", text)
    return sum(1 for token in text.split() if any(ch.isalnum() for ch in token))


def is_spoken(line):
    stripped = line.strip()
    return bool(stripped) and not stripped.startswith(("#", ">"))


def first_strong(line):
    for ch in line:
        kind = unicodedata.bidirectional(ch)
        if kind in ("L", "R", "AL"):
            return kind
    return None


def finalize_script(path, wpm, dry_run):
    with open(path, encoding="utf-8", newline="") as f:
        lines = f.read().replace("\r\n", "\n").split("\n")

    separators = [i for i, line in enumerate(lines) if line.strip() == SEPARATOR]
    if not separators:
        sys.exit("Aucune ligne « --- » : le modèle du script n'est pas respecté.")
    start = separators[0] + 1
    end = separators[-1] if len(separators) > 1 else len(lines)

    warnings = []
    sections = []  # [index du titre, nombre de mots, première ligne lue]
    previous_spoken = False
    for i in range(start, end):
        line = lines[i].lstrip(RLM)
        if line.startswith("####"):
            sections.append([i, 0, None])
            lines[i] = line
            previous_spoken = False
        elif is_spoken(line):
            lines[i] = RLM + line
            if sections:
                sections[-1][1] += count_words(line)
                if sections[-1][2] is None:
                    sections[-1][2] = line
            if previous_spoken:
                warnings.append(f"ligne {i + 1} collée à la précédente : mets une ligne vide entre deux lignes")
            previous_spoken = True
        else:
            lines[i] = line
            previous_spoken = False

    total_words = sum(words for _, words, _ in sections)
    total_seconds = round(total_words / wpm * 60)

    cumulated = 0
    rows = []
    for index, words, _ in sections:
        t0 = round(cumulated / wpm * 60)
        cumulated += words
        t1 = round(cumulated / wpm * 60)
        heading = re.sub(r"\s*·\s*\d+\s*-\s*\d+\s*s\s*$", "", lines[index].rstrip())
        lines[index] = f"{heading} · {t0}-{t1} s"
        rows.append((lines[index].lstrip("# "), words))

    for i in range(0, start - 1):
        lines[i] = re.sub(
            r"Durée\s*:\s*~?\d+\s*s\s*·\s*\d+\s*mots",
            f"Durée : ~{total_seconds} s · {total_words} mots",
            lines[i],
        )

    if sections and sections[0][2] and count_words(sections[0][2]) > HOOK_MAX_WORDS:
        warnings.append(f"la première ligne du hook fait {count_words(sections[0][2])} mots (maximum {HOOK_MAX_WORDS})")
    if total_words > MAX_WORDS:
        warnings.append(f"{total_words} mots : au-dessus du maximum de {MAX_WORDS} mots (2 min 30)")
    if total_words < MIN_WORDS:
        warnings.append(f"{total_words} mots : en dessous du minimum de {MIN_WORDS} mots (30 s)")
    for (_, words, _), (title, _) in zip(sections, rows):
        if words == 0:
            warnings.append(f"section vide : {title}")

    if not dry_run:
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(lines))

    print(f"Script : {path}" + ("  (simulation, rien d'écrit)" if dry_run else ""))
    for title, words in rows:
        print(f"  {words:>4} mots   {title}")
    print(f"  Total : {total_words} mots, environ {total_seconds} s à {wpm} mots par minute")
    for warning in warnings:
        print(f"  ATTENTION : {warning}")
    if not warnings:
        print("  Aucun problème détecté.")


def check_description(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    lines = [line.rstrip() for line in text.split("\n") if line.strip()]
    warnings = []
    if len(lines) < 3:
        sys.exit("Description : il faut au moins un titre, une accroche et une ligne de hashtags.")

    title, tag_line, body = lines[0], lines[-1], lines[1:-1]
    tags = [token for token in tag_line.split() if token.startswith("#")]
    hook_line = body[0]
    body_chars = sum(len(line) for line in body)
    raw = text.split("\n")
    for number in range(1, len(raw)):
        if raw[number].strip() and raw[number - 1].strip():
            warnings.append(f"ligne {number + 1} collée à la précédente : mets une ligne vide entre deux lignes")

    if len(title) > TITLE_MAX:
        warnings.append(f"titre de {len(title)} caractères (maximum {TITLE_MAX})")
    if len(hook_line) > HOOK_LINE_MAX:
        warnings.append(f"accroche de {len(hook_line)} caractères (maximum {HOOK_LINE_MAX})")
    if body_chars > BODY_MAX:
        warnings.append(f"description de {body_chars} caractères hors hashtags (environ {BODY_MAX} maximum)")
    if not 3 <= len(tags) <= 5 or len(tags) != len(tag_line.split()):
        warnings.append(f"la dernière ligne doit contenir 3 à 5 hashtags et rien d'autre ({len(tags)} trouvés)")
    if RLM in text:
        warnings.append("caractère invisible RLM présent : il serait copié dans les légendes")
    for number, line in enumerate(lines, 1):
        if re.match(r"^(#{1,6}\s|\*\*|[-*+]\s)", line) or re.match(r"^(titre|description|hashtags?)\s*:", line, re.I):
            warnings.append(f"formatage Markdown ou étiquette sur la ligne « {line[:30]} »")
        if first_strong(line) == "L":
            warnings.append(f"la ligne « {line[:30]} » ne commence pas par un mot arabe")

    print(f"Description : {path}")
    print(f"  Titre {len(title)} car. · accroche {len(hook_line)} car. · texte {body_chars} car. · {len(tags)} hashtags")
    for warning in warnings:
        print(f"  ATTENTION : {warning}")
    if not warnings:
        print("  Aucun problème détecté.")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("script")
    parser.add_argument("description", nargs="?")
    parser.add_argument("--wpm", type=int, default=130, help="mots par minute (130 par défaut)")
    parser.add_argument("--dry-run", action="store_true", help="n'écrit rien dans le script")
    args = parser.parse_args()

    finalize_script(args.script, args.wpm, args.dry_run)
    if args.description:
        check_description(args.description)


if __name__ == "__main__":
    main()
