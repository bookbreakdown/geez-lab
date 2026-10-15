#!/usr/bin/env python3
"""Check public packaging and research integrity, not linguistic accuracy.

Ge'ez Lab / https://ethiopiancanon.com. MIT.
"""

import ast
import csv
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
errors = []


def require(condition, message):
    if not condition:
        errors.append(message)


def files():
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT)
        if any(part in {".git", "__pycache__", "chunks", ".venv"} for part in rel.parts):
            continue
        if path.is_file() and str(rel) != "chunks-index.csv":
            yield path


def main():
    counts = {"calibrated": 68, "claude": 21, "chatgpt": 25, "chatgpt-high": 1}
    for directory, count in counts.items():
        paths = list((ROOT / "passes" / directory).glob("*.md"))
        require(len(paths) == count, f"Unexpected corpus count: {directory}: {len(paths)}")
        for path in paths:
            text = path.read_text(encoding="utf-8")
            require(text.splitlines()[0] == path.stem, f"Incorrect first-line code: {path}")
            require("## TRANSCRIPTION" in text, f"Missing transcription: {path}")
            require(bool(re.search(r"[\u1200-\u137f]", text)), f"Missing Ethiopic: {path}")
    expected = {f"MAIX1-{n}{s}" for n in range(156, 190) for s in "RV"}
    require({p.stem for p in (ROOT / "passes/calibrated").glob("*.md")} == expected,
            "Main corpus must cover exactly 156r–189v")

    with (ROOT / "folios.csv").open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    require(len(rows) == 249 and len({r['code'] for r in rows}) == 249,
            "Source index must have 249 unique sides")
    boundary = [r for r in rows if r['code'] == 'MAIX1-241R']
    require(len(boundary) == 1 and boundary[0]['catalogue_books'] == 'VI;VII',
            "Shared 241r allocation must be explicit")

    manifest = json.loads((ROOT / "docs/release-manifest.json").read_text(encoding="utf-8"))
    imported = json.loads((ROOT / "docs/import-manifest.json").read_text(encoding="utf-8"))
    for entry in manifest["files"]:
        path = ROOT / entry["path"]
        require(path.is_file(), f"Missing research artifact: {entry['path']}")
        if path.is_file():
            require(hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"],
                    f"Research artifact changed; add a review instead: {entry['path']}")
    # Original readings are exact imports, independently of the release hashes.
    for entry in imported["files"]:
        name = entry["path"]
        if name.startswith(("passes/", "reconciled/", "groundtruth/")) or (name.startswith("ab/") and name.endswith(".txt")):
            path = ROOT / name
            require(path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == entry['sha256_original'],
                    f"Archived reading differs from original import: {name}")

    require("https://ethiopiancanon.com" in (ROOT / "LICENSE").read_text(), "MIT attribution missing")
    require("https://ethiopiancanon.com" in (ROOT / "LICENSE-RESEARCH.md").read_text(), "Research attribution missing")
    for path in files():
        rel = str(path.relative_to(ROOT))
        require(path.suffix.lower() not in {".jpg", ".jpeg", ".png", ".pdf", ".pem", ".key"},
                f"Unexpected binary or credential file: {rel}")
        if path.suffix not in {".py", ".md", ".txt", ".json", ".csv", ".cff", ".yml"} and path.name != "LICENSE":
            continue
        text = path.read_text(encoding="utf-8")
        # Fail on machine-specific private paths or recognisable credential values.
        require(not re.search(r"/(?:var/www|home/[A-Za-z]|mnt/[a-z]/Users)/", text), f"Private machine path: {rel}")
        require(not re.search(r"(?:gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{24,}|-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----)", text),
                f"Possible credential: {rel}")
        if path.suffix == ".py":
            try:
                ast.parse(text, filename=rel)
            except SyntaxError as exc:
                errors.append(str(exc))
        if path.suffix == ".md":
            for target in re.findall(r"\[[^\]\n]*\]\(([^)\s]+)\)", text):
                if re.match(r"[a-zA-Z]+:", target) or target.startswith("#"):
                    continue
                target = unquote(target.split("#")[0])
                require((path.parent / target).exists(), f"Broken local link in {rel}: {target}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Public package checks passed: corpus counts, provenance hashes, source index, Python syntax, local links, attribution, and credential-pattern screening.")
    print("These checks do not verify linguistic accuracy or establish third-party rights.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
