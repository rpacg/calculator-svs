from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent
INDEX_FILE = ROOT / "index.html"


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


def main():
    version_files = sorted(ROOT.glob("Score Calculator SVS v*.html"))
    version = latest_version(version_files)
    if version is None:
        print("Tidak ditemukan file versi yang sesuai.")
        return 1

    changed = update_index(INDEX_FILE, version)
    print(f"Versi terbaru: {version}")
    print("index.html diperbarui." if changed else "index.html sudah menggunakan versi terbaru.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
