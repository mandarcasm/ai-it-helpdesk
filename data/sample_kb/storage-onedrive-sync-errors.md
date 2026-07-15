# SOP: OneDrive Sync Errors

## Issue
OneDrive shows a red/yellow warning icon, files aren't syncing, or shows "Sync pending" indefinitely.

## Common Causes
1. File path too long (Windows has path length limits that OneDrive sync can hit with deeply nested folders)
2. File currently open/locked by another application preventing sync
3. Sync client stuck in a bad state after a network interruption
4. Storage quota reached (unlikely with standard business licensing, but possible with large media files)

## Resolution Steps
1. Click the OneDrive icon in the system tray to see the specific error — it usually names the problem file, not just "sync error" generically.
2. For "file path too long" errors, have the user shorten folder names or move deeply nested files closer to the root — OneDrive can't sync paths over Windows' length limit.
3. Close any files shown as currently open elsewhere that are blocking sync.
4. If sync is broadly stuck (not one file), try Pause Sync then Resume from the tray icon — this often clears a stuck state without needing a full reset.
5. As a deeper fix, use OneDrive's "Reset" option under Settings (or run `onedrive.exe /reset` then relaunch) — this doesn't delete files, just resets the local sync engine.
6. Check storage quota under OneDrive settings if the error specifically mentions storage limits.

## Escalation
If sync issues are affecting multiple users simultaneously, check Microsoft 365 Service Health first — may be a service-side issue, not local.

## SLA
P4 (single user) — target resolution 1 business day.
