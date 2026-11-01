# hatimmrabet — plugins Claude

Marketplace de plugins Claude Code de Hatim.

## Installation

```
/plugin marketplace add hatimmrabet/agent-plugins
/plugin install <nom-du-plugin>@hatimmrabet
```

Mise à jour : `/plugin marketplace update hatimmrabet`

## Plugins

| Plugin | Description | Version |
|--------|-------------|---------|
| `darija-shorts-script` | Script prêt à lire en darija pour Shorts / Reels / TikTok, avec titre et description | 1.0.0 |

## Structure

```
hatimmrabet/
├── .claude-plugin/marketplace.json   # catalogue
└── plugins/
    └── <plugin>/
        ├── .claude-plugin/plugin.json  # manifeste + version (semver)
        ├── skills/<skill>/SKILL.md
        └── CHANGELOG.md
```

## Publier une nouvelle version

1. Bumper `version` dans `plugins/<plugin>/.claude-plugin/plugin.json`
2. Mettre à jour le `CHANGELOG.md` du plugin
3. `git commit -am "<plugin> vX.Y.Z" && git tag <plugin>-vX.Y.Z && git push --follow-tags`
