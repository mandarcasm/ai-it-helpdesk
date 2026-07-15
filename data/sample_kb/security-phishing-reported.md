# SOP: Phishing Email Reported by User

## Issue
A user reports receiving a suspicious email — potential phishing, a spoofed sender, or a malicious link/attachment.

## Resolution Steps
1. Treat every report as genuine until proven otherwise — never dismiss a phishing report without review, even if the user seems unsure.
2. If the user clicked a link or opened an attachment, prioritize this ticket immediately as time-sensitive — ask whether they entered any credentials on a resulting page.
3. Do not open the email's links or attachments yourself on a standard workstation — review headers and content safely via the email security platform's quarantine/preview tools, or a sandboxed environment.
4. If credentials were entered on a phishing page, immediately force a password reset and revoke active sessions for that user (see SOP "Password Reset & Account Lockout" for the reset itself) — this step cannot wait.
5. Use the reported message to search the mail environment for other recipients of the same phishing campaign, and quarantine/delete it tenant-wide if found elsewhere.
6. Confirm with the user whether they forwarded or replied to the email, since that may have exposed other people.

## Escalation
Any case involving entered credentials, a suspected compromised account, or a campaign hitting multiple users must be escalated to Security immediately as an incident — this is not a routine ticket queue item.

## SLA
P1 (credentials entered or malware suspected) — target resolution: immediate escalation, response within 30 minutes.
P3 (reported, not clicked/opened) — target resolution 4 business hours for review.
