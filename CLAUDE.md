# agent-plugins

Public plugin marketplace for Claude Code and GitHub Copilot: GitHub repo `hatimmrabet/agent-plugins`, marketplace name `hatimmrabet`. One plugin so far: `darija-shorts-script`. The README is for end users only; maintainer notes live here.

## Layout

```
.claude-plugin/marketplace.json   # catalog: one entry (name, source, description) per plugin
plugins/<plugin>/
├── .claude-plugin/plugin.json    # manifest; the only place a version is set (semver)
├── skills/<skill>/SKILL.md       # `name` must equal the folder name
├── skills/<skill>/references/    # files SKILL.md points to
├── skills/<skill>/scripts/       # helpers the skill runs (Python)
└── CHANGELOG.md
```

Add a plugin = new `plugins/<plugin>/` folder + one entry in `marketplace.json`. The entry `name` must equal the `name` in that plugin's `plugin.json`.

## Commands

Run from the repository root. There is no automated test suite: check changes with these.

```bash
# Load a plugin from the working tree for one session (use /reload-plugins after edits)
claude --plugin-dir ./plugins/<plugin>

# Confirm the plugin loads: look for `<plugin>@inline` with "Status: ✔ loaded" under "Session-only plugins"
claude --plugin-dir ./plugins/<plugin> plugin list

# Validate catalog and manifests: must end with "Validation passed"
claude plugin validate .

# Update your own install after a release, then restart Claude Code
claude plugin marketplace update hatimmrabet && claude plugin update <plugin>@hatimmrabet
```

To test from another project, pass the absolute path of the plugin folder to `--plugin-dir`. For that session the local folder silently replaces an installed plugin with the same name, so you test the working tree, not the published version.

## Rules

- IMPORTANT: edit plugins only in this repository, never the copies in `~/.claude/skills/` or `~/.claude/plugins/` (cache and marketplace clone). A standalone copy in `~/.claude/skills/` loads the skill twice next to the installed plugin.
- IMPORTANT: do not rename the marketplace `name` (`hatimmrabet`) in `marketplace.json`. It is the install key (`<plugin>@hatimmrabet`) and renaming breaks every existing install.
- IMPORTANT: in `darija-shorts-script`, keep the French labels written into the generated script (`Durée`, `mots`, `Hook`, `Idées`, `Contexte`, `Idée`, `Clôture`, `Écran`, `À ne pas lire`, `Hooks alternatifs`, `À vérifier`) and the French hook type names in `references/hooks.md`. `scripts/finalize.py` matches `Durée` and `mots`; changing a label means updating the script and checking its output.
- Write all repository text in English, except what the skills produce and Arabic content.
- Keep skill instructions tool-agnostic: Claude Code and Copilot name their tools differently, so write "web search tool" with the Claude Code name in parentheses.
- `references/plateformes.md` keeps its French file name because `SKILL.md` links to it; update both together if it ever changes.

## Release

1. Bump `version` in `plugins/<plugin>/.claude-plugin/plugin.json` only. Do not set a version in `marketplace.json` (`plugin.json` wins and a mismatch is reported). Installed copies update only when this value changes, so a push without a bump reaches nobody.
2. Add an entry to the plugin's `CHANGELOG.md`.
3. Run `claude plugin validate .`.
4. Commit, then tag and push. The tag must be annotated, because `--follow-tags` skips lightweight tags:

```bash
git tag -a <plugin>-vX.Y.Z -m "<plugin> vX.Y.Z"
git push --follow-tags
```

`metadata.version` in `marketplace.json` is the catalog's own version: leave it alone on plugin releases. Auto-update is off by default for third-party marketplaces; enable it in `/plugin` → Marketplaces → hatimmrabet.

## Gotchas

- Copilot CLI and VS Code read the same `.claude-plugin/` manifests and `skills/` layout. This is documented by GitHub but has not been tested end to end.
- Git on Windows prints `LF will be replaced by CRLF` warnings: harmless.
