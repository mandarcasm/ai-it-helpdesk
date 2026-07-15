# SOP: New Hire Account & Device Setup

## Issue
A new employee's start date is confirmed and IT needs to provision their account and device before day one.

## Resolution Steps
1. Confirm HR has submitted the new hire request with role, department, manager, and start date — do not begin provisioning from a verbal request alone.
2. Create the Entra ID account with the standard naming convention, assign the correct license bundle (M365, any role-specific apps) based on department.
3. Add the user to the standard department security groups and any role-specific distribution lists — check the role's access template rather than guessing.
4. Provision a device from stock: apply the standard endpoint image, confirm it enrolls into Intune and shows compliant before handover.
5. Set a temporary password with forced change at first login, and pre-register the account for MFA enrollment on day one under IT supervision — don't leave MFA setup to the new hire unsupervised on their first day.
6. Prepare a day-one welcome document covering: how to log in, how to reach IT, and where to find internal resources.

## Common Follow-up Issues
- New hire's manager requests access to a system not in the standard template — this needs manager approval on the ticket before provisioning, not automatic granting.
- Device isn't ready by start date — escalate immediately to Asset Management rather than scrambling on day one.

## Escalation
Missing HR paperwork or unclear role/access requirements should be escalated back to HR/the hiring manager before account creation — provisioning without correct info creates cleanup work later.

## SLA
P3 (new hire request) — target resolution: account and device ready 1 business day before start date.
