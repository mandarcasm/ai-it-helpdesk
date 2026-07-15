# SOP: USB / Removable Media Blocked

## Issue
User plugs in a USB drive or other removable media and it's not recognized, or Windows shows a policy-blocked notification.

## Resolution Steps
1. Confirm this is expected behavior first — most managed endpoints block unauthorized removable media by default as a data-loss-prevention security control, not a fault.
2. Ask the user what legitimate business need requires USB access — this determines whether the right path is a policy exception request or an alternative (e.g. use OneDrive/SharePoint for file transfer instead).
3. If there's a genuine business need (e.g. transferring files from an air-gapped system, or specific hardware requiring a USB dongle), this requires a formal exception request with manager approval, not a direct unblock.
4. For approved exceptions, the policy change should be scoped to the specific device or user, with an expiration date if the need is temporary — not a blanket USB policy change.
5. If the user simply needs to move files and doesn't have a specific hardware requirement, redirect them to approved cloud storage transfer methods instead of pursuing a USB exception at all.

## Escalation
All USB policy exception requests must go through Security review and approval — do not disable USB restrictions at the ticket level under any circumstances.

## SLA
P4 (policy exception request) — target resolution 2 business days, pending Security approval.
