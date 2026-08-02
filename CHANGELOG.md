# Changelog

All notable changes to this project will be documented in this file.

## [9.4.2] - 2026-08-02
### Added
- Update public page version to `v9.4.2` in `index.html`.

### Changed
- Minor fixes and developer helper added (history debug button).



---

## Archived update logs (consolidated from archives/update-logs)

### [v(9, 3, 23)]

Change summary:
- Created a new release file: Score Calculator SVS v9.3.23.html
- Added responsive CSS rules for small screens so the calculator remains usable on phones and tablets
- Adjusted the layout for form rows, buttons, player cards, and action grids to prevent cramped or overflowing views on narrow displays
- Updated the visible version labels in the main HTML page and release file to v9.3.23

## Functional impact
- The calculator is now easier to use on mobile devices without horizontal overflow or crowded controls
- Desktop and larger-screen layouts remain unchanged, while smaller screens receive a more practical and readable arrangement

### [v(9, 3, 22)]

Change summary:
- Created a new release file: `Score Calculator SVS v9.3.22.html`
- Updated the HTML document title version metadata from the previous release value to `v9.3.22`
- Updated the footer version label from the previous release value to `V9.3.22`
- Kept the release file isolated as a new versioned build so the version history remains clear and consistent

## Reason for change
This release updates the visible version metadata for the latest distribution file and keeps the release history aligned with the new build.

### [v(9, 3, 21)]

Change summary:
- Created a new release file: `Score Calculator SVS v9.3.21.html`
- Updated the main header text to `SVS Championship` for a cleaner and more consistent branding presentation
- Reworked the subtitle area to better reflect the calculator purpose and team identity
- Updated the footer version text from `V9.3.20` to `V9.3.21`
- Kept the release isolated in a separate versioned file so the previous version remains available as a reference

## Reason for change
This release focuses on presentation and branding. The header and subtitle were refreshed to align the interface with the championship theme, while the footer version metadata was updated to match the new release.

### [v(9, 3, 20)]

Change summary:
- Created a new release file: `Score Calculator SVS v9.3.20.html`
- Updated the page title and footer version text from `v9.3.19` to `v9.3.20`
- Fixed the jungler-type toggle logic so the toggle buttons remain active only when the selected player role is `Jungler`
- Corrected the role-switching behavior so changing away from `Jungler` resets the related toggle state properly
- Added an immediate refresh call to `updateAllTfpHints()` after `setJunglerType()` to ensure TFP helper text stays synchronized with the selected role
- Kept the release isolated in a separate versioned file so the previous stable version remains available for rollback and comparison

## Reason for change
This update addresses a UI state issue in the jungler-role workflow. The previous behavior could leave stale toggle states active after changing roles, which made the interface inconsistent. The fix ensures the selection state is reset and the helper text updates immediately whenever the role changes.

## Notes
- `v9.3.20` is a new versioned release file built from `v9.3.19`
- The change is intentionally isolated in the new file to keep the version history clear and safe to review
- The update improves role-based UI consistency without altering the overall calculator logic

### [v(9, 3, 19)]

Change summary:
- Created new file: `Score Calculator SVS v9.3.19.html`
- Updated title and footer metadata from `v9.3.18` to `v9.3.19`
- Restored jungler type toggle visibility (`Tank` / `Other`) when a player is set to `Jungler`
- Ensured `Damage Taken` bonus (+3) applies only for Jungler Tank/Fighter types
- Fixed UI refresh logic so jungler toggle state is kept correct after role changes
- Removed stale `tfp-bonus` row reference from player UI update logic

## Reason for change
This release isolates the bug fix in a new version file while preserving the original `v9.3.18` file as a stable release.

## Notes
- `v9.3.19` is a new versioned release file built from `v9.3.18`.
- The fix ensures the jungler type toggle updates UI immediately and avoids dead row references in JavaScript.

### [v(9, 3, 18)]

Change summary:
- Created new file: `Score Calculator SVS v9.3.18.html`
- Updated version metadata in title and footer from `v9.3.17` to `v9.3.18`
- Fixed history delete action so `ts` values are compared as strings, preventing delete failures for older saved entries

## Reason for change
This update improves history deletion reliability and preserves correct versioning for the new release file.

## Notes
- `v9.3.18` is a new versioned release file with the same core behavior as `v9.3.17`, plus the history delete fix.
- The fix is intentionally isolated in the new versioned HTML file to keep update history clear.

### [v(9, 3, 17)]

Change summary:
- Created new file: `Score Calculator SVS v9.3.17.html`
- Kept the previous v9.3.16 behavior intact as the base version
- Added a separate versioned file for the sanitization-based fix so the original 9.3.16 remains unchanged
- Updated version metadata in title and footer from `v9.3.16` to `v9.3.17`

## Reason for change
This update preserves the earlier v9.3.16 file as the original release state and isolates the fix into a new versioned file, so the change history remains clearer and safer to track.

## Notes
- v9.3.16 is restored to the pre-fix state.
- v9.3.17 is the new version containing the improved handling for the earlier fix work.

### [v(9, 3, 16)]

Change summary:
- Created new file: `Score Calculator SVS v9.3.16.html`
- Updated version metadata in title and footer from `v9.3.15` to `v9.3.16`
- Fixed player-name handling so blank name fields now return `''` instead of `Player N`
- Added `input` listeners to `p1_name`..`p5_name` so `calc()` runs immediately when player names are typed
- Kept fallback display logic so users still see `Player N` in the breakdown when a name is not entered

## Reason for fix
This update resolves a bug where unnamed player slots could be incorrectly included in the team total and saved history because the code treated placeholder names as real player names.

## Verification
- Team total now excludes players without entered names
- Stats entered without a player name trigger a warning and do not affect the team score
- History saving and clipboard export now only include players with actual entered names

### [v(9, 3, 15)]

Change summary:
- Created new file: `Score Calculator SVS v9.3.15.html`
- Updated version metadata in title and footer from `v9.3.14` to `v9.3.15`
- Improved score-cell layout by adding `white-space: nowrap` so numeric values no longer wrap awkwardly in the summary and history sections

## Reason for fix
This update improves readability and visual consistency for score values on smaller screens and in dense score tables.

## Verification
- Score values remain aligned and readable in the summary and history display
- Version metadata now correctly shows `v9.3.15`

---

All archived update logs have been consolidated above; the original archive files remain in `archives/update-logs/`.
The batter to learn more.