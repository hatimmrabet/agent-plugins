#!/usr/bin/env python3
"""Finalizes a Darija short script and checks the description.

On <script.md> the program:
  1. places the invisible RLM character (U+200F) at the start of each line to
     be read, so that the Markdown reader displays it right to left even when
     the line starts with French or English;
  2. counts the words read, section by section;
  3. rewrites the time marks of the headings and the « Durée : ... » line.

On <description.md> it modifies nothing: it checks the rules (lengths,
hashtags, no Markdown, first letter Arabic). No RLM here, because this text is
copy-pasted as-is onto the platforms.

Usage:
    python finalize.py script.md [description.md] [--wpm 130] [--dry-run]
"""
import argparse
import re
import sys
import unicodedata

RLM = "‏"
SEPARATOR = "---"
MIN_WORDS = 65   # about 30 s
MAX_WORDS = 325  # about 2 min 30
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
        sys.exit('No "---" line: the script template was not followed.')
    start = separators[0] + 1
    end = separators[-1] if len(separators) > 1 else len(lines)

    warnings = []
    sections = []  # [heading index, word count, first line read]
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
                warnings.append(f"line {i + 1} stuck to the previous one: put a blank line between two lines")
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

    # "Durée" and "mots" are the labels written in the generated script: keep them in French.
    for i in range(0, start - 1):
        lines[i] = re.sub(
            r"Durée\s*:\s*~?\d+\s*s\s*·\s*\d+\s*mots",
            f"Durée : ~{total_seconds} s · {total_words} mots",
            lines[i],
        )

    if sections and sections[0][2] and count_words(sections[0][2]) > HOOK_MAX_WORDS:
        warnings.append(f"the first line of the hook is {count_words(sections[0][2])} words (maximum {HOOK_MAX_WORDS})")
    if total_words > MAX_WORDS:
        warnings.append(f"{total_words} words: above the maximum of {MAX_WORDS} words (2 min 30)")
    if total_words < MIN_WORDS:
        warnings.append(f"{total_words} words: below the minimum of {MIN_WORDS} words (30 s)")
    for (_, words, _), (title, _) in zip(sections, rows):
        if words == 0:
            warnings.append(f"empty section: {title}")

    if not dry_run:
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(lines))

    print(f"Script: {path}" + ("  (dry run, nothing written)" if dry_run else ""))
    for title, words in rows:
        print(f"  {words:>4} words   {title}")
    print(f"  Total: {total_words} words, about {total_seconds} s at {wpm} words per minute")
    for warning in warnings:
        print(f"  WARNING: {warning}")
    if not warnings:
        print("  No problem detected.")


def check_description(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    lines = [line.rstrip() for line in text.split("\n") if line.strip()]
    warnings = []
    if len(lines) < 3:
        sys.exit("Description: at least a title, a teaser and a hashtag line are required.")

    title, tag_line, body = lines[0], lines[-1], lines[1:-1]
    tags = [token for token in tag_line.split() if token.startswith("#")]
    hook_line = body[0]
    body_chars = sum(len(line) for line in body)
    raw = text.split("\n")
    for number in range(1, len(raw)):
        if raw[number].strip() and raw[number - 1].strip():
            warnings.append(f"line {number + 1} stuck to the previous one: put a blank line between two lines")

    if len(title) > TITLE_MAX:
        warnings.append(f"title of {len(title)} characters (maximum {TITLE_MAX})")
    if len(hook_line) > HOOK_LINE_MAX:
        warnings.append(f"teaser of {len(hook_line)} characters (maximum {HOOK_LINE_MAX})")
    if body_chars > BODY_MAX:
        warnings.append(f"description of {body_chars} characters excluding hashtags (about {BODY_MAX} maximum)")
    if not 3 <= len(tags) <= 5 or len(tags) != len(tag_line.split()):
        warnings.append(f"the last line must contain 3 to 5 hashtags and nothing else ({len(tags)} found)")
    if RLM in text:
        warnings.append("invisible RLM character present: it would be copied into the captions")
    for number, line in enumerate(lines, 1):
        if re.match(r"^(#{1,6}\s|\*\*|[-*+]\s)", line) or re.match(r"^(titre|description|hashtags?)\s*:", line, re.I):
            warnings.append(f"Markdown formatting or label on the line « {line[:30]} »")
        if first_strong(line) == "L":
            warnings.append(f"the line « {line[:30]} » does not start with an Arabic word")

    print(f"Description: {path}")
    print(f"  Title {len(title)} chars · teaser {len(hook_line)} chars · text {body_chars} chars · {len(tags)} hashtags")
    for warning in warnings:
        print(f"  WARNING: {warning}")
    if not warnings:
        print("  No problem detected.")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("script")
    parser.add_argument("description", nargs="?")
    parser.add_argument("--wpm", type=int, default=130, help="words per minute (130 by default)")
    parser.add_argument("--dry-run", action="store_true", help="do not write anything to the script")
    args = parser.parse_args()

    finalize_script(args.script, args.wpm, args.dry_run)
    if args.description:
        check_description(args.description)


if __name__ == "__main__":
    main()
