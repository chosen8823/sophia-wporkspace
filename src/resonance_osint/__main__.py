from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


TEXT_SUFFIXES = {
    ".md", ".txt", ".py", ".js", ".ts", ".tsx", ".jsx", ".json",
    ".yaml", ".yml", ".toml", ".html", ".css", ".sql", ".sh"
}


@dataclass(frozen=True)
class ArtifactAtom:
    path: str
    sha256: str
    bytes: int
    kind: str
    perspective: str = "OBSERVED"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def walk(root: Path) -> Iterable[ArtifactAtom]:
    ignored = {".git", ".venv", "node_modules", "dist", "build", "resonance"}
    for path in sorted(root.rglob("*")):
        if not path.is_file() or any(part in ignored for part in path.parts):
            continue
        data = path.read_bytes()
        yield ArtifactAtom(
            path=str(path.relative_to(root)),
            sha256=digest(data),
            bytes=len(data),
            kind="text" if path.suffix.lower() in TEXT_SUFFIXES else "binary",
        )


def perspectives(atom: ArtifactAtom) -> list[dict]:
    """Generate deterministic lenses first; model lenses can be adapters later."""
    return [
        {"lens": "provenance", "artifact": atom.path, "claim": "artifact observed", "basis": atom.sha256},
        {"lens": "structure", "artifact": atom.path, "claim": f"kind={atom.kind}; bytes={atom.bytes}", "basis": atom.sha256},
        {"lens": "resonance", "artifact": atom.path, "claim": "candidate for semantic embedding", "basis": atom.sha256},
    ]


def crawl(root: Path, out: Path) -> None:
    atoms = list(walk(root))
    out.mkdir(parents=True, exist_ok=True)

    with (out / "artifacts.jsonl").open("w", encoding="utf-8") as f:
        for atom in atoms:
            f.write(json.dumps(asdict(atom), sort_keys=True) + "\n")

    with (out / "perspectives.jsonl").open("w", encoding="utf-8") as f:
        for atom in atoms:
            for view in perspectives(atom):
                f.write(json.dumps(view, sort_keys=True) + "\n")

    manifest = {
        "schema": "resonance-osint/run/v0",
        "root": str(root.resolve()),
        "artifact_count": len(atoms),
        "invariant": "observation != attribution; similarity != identity",
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps(manifest, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["crawl"])
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--out", default="resonance/latest")
    args = parser.parse_args()

    if args.command == "crawl":
        crawl(Path(args.root), Path(args.out))


if __name__ == "__main__":
    main()
