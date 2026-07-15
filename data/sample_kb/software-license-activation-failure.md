# SOP: Software License Activation Failure

## Issue
An installed application shows "Unlicensed," "Activation required," or a trial-expired banner, even though the user should have a valid license.

## Common Causes
1. License assigned in the admin portal but not yet synced to the device (can take up to a few hours)
2. User signed into the app with a personal account instead of their work account
3. License pool exhausted — all seats for that app are currently assigned to other users
4. Device not enrolled/compliant, so it fails the license check tied to Conditional Access

## Resolution Steps
1. Confirm in the software licensing admin portal (e.g. Microsoft 365 admin center for Office apps) that a license is actually assigned to this user.
2. Have the user fully sign out of the app and sign back in with their work account specifically — check under the app's Account settings which identity is active.
3. If licenses are assigned correctly but activation still fails, have the user restart the device — some apps only re-check license state on boot.
4. Check the license pool's available seat count — if at zero, this becomes a procurement/reallocation request, not a technical fix.

## Escalation
Seat pool exhaustion should be flagged to IT Asset Management for additional license procurement — don't keep reassigning between users as a workaround.

## SLA
P3 (single user, license confirmed assigned) — target resolution 4 business hours.
P4 (seat pool exhausted, procurement needed) — target resolution 3 business days.
