# SOP: Distribution List Emails Not Received

## Issue
A user reports they're not receiving emails sent to a distribution list they believe they're a member of, while other members receive it fine.

## Common Causes
1. User isn't actually a current member of the list (assumption doesn't match reality — verify, don't assume)
2. An inbox rule or Focused Inbox setting is routing list emails somewhere the user isn't checking
3. The list has moderation enabled and messages are pending approval, delaying delivery to everyone (not user-specific, but worth confirming)
4. Message size or attachment triggered a mailbox rule/filter for that specific user only

## Resolution Steps
1. Verify actual list membership in Exchange Admin Center first — don't troubleshoot delivery for someone who isn't actually on the list; this happens more often than expected.
2. Check the user's inbox rules and Focused/Other inbox split — list emails commonly get auto-sorted to "Other" and read as "not received."
3. Check the user's Junk/Clutter folder specifically for messages from that list's sender address.
4. If membership and filtering both check out, confirm with Exchange Admin Center message trace whether the email was actually delivered to that mailbox — this shows definitively whether it's a delivery issue or a user-side visibility issue.
5. For lists with moderation, confirm whether messages are stuck pending approval — this affects all members equally, so check if others are also missing the same message.

## Escalation
If message trace shows delivery failures specifically for this user across multiple lists (not just one), escalate to Exchange admin to check for a mailbox-level delivery restriction or quota issue.

## SLA
P4 (single user) — target resolution 1 business day.
