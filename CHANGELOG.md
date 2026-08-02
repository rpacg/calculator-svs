# Changelog

All notable changes to this project will be documented in this file.

## [9.4.2] - 2026-08-02
### Added
- Update public page version to `v9.4.2` in `index.html`.

### Changed
- Minor fixes and developer helper added (history debug button).



---

## Archived update logs (consolidated from archives/update-logs)

### [v9.3.23]
Change summary:
- Created a new release file `Score Calculator SVS v9.3.23.html` and updated visible version labels to `v9.3.23` in the main page and release file.
- Added responsive CSS rules and layout adjustments to make the calculator usable on phones and tablets (form rows, buttons, player cards, action grids).

Functional impact:
- Improves mobile usability by preventing cramped or overflowing views on narrow displays; desktop layouts remain unchanged.

### [v9.3.22]
Change summary:
- Created `Score Calculator SVS v9.3.22.html` and updated the HTML title and footer version metadata to `v9.3.22`.

Reason / impact:
- Keeps visible version metadata aligned with the release distribution and preserves a separate versioned build for historical clarity.

### [v9.3.21]
Change summary:
- Created `Score Calculator SVS v9.3.21.html`.
- Updated the main header text to `SVS Championship` and reworked subtitle area for clearer branding and purpose.

Reason / impact:
- Presentation and branding refresh: clearer header/subtitle and matching footer metadata, with the previous version preserved as a separate file.

### [v9.3.20]
Change summary:
- Created `Score Calculator SVS v9.3.20.html` and bumped page title/footer from `v9.3.19` to `v9.3.20`.
- Fixed UI state for jungler-type toggle so toggles are only active for the `Jungler` role and reset correctly when switching roles. Also ensured `updateAllTfpHints()` runs after `setJunglerType()`.

Reason / impact:
- Resolves inconsistent toggle state and keeps helper text synchronized when changing player roles. No changes to core calculator logic.

### [v9.3.19]
Change summary:
- Created `Score Calculator SVS v9.3.19.html` and updated title/footer metadata to `v9.3.19`.
- Restored jungler-type toggle visibility and ensured `Damage Taken` bonus (+3) applies only to Jungler Tank/Fighter types. Fixed UI refresh logic and removed stale `tfp-bonus` row references.

Reason / impact:
- Fixes UI inconsistencies related to jungler toggles and safeguards against broken references that could cause display or logic errors.

### [v9.3.18]
Change summary:
- Created `Score Calculator SVS v9.3.18.html` and updated version metadata to `v9.3.18`.
- Fixed history delete action so `ts` values are compared reliably (prevents delete failures for older entries).

Reason / impact:
- Improves reliability of deleting saved history entries across different saved formats/ts types.

### [v9.3.17]
Change summary:
- Created `Score Calculator SVS v9.3.17.html` to isolate a sanitization-based fix while keeping `v9.3.16` unchanged.

Reason / impact:
- Keeps the prior release file intact for reference and places the fix into a new versioned build for clearer history and safer rollbacks.

### [v9.3.16]
Change summary:
- Created `Score Calculator SVS v9.3.16.html` and updated title/footer metadata to `v9.3.16`.
- Fixed player-name handling: unnamed fields return `''` rather than `Player N`; added `input` listeners to name fields so `calc()` runs immediately when names are typed.

Reason / impact:
- Prevents unnamed slots from being treated as real players in team totals and saved history; improves real-time feedback while typing names.

Verification:
- Team totals exclude players without entered names; history saving and clipboard export include only players with actual entered names.

### [v9.3.15]
Change summary:
- Created `Score Calculator SVS v9.3.15.html` and updated title/footer metadata to `v9.3.15`.
- Improved score-cell layout by adding `white-space: nowrap` to prevent numeric values from wrapping in summary and history sections.

Reason / impact:
- Improved readability and visual consistency of score values on small screens and dense displays.

---

### [3.4] - 2026-08-02
### Added
- Simple match history trend chart for per-match metrics in the history tab.
- Dropdown selector for metric type: average total score, average kill, and average damage.

### Changed
- Updated page version labels from `v9.3.23` to `v3.4` in `index.html`.

### Notes
- History chart is rendered from saved local storage score history and displays a simple bar chart per match.

---

All archived update logs have been consolidated above; the original archive files remain available under `archives/update-logs/`.
