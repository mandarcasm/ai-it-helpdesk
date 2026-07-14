# SOP: SolsticeConnect VPN Client Crashes on Launch

## Issue
The SolsticeConnect VPN client crashes immediately on launch, or the window opens and closes within a second with no error dialog.

## Common Causes
1. Corrupted client installation after a Windows Update
2. Conflicting VPN adapter left behind by a previously uninstalled VPN client (e.g. old Cisco AnyConnect or GlobalProtect remnants)
3. .NET runtime out of date on the endpoint
4. Corrupted local client config/cache in `%localappdata%\Solstice\Connect`

## Resolution Steps
1. Check Event Viewer > Windows Logs > Application for a SolsticeConnect crash entry — note the faulting module (usually points to a specific cause).
2. Have the user fully uninstall SolsticeConnect via Settings > Apps, then reboot before reinstalling — a reboot without reinstalling first clears locked adapter handles.
3. Check Device Manager > Network Adapters for any greyed-out or "unknown" VPN virtual adapters from old clients. Remove them.
4. Delete the config cache folder at `%localappdata%\Solstice\Connect` before reinstalling — this is safe, it only holds local session data, not credentials.
5. Confirm .NET Desktop Runtime 6.0+ is installed (`dotnet --list-runtimes` in Command Prompt). Push via Intune if missing.
6. Reinstall the latest SolsticeConnect MSI from the Intune Company Portal.

## Escalation
If crashes persist after a clean reinstall on a known-good machine image, escalate to Endpoint Engineering with the Event Viewer crash log attached — this may indicate a bad client build.

## SLA
P3 (single user, workaround: use VPN via alternate device) — target resolution 4 business hours.
