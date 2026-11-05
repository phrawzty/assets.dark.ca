#!/usr/bin/env python3
"""Create, restore and verify the original public Noti.st preservation snapshot."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import tarfile
import tempfile
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "preservation-manifest.json"


def sha(path):
    checksum = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            checksum.update(chunk)
    return checksum.hexdigest()


def verify(root, records):
    actual = {str(path.relative_to(root)) for path in root.rglob("*") if path.is_file()}
    if actual != {item["path"] for item in records}:
        raise ValueError("Preservation file inventory differs from the manifest")
    for item in records:
        path = root / item["path"]
        if path.stat().st_size != item["bytes"] or sha(path) != item["sha256"]:
            raise ValueError("Preserved file differs: " + item["path"])
    print(f"Verified all {len(records):,} preserved files.")


def create():
    source = ROOT / "preservation"
    records = [{"path": str(path.relative_to(source)), "bytes": path.stat().st_size, "sha256": sha(path)}
               for path in sorted(source.rglob("*")) if path.is_file()]
    if not records:
        raise ValueError("No preservation files found")
    work = ROOT / "releases"
    work.mkdir(exist_ok=True)
    archive = work / "notist-migration.tar.gz"
    with tarfile.open(archive, "w:gz", compresslevel=1) as output:
        for record in records:
            output.add(source / record["path"], arcname=record["path"], recursive=False)
    checksum = sha(archive)
    destination = work / f"notist-migration-{checksum}.tar.gz"
    archive.replace(destination)
    manifest = {"version": 1, "scope": "public Noti.st portfolio, recovered 2026-11-05",
                "archive": {"name": destination.name, "sha256": checksum, "bytes": destination.stat().st_size,
                            "url": "https://github.com/phrawzty/assets.dark.ca/releases/download/notist-migration-2026-11-05/" + destination.name},
                "files": records}
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
    verify(source, records)
    print(destination)


def restore(manifest):
    destination = ROOT / "preservation"
    if destination.exists():
        raise ValueError("preservation/ already exists; verify it or move it aside before restoring")
    with tempfile.TemporaryDirectory(dir=ROOT, prefix="restore-") as work:
        work = Path(work)
        archive = work / "backup.tar.gz"
        record = manifest["archive"]
        with urlopen(Request(record["url"], headers={"User-Agent": "dark.ca-preservation/1.0"}), timeout=180) as incoming, archive.open("wb") as output:
            shutil.copyfileobj(incoming, output)
        if archive.stat().st_size != record["bytes"] or sha(archive) != record["sha256"]:
            raise ValueError("Backup archive checksum failed")
        extracted = work / "preservation"
        extracted.mkdir()
        expected = {item["path"] for item in manifest["files"]}
        with tarfile.open(archive, "r:gz") as source:
            members = source.getmembers()
            if len(members) != len(expected) or {member.name for member in members} != expected:
                raise ValueError("Archive inventory differs from the manifest")
            for member in members:
                path = Path(member.name)
                if not member.isfile() or path.is_absolute() or ".." in path.parts:
                    raise ValueError("Unsafe archive entry")
                target = extracted / path
                target.parent.mkdir(parents=True, exist_ok=True)
                with source.extractfile(member) as incoming, target.open("wb") as output:
                    shutil.copyfileobj(incoming, output)
        verify(extracted, manifest["files"])
        extracted.rename(destination)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["create", "restore", "verify"])
    args = parser.parse_args()
    if args.action == "create":
        create()
    else:
        manifest = json.loads(MANIFEST.read_text())
        if args.action == "restore":
            restore(manifest)
        else:
            verify(ROOT / "preservation", manifest["files"])
