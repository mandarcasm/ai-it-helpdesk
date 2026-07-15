# SOP: Shared Mailbox Access Issues

## Issue
User cannot see a shared mailbox in Outlook, sees it but gets "Access Denied" when opening, or can view it but cannot send-as/send-on-behalf. Distinct from SOP "Outlook & Teams Sync / Login Issues" — the user's own mailbox works fine; this is specifically about a shared resource.

## Common Causes
1. Permissions granted in Exchange Online but Outlook cache hasn't refreshed (Outlook auto-mapping can take up to an hour, or require a restart)
2. Full Access permission granted but Send As / Send on Behalf not separately configured (these are distinct permission types)
3. Shared mailbox not auto-mapping because it was added manually instead of via Full Access delegation
4. User exceeded the practical limit of auto-mapped mailboxes in Outlook (performance degrades noticeably past ~10)

## Resolution Steps
1. Confirm in Exchange Admin Center > Recipients > Mailboxes > shared mailbox > Delegation, that the user actually has Full Access permission listed — don't take the requester's word for it, verify.
2. If permission is confirmed but not visible in Outlook, have the user fully close and reopen Outlook (not just remove/re-add the account) — auto-mapping applies on the next full profile load.
3. For send-as failures specifically, check that "Send As" is granted separately in the same Delegation panel — Full Access does not include this by default.
4. If the mailbox still won't appear after a restart, manually add it via File > Account Settings > double-click account > More Settings > Advanced > Add, using the shared mailbox's email address.
5. If the user has many shared mailboxes and Outlook is sluggish, recommend disabling auto-mapping for rarely-used ones and accessing those via Outlook on the Web instead.

## Escalation
Requests to grant Full Access to a shared mailbox require the mailbox owner's or manager's approval on the ticket before provisioning — treat as an access request, not purely a technical fix.

## SLA
P4 (access/config issue) — target resolution 1 business day.
