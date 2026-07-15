# SOP: Shared Calendar Not Updating or Visible

## Issue
User can't see a shared team/resource calendar, or changes made to a shared calendar by one person aren't showing up for others.

## Common Causes
1. Calendar permission level too restrictive (e.g. "Can view when busy" instead of full details) — the calendar shows as present but with limited information, which users often mistake for a sync error
2. Local Outlook cache not refreshed after a permission change
3. Calendar shared via a personal invite rather than proper delegation, causing inconsistent visibility
4. Resource/room calendar auto-accept settings misconfigured, showing conflicting availability

## Resolution Steps
1. Confirm exactly what "not updating" means — is the calendar not appearing at all, or appearing but not showing event details? These have different causes.
2. Check the calendar owner's sharing settings for the requesting user's permission level — adjust to the appropriate level (view details vs. edit) rather than defaulting to full edit access unless needed.
3. Have the user remove and re-add the shared calendar in Outlook to force a fresh sync, rather than waiting for an automatic refresh which can take time.
4. For resource/room calendars, check the resource mailbox's auto-accept and conflict settings in Exchange Admin Center — misconfigured settings here cause the most confusing "shows busy but no event" reports.
5. Confirm the user is checking the correct calendar if multiple similarly-named calendars exist (common after team reorganizations).

## Escalation
If a resource/room calendar's booking behavior needs to change (e.g. auto-decline conflicts), this is a Facilities/Exchange admin configuration change — route accordingly rather than treating as a one-off user fix.

## SLA
P4 (single user) — target resolution 1 business day.
