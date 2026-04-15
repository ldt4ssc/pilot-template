# Updates

This folder contains your pilot's structured journey documentation: short
public posts about what your pilot is doing, achieving, learning, releasing,
and participating in. Updates published here are read by the LDT4SSC
aggregator and rendered on your pilot's page on the Knowledge Hub and in the
unified feed on the LDT4SSC project website.

## How to add an update

1. **Pick the right record type** for what you are posting (see below).
2. **Copy one of the worked examples** from [`_examples/`](_examples/) into
   this folder, renaming the file to follow the pattern
   `YYYY-MM-DD-short-title.md`.
3. **Edit the front matter** at the top of the file (between the `---`
   markers) to describe your update.
4. **Write the body** in Markdown.
5. **Commit and push.** The validation workflow will check that your update
   conforms to the schema and report any problems.

Detailed guidance — including how to write Markdown, how to insert images
and links, how often to post, and what not to post — is provided in the
**Pilot Update Guide** annex of the LDT4SSC pilot onboarding package.

## The five record types

| Type | When to use |
|---|---|
| `general` | General progress notes, ongoing work, decisions, reflections. |
| `milestone` | A concrete outcome, achievement, or threshold reached. |
| `lesson` | Something you learned, positive or negative, that could help other pilots. |
| `asset` | An output made available for reuse, with a link to where it lives. |
| `event` | An event your pilot hosted, attended, or participated in. |

## File naming

Update files must be named `YYYY-MM-DD-short-title.md`, where:

- `YYYY-MM-DD` is the date of the update in ISO 8601 format.
- `short-title` is a short descriptive slug, lowercase, with hyphens
  instead of spaces, ideally fewer than 60 characters.

Examples:

- `2026-03-14-first-data-integration.md`
- `2026-04-02-lessons-from-stakeholder-workshop.md`
- `2026-05-20-air-quality-sensors-deployed.md`

## The schema

All updates must conform to the schema defined in
[`_schema/update-v1.schema.json`](_schema/update-v1.schema.json). The
validation workflow runs this check automatically on every push.

The schema is **versioned**. The current version is `v1`, and every update
must declare `schema_version: 1` in its front matter. If a future version of
the schema is published, older updates will continue to validate against the
version they declare; you do not need to migrate existing posts.

## Worked examples

The [`_examples/`](_examples/) folder contains worked examples of three
record types: `milestone`, `lesson`, and `update`. Use them as starting
points when writing your own. The `asset` and `event` record types follow
the same structure; if you need a worked example for either, ask the
LDT4SSC Help Desk and we will publish one.

The examples are ignored by the aggregator (they are filtered by the `_`
prefix in the folder name), so they are visible to you as references but
do not appear as real updates on the Knowledge Hub or project website.

## What if the validation fails?

If you commit an update and the validation workflow reports an error, the
GitHub Actions interface will show you which file has the problem and what
is wrong with it. Common issues:

- **Wrong field name** (e.g., `tag` instead of `tags`) — fix the spelling.
- **Wrong field value** (e.g., `type: news` instead of one of the five
  allowed types) — change to a valid value.
- **Missing required field** — add it.
- **Wrong date format** — use `YYYY-MM-DD`, not `15/03/2026`.
- **Tabs in the YAML front matter** — replace with spaces.

If the error message is not clear, contact the LDT4SSC Help Desk.

## Where these updates appear

Once an update is committed and passes validation, the next scheduled build
of the LDT4SSC aggregator (running at least daily) will publish it on:

- Your pilot's page on the **LDT4SSC Knowledge Hub**.
- The unified feed on the **LDT4SSC project website**.
- The project-wide and per-pilot **RSS/Atom feeds**.

You do not need to do anything beyond committing the update.