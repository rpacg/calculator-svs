import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VERSION_PATTERN = re.compile(r"^Score Calculator SVS v\d+(?:\.\d+)+\.html$")


def discover_versions(root: Path):
    items = {}
    for path in root.glob("Score Calculator SVS v*.html"):
        if VERSION_PATTERN.match(path.name):
            items[path.name] = path.stat().st_mtime_ns
    return items


def run_update():
    subprocess.run([sys.executable, str(ROOT / "update_index_version.py")], cwd=str(ROOT), check=False)


def main():
    print("Watcher versi dimulai...")
    last_state = discover_versions(ROOT)
    run_update()

    while True:
        current_state = discover_versions(ROOT)
        changed = False

        if set(current_state) != set(last_state):
            changed = True
        else:
            for name, mtime in current_state.items():
                if last_state.get(name) != mtime:
                    changed = True
                    break

        if changed:
            print("Perubahan file versi terdeteksi, memperbarui index...")
            run_update()
            last_state = current_state

        time.sleep(2)


if __name__ == "__main__":
    main()
