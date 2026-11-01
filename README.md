# hatimmrabet — Claude plugins

Hatim's Claude Code plugin marketplace.

## Installation

```
/plugin marketplace add hatimmrabet/agent-plugins
/plugin install <plugin-name>@hatimmrabet
```

Update: `/plugin marketplace update hatimmrabet`

## Plugins

| Plugin | Description | Version |
|--------|-------------|---------|
| `darija-shorts-script` | Ready-to-read Darija script for Shorts / Reels / TikTok, with title and description | 1.0.0 |

## Structure

```
agent-plugins/
├── .claude-plugin/marketplace.json   # catalog
└── plugins/
    └── <plugin>/
        ├── .claude-plugin/plugin.json  # manifest + version (semver)
        ├── skills/<skill>/SKILL.md
        └── CHANGELOG.md
```

## Publishing a new version

1. Bump `version` in `plugins/<plugin>/.claude-plugin/plugin.json`
2. Update the plugin's `CHANGELOG.md`
3. `git commit -am "<plugin> vX.Y.Z" && git tag <plugin>-vX.Y.Z && git push --follow-tags`
