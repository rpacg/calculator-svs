#!/usr/bin/env python3
"""
Merge archived update-log files into CHANGELOG.md in newest->old order.

Usage: python scripts/merge_changelog.py

This script looks for markdown files under `archives/update-logs/`, sorts
them by semantic version (newest first), consolidates their summaries into
an "Archived update logs" section, and replaces or appends that section in
`CHANGELOG.md`.

It is idempotent and keeps the rest of CHANGELOG.md intact.
"""
import re
import pathlib
from packaging.version import Version, InvalidVersion

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARCHIVE_DIR = ROOT / 'archives' / 'update-logs'
CHANGELOG = ROOT / 'CHANGELOG.md'

START_MARKER = '## Archived update logs (consolidated from archives/update-logs)'
END_SNIPPET = 'All archived update logs have been consolidated above;'


def parse_version_from_filename(name: str):
    # Expect formats like v9.3.23-update-log.md or v9.3.23.md
    m = re.search(r'v?(\d+\.\d+(?:\.\d+)?)', name)
    if not m:
        return None
    try:
        return Version(m.group(1))
    except InvalidVersion:
        return None


def build_consolidated_section():
    files = [p for p in ARCHIVE_DIR.glob('*.md') if p.is_file()]
    entries = []
    for p in files:
        ver = parse_version_from_filename(p.name)
        entries.append((ver, p))
    # sort: newest first; versions that fail to parse go to the end
    entries.sort(key=lambda x: (x[0] is None, x[0]), reverse=True)

    lines = [START_MARKER, '']
    for ver, p in entries:
        label = f'[{p.stem}]' if ver is None else f'[v{ver}]'
        lines.append(f'### {label}')
        lines.append('')
        try:
            content = p.read_text(encoding='utf-8').strip()
        except Exception:
            content = f'*Could not read {p.name}*'
        # Include the Change summary section from the archived file if present
        # We will take everything after the first H2 (## Change summary) or include full content
        m = re.search(r'## Change summary\n([\s\S]*)', content, re.IGNORECASE)
        if m:
            summary = m.group(1).strip()
        else:
            # fallback: include first 20 lines
            summary = '\n'.join(content.splitlines()[:20])
        lines.append('Change summary:')
        for l in summary.splitlines():
            lines.append(l)
        lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('All archived update logs have been consolidated above; the original archive files remain in `archives/update-logs/`.')
    lines.append('')
    return '\n'.join(lines)


def replace_section(changelog_text: str, new_section: str) -> str:
    if START_MARKER in changelog_text:
        start = changelog_text.index(START_MARKER)
        # find end snippet if present
        end_idx = changelog_text.find(END_SNIPPET, start)
        if end_idx != -1:
            # include the END_SNIPPET line in the replacement
            # find the end of that line
            end_line_idx = changelog_text.find('\n', end_idx)
            if end_line_idx == -1:
                end_line_idx = len(changelog_text)
            new_text = changelog_text[:start] + new_section + changelog_text[end_line_idx+1:]
            return new_text
        else:
            # no explicit end, replace from start to end of file
            return changelog_text[:start] + new_section
    else:
        # append at end
        if not changelog_text.endswith('\n'):
            changelog_text += '\n'
        return changelog_text + '\n' + new_section


def main():
    if not ARCHIVE_DIR.exists():
        print('No archive dir found:', ARCHIVE_DIR)
        return
    new_section = build_consolidated_section()
    text = CHANGELOG.read_text(encoding='utf-8') if CHANGELOG.exists() else '# Changelog\n\n'
    new_text = replace_section(text, new_section)
    CHANGELOG.write_text(new_text, encoding='utf-8')
    print('CHANGELOG.md updated with consolidated archived logs.')


if __name__ == '__main__':
    main()
