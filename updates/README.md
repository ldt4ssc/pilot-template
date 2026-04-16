# Updates

This folder contains your pilot's structured journey documentation: short
public posts about what your pilot is doing, achieving, learning, releasing,
and participating in. Updates published here are read by the LDT4SSC
aggregator and rendered on your pilot's page on the Knowledge Hub and in the
unified feed on the LDT4SSC project website.

## Quick start — add a new update

To create a new update, start from one of the worked examples below that
matches the kind of post you want to publish.

- **[General update](_examples/2026-04-15-example-general.md)** — for
  progress notes, decisions, ongoing work, or reflections.
- **[Milestone](_examples/2026-04-15-example-milestone.md)** — for concrete
  outcomes, achievements, or thresholds reached.
- **[Lesson learned](_examples/2026-04-15-example-lesson.md)** — for
  lessons, positive or negative, that could help other pilots.
- **[Asset release](_examples/2026-04-15-example-asset.md)** — for outputs
  made available for reuse, with a link to where they live.
- **[Event report](_examples/2026-04-15-example-event.md)** — for events
  your pilot hosted, attended, or participated in.

**To create a new update from an example:**

1. Open the linked example file.
2. Click the **Raw** button (top-right of the file view) to see the plain
   source.
3. Select and copy the entire content.
4. Come back to this `updates/` folder and click **Add file → Create new
   file**.
5. Name the file `YYYY-MM-DD-short-title.md`, using today's date and a
   short descriptive slug (e.g. `2026-05-20-air-quality-sensors-deployed.md`).
6. Paste the content, then edit it: **update every field in the front matter**,
   rewrite the body, and remove any sections that do not apply.
7. Commit.

Alternatively, in your local clone, copy the example file into this
folder with a new date-based filename and edit it there.

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

## What happens after you post

Once an update is committed and passes validation, the next scheduled build
of the LDT4SSC aggregator (running at least daily) will publish it on:

- Your pilot's page on the **LDT4SSC Knowledge Hub**.
- The unified feed on the **LDT4SSC project website**.
- The project-wide and per-pilot **RSS/Atom feeds**.

You do not need to do anything beyond committing the update.

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

See the Pilot Update Guide annex of the LDT4SSC onboarding package for
detailed guidance. If the error message is not clear, contact the LDT4SSC
Help Desk.

## The `_examples/` and `_schema/` folders

These two folders inside `updates/` are reserved for internal use:

- `_examples/` contains the worked examples referenced in the Quick
  Start section above. Copy from them when writing your own updates, but
  do not add real updates here — the aggregator ignores any file inside
  a folder starting with an underscore.
- `_schema/` contains the formal schema definitions used by the
  validation workflow. Do not modify anything in this folder unless you
  are maintaining the template itself.

Real updates go directly inside `updates/`, not inside either of the
underscore-prefixed folders.