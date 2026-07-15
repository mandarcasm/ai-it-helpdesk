# SOP: Calendar or Meeting Invite Issues

## Issue
User isn't receiving meeting invites, accepted meetings don't show on their calendar, or a meeting they organized shows different details to different attendees.

## Common Causes
1. Inbox rule silently moving/deleting calendar invites (common when a user has an overly broad rule set up for a different purpose)
2. Time zone mismatch between organizer and attendee causing the meeting to appear at the wrong time
3. Recurring meeting was modified for a single occurrence, causing that instance to look different across attendees' calendars
4. Attendee's calendar sync delayed or stuck (see SOP "Outlook & Teams Sync / Login Issues" if this is the actual root cause)

## Resolution Steps
1. Check the user's inbox rules (Outlook Settings > Rules) for anything that might be filtering calendar invites — this is a frequently overlooked cause since the user often doesn't remember creating the rule.
2. Confirm both organizer's and attendee's time zone settings match their actual location — a wrong time zone setting is a very common and easy-to-miss cause of "wrong meeting time" complaints.
3. For recurring meeting discrepancies, ask specifically whether "this occurrence" or "the series" was edited — single-occurrence edits are a common source of confusion when only some attendees see the change.
4. If invites aren't arriving at all (not a display issue), confirm the meeting wasn't sent to a distribution list the user isn't a current member of, rather than to them directly.
5. Have the user try viewing their calendar via Outlook on the Web to isolate whether this is a local Outlook client issue or a genuine calendar data issue.

## Escalation
If multiple users report the same meeting showing different details, escalate to check Exchange Online calendar sync health rather than troubleshooting each attendee individually.

## SLA
P4 (single user) — target resolution 1 business day.
