# SOP: Outlook & Teams Sync / Login Issues

## Issue
Outlook stuck on "Trying to connect," Teams shows persistent sign-in loop, or mailbox not syncing new mail.

## Resolution Steps
1. Check Microsoft 365 Service Health dashboard first — confirm this isn't a tenant-wide outage before troubleshooting the local machine.
2. Have user run Outlook in Safe Mode (`outlook.exe /safe`) to rule out a corrupt add-in.
3. If Outlook is stuck connecting, delete the cached Outlook profile (Control Panel > Mail > Show Profiles) and let it rebuild — confirm OST file backup isn't needed first for offline data.
4. For Teams sign-in loops, clear the Teams cache: close Teams fully, delete contents of `%appdata%\Microsoft\Teams`, relaunch.
5. Confirm the account isn't hitting a Conditional Access block — check Entra ID Sign-in Logs for "Failure" status with a policy name attached.
6. If mail isn't syncing but Outlook shows "Connected," check mailbox size against quota — a full mailbox silently stops receiving new mail in some configurations.

## Escalation
If multiple users report simultaneous Outlook/Teams failures, treat as a potential Exchange Online or tenant-level issue — escalate to Cloud/Infrastructure team immediately rather than troubleshooting individually.

## SLA
P3 (single user) — target resolution 3 business hours.
