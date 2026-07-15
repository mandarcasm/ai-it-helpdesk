# SOP: Application Install Blocked or Fails

## Issue
User tries to install an application and gets an "Access Denied" message, or the install fails partway through.

## Common Causes
1. Standard users lack local admin rights on managed endpoints (by design)
2. App isn't in the approved Company Portal catalog yet
3. Installer conflicts with an existing older version still partially present

## Resolution Steps
1. Confirm whether the app is available in the Intune Company Portal / Software Center — this is the supported self-service install path for approved apps.
2. If it's not listed, check whether it's an approved app awaiting packaging, or a net-new request that needs manager + security approval first.
3. For apps that fail even via Company Portal, check Intune's install logs for the device — a common cause is a stuck older version; uninstall the old version first, then retry.
4. Never grant temporary local admin to work around this — use Intune's "Install as System" for one-off approved installs instead.

## Escalation
Requests for new (not-yet-approved) software go to the Software Approval process, not a standard ticket — flag ownership before promising a timeline.

## SLA
P4 (self-service via Company Portal) — target resolution same day.
P3 (new software approval needed) — target resolution 3 business days.
