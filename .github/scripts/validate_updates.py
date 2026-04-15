#!/usr/bin/env python3
"""
LDT4SSC pilot update validator.

Walks the updates/ folder, parses each update file's YAML front matter,
routes it to the correct schema based on its declared schema_version,
and validates it. Reports all errors found and exits non-zero if any
update is invalid.

This script is run by the validate-updates GitHub Actions workflow.
"""

import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator
from jsonschema.exceptions import ValidationError

REPO_ROOT = Path(__file__).resolve().parents[2]
UPDATES_DIR = REPO_ROOT / "updates"
SCHEMA_DIR = UPDATES_DIR / "_schema"
EXAMPLES_DIR = UPDATES_DIR / "_examples"

FRONT_MATTER_PATTERN = re.compile(
    r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.DOTALL
)

FILENAME_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}-[a-z0-9-]+\.md$")


def find_update_files():
    """Find all update markdown files, excluding examples and schema folder."""
    if not UPDATES_DIR.is_dir():
        return []
    files = []
    for path in sorted(UPDATES_DIR.rglob("*.md")):
        # Skip files inside _examples/, _schema/, or any folder starting with _
        if any(part.startswith("_") for part in path.relative_to(UPDATES_DIR).parts):
            continue
        # Skip the updates/README.md itself
        if path.name == "README.md":
            continue
        files.append(path)
    return files


def parse_front_matter(file_path):
    """Extract and parse the YAML front matter from an update file."""
    text = file_path.read_text(encoding="utf-8")
    match = FRONT_MATTER_PATTERN.match(text)
    if not match:
        raise ValueError(
            "File does not start with a valid YAML front matter block "
            "(expected '---' on the first line, then YAML, then '---' "
            "on a line by itself)."
        )
    front_matter_text = match.group(1)
    try:
        front_matter = yaml.safe_load(front_matter_text)
    except yaml.YAMLError as e:
        raise ValueError(f"YAML parse error in front matter: {e}")
    if not isinstance(front_matter, dict):
        raise ValueError(
            "Front matter must be a YAML mapping (key-value pairs)."
        )
    return front_matter


def load_schema(schema_version):
    """Load the schema file matching the declared schema version."""
    schema_path = SCHEMA_DIR / f"update-v{schema_version}.schema.json"
    if not schema_path.is_file():
        raise FileNotFoundError(
            f"No schema file found for schema_version={schema_version} "
            f"(expected at {schema_path.relative_to(REPO_ROOT)})."
        )
    with schema_path.open(encoding="utf-8") as f:
        return json.load(f)


def validate_filename(file_path):
    """Check that the filename follows the YYYY-MM-DD-short-title.md pattern."""
    if not FILENAME_PATTERN.match(file_path.name):
        raise ValueError(
            f"Filename does not match the required pattern "
            f"'YYYY-MM-DD-short-title.md' (lowercase, hyphens, no spaces)."
        )


def validate_file(file_path):
    """Validate a single update file. Returns a list of error messages."""
    errors = []
    rel_path = file_path.relative_to(REPO_ROOT)

    # Filename check
    try:
        validate_filename(file_path)
    except ValueError as e:
        errors.append(f"  Filename: {e}")

    # Front matter parse
    try:
        front_matter = parse_front_matter(file_path)
    except ValueError as e:
        errors.append(f"  {e}")
        return errors  # Cannot proceed without parsed front matter

    # Schema version routing
    schema_version = front_matter.get("schema_version")
    if schema_version is None:
        errors.append("  Missing required field: schema_version")
        return errors

    try:
        schema = load_schema(schema_version)
    except FileNotFoundError as e:
        errors.append(f"  {e}")
        return errors

    # Schema validation
    validator = Draft202012Validator(schema)
    schema_errors = sorted(validator.iter_errors(front_matter), key=lambda e: e.path)
    for err in schema_errors:
        path = ".".join(str(p) for p in err.absolute_path) or "(root)"
        errors.append(f"  Schema error at '{path}': {err.message}")

    return errors


def main():
    files = find_update_files()
    if not files:
        print("No update files to validate.")
        return 0

    print(f"Validating {len(files)} update file(s)...\n")

    total_errors = 0
    for file_path in files:
        rel_path = file_path.relative_to(REPO_ROOT)
        errors = validate_file(file_path)
        if errors:
            print(f"FAIL: {rel_path}")
            for err in errors:
                print(err)
            print()
            total_errors += len(errors)
        else:
            print(f"OK:   {rel_path}")

    print()
    if total_errors:
        print(f"Validation failed with {total_errors} error(s).")
        return 1
    else:
        print("All updates valid.")
        return 0


if __name__ == "__main__":
    sys.exit(main())