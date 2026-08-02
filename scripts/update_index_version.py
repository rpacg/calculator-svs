from pathlib import Path
from datetime import date
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
INDEX_FILE = ROOT / "index.html"
ARCHIVE_DIR = ROOT / "archives" / "html-versions"
CHANGELOG_FILE = ROOT / "CHANGELOG.md"


def sync_index_to_latest_version(root: Path, index_path: Path):
    version_files = sorted(list((root / "archives" / "html-versions").glob("Score Calculator SVS v*.html")))
    version = latest_version(version_files)
    if version is None:
        return False, None

    changed = update_index(index_path, version)
    return changed, version


def parse_version(value: str):
    match = re.search(r"(\d+(?:\.\d+)+)", value)
    if not match:
        return None
    parts = tuple(int(part) for part in match.group(1).split("."))
    return parts


def latest_version(files):
    versions = []
    for file in files:
        version = parse_version(file.name)
        if version is not None:
            versions.append((version, file.name))
    if not versions:
        return None

    latest = max(versions, key=lambda item: item[0])[1]
    match = re.search(r"(v\d+(?:\.\d+)+)", latest, re.IGNORECASE)
    return match.group(1).lower() if match else None


def update_index(index_path: Path, version: str):
    text = index_path.read_text(encoding="utf-8")
    original = text

    text = re.sub(
        r"(<title>.*?\b)(v\d+(?:\.\d+)+)(</title>)",
        rf"\g<1>{version}\g<3>",
        text,
        count=1,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"(<footer>.*?\b)(V\d+(?:\.\d+)+)(</footer>)",
        rf"\g<1>V{version[1:]}\g<3>",
        text,
        count=1,
        flags=re.IGNORECASE,
    )

    if text != original:
        index_path.write_text(text, encoding="utf-8")
        return True
    return False


def ensure_changelog_exists():
    if not CHANGELOG_FILE.exists():
        CHANGELOG_FILE.write_text(
            "# Changelog\n\nAll notable changes to this project will be documented in this file.\n\n",
            encoding="utf-8",
        )


def changelog_contains_version(version: str):
    text = CHANGELOG_FILE.read_text(encoding="utf-8")
    return re.search(rf"^## \[{re.escape(version)}\]", text, flags=re.MULTILINE) is not None


def append_changelog_entry(version: str):
    ensure_changelog_exists()
    if changelog_contains_version(version):
        return False

    today = date.today().isoformat()
    section = (
        f"## [{version}] - {today}\n"
        "### Added\n"
        "- Describe changes for this version.\n\n"
        "### Changed\n"
        "- \n\n"
        "### Fixed\n"
        "- \n\n"
    )
    text = CHANGELOG_FILE.read_text(encoding="utf-8")
    CHANGELOG_FILE.write_text(text + section, encoding="utf-8")
    return True


def main():
    changed, version = sync_index_to_latest_version(ROOT, INDEX_FILE)
    if version is None:
        print("Tidak ditemukan file versi yang sesuai.")
        return 1

    version_number = version[1:] if version.startswith('v') else version
    changelog_changed = append_changelog_entry(version_number)

    print(f"Versi terbaru: {version}")
    print("index.html diperbarui." if changed else "index.html sudah menggunakan versi terbaru.")
    if changelog_changed:
        print(f"CHANGELOG.md diperbarui dengan entri versi {version_number}.")
    else:
        print(f"CHANGELOG.md sudah berisi entri versi {version_number}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
