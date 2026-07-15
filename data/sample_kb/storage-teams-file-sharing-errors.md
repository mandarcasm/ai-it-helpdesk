# SOP: Teams File Sharing / Permission Errors

## Issue
User can't upload, share, or open a file within a Teams channel, or an external participant can't access a file shared during a meeting.

## Common Causes
1. Files shared in a Teams channel actually live in the underlying SharePoint site — permission issues there manifest inside Teams (see SOP "SharePoint Access or Permission Issues" for the root cause)
2. External/guest participant lacks the right sharing permissions for the specific file
3. File type blocked by a data-loss-prevention or file-type restriction policy
4. Channel was deleted or archived, orphaning previously shared files

## Resolution Steps
1. Confirm whether the issue is with a specific file or all files in the channel — a single file issue is usually a permission/sharing setting on that file; a broad issue points to the channel's underlying SharePoint site.
2. For external participants unable to access a shared file, check the org's external sharing policy — Teams respects the same guest/external sharing rules as SharePoint and OneDrive.
3. If a file type is blocked (e.g. certain executable or script file types), this is usually a deliberate DLP policy — confirm the legitimate business need and route as a policy exception request if warranted, don't attempt to bypass it.
4. For files from a deleted/archived channel, check the Teams team's associated SharePoint site directly — files often persist there even after the channel view is gone.

## Escalation
Requests to loosen external sharing permissions org-wide (not per-file) require Security review — this is a policy change, not a per-ticket fix.

## SLA
P4 (single user/file) — target resolution 1 business day.
