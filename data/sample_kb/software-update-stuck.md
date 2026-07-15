# SOP: Application Update Stuck or Failing

## Issue
An application shows "Update available" but the update never completes, gets stuck at a percentage, or fails with an error.

## Common Causes
1. Insufficient disk space for the update package
2. Update service (e.g. Office Click-to-Run) in a stuck/corrupted state from a previous failed attempt
3. Network policy blocking the update download source
4. App was open and in use during the update attempt

## Resolution Steps
1. Check available disk space first (`This PC` in File Explorer) — most updates need several GB free temporarily even for a small final install size.
2. Fully close the application (check Task Manager, not just the window) before retrying the update.
3. For Microsoft 365 apps specifically, run the Office repair tool: Settings > Apps > Microsoft 365 > Modify > Online Repair — this resets a stuck Click-to-Run state.
4. Confirm the update isn't being blocked by a firewall/proxy policy — check if other users on the same network segment have the same stuck update.
5. As a last resort, uninstall and push a fresh install via Company Portal rather than continuing to retry a broken in-place update.

## Escalation
If the same update is stuck fleet-wide, escalate to Endpoint Engineering — this may indicate a bad update package or a blocked update source needing a firewall rule change.

## SLA
P4 (single user) — target resolution 1 business day.
