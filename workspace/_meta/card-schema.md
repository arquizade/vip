# Card Schema

Every project or client card uses this format.

## Frontmatter (required)

| Field | Type | Description |
| :--- | :--- | :--- |
| `type` | text | `project` or `client` |
| `status` | text | `active`, `paused`, or `done` |
| `next` | text | One sentence. The next concrete action. |
| `updated` | date | `YYYY-MM-DD`, the last time the card changed |

## Home table (required)

| Source | Path |
| :--- | :--- |
| Repo | Absolute or relative path to the code repository |
| Memory | Optional. Path to a memory file your AI tool uses. |
| Vault folder | Path to the project folder in `vault/main/` |
| Resources | Optional. Links to relevant atomic notes. |

## Body

Keep the body empty or under five lines. Long text belongs in the vault.
