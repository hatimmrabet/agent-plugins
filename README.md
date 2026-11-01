# agent-plugins

Hatim's plugin marketplace for AI coding agents (Claude Code, GitHub Copilot).

## Installation

### Claude Code

```
/plugin marketplace add hatimmrabet/agent-plugins
/plugin install <plugin-name>@hatimmrabet
```

Update: `/plugin marketplace update hatimmrabet`

### GitHub Copilot

The plugins use the standard `skills/<name>/SKILL.md` layout, and Copilot CLI reads the `.claude-plugin/` manifests, so the same repository works as a Copilot marketplace.

**Copilot CLI**

```
copilot plugin marketplace add hatimmrabet/agent-plugins
copilot plugin install <plugin-name>@hatimmrabet
```

Update a plugin: `copilot plugin update <plugin-name>`

**VS Code**

Add `hatimmrabet/agent-plugins` to the `chat.plugins.marketplaces` setting, then install the plugin from the Agent Customizations editor (`Chat: Open Customizations` → Browse).

**Without a plugin**

Copy a skill folder (for example `plugins/darija-shorts-script/skills/darija-shorts-script`) into `.github/skills/` (project) or `~/.copilot/skills/` (personal).

> The plugins are tested with Claude Code. The Copilot instructions follow GitHub's and VS Code's documentation and have not been tested end to end.

## Plugins

| Plugin | Description | Version |
|--------|-------------|---------|
| `darija-shorts-script` | Ready-to-read Darija script for Shorts / Reels / TikTok, with title and description | 1.0.1 |

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

1. Bump `version` in `plugins/<plugin>/.claude-plugin/plugin.json` and in `.claude-plugin/marketplace.json`
2. Update the plugin's `CHANGELOG.md`
3. `git commit -am "<plugin> vX.Y.Z" && git tag <plugin>-vX.Y.Z && git push --follow-tags`
