# SOP: Application Crashes Immediately on Launch

## Issue
A desktop application opens briefly then closes, or shows an error dialog immediately on launch. Distinct from an app that's simply slow or unresponsive — this is a hard crash on startup.

## Common Causes
1. Corrupted local app cache/config from an interrupted previous session
2. App version incompatible with a recent Windows Update
3. Conflicting add-in/plugin causing a startup crash (common in Office apps)
4. Missing or corrupted runtime dependency (.NET, Visual C++ Redistributable)

## Resolution Steps
1. Check Event Viewer > Application logs for the crash entry — note the faulting module, which usually points at the real cause (a specific DLL or add-in).
2. Try launching in Safe Mode if the app supports it (Office apps: `/safe` switch) to rule out a plugin/add-in conflict.
3. Clear the app's local cache/config folder (usually under `%appdata%` or `%localappdata%`) — safe to delete, it rebuilds automatically, but confirm no unsaved local data lives there first.
4. Confirm required runtimes are current: .NET Desktop Runtime and Visual C++ Redistributable, both pushable via Intune if missing.
5. If it started after a specific Windows Update, check whether other users on the same update are affected — may indicate a compatibility issue needing an app update, not a local fix.

## Escalation
If the crash is reproducible across multiple machines on the same app version, escalate to Endpoint Engineering to evaluate an app update or known-issue rollback.

## SLA
P3 (single user) — target resolution 4 business hours.
