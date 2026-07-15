# SOP: Shared or Service Account Password Change Request

## Issue
A request to change the password for a shared mailbox account, service account, or a shared login used by a team (e.g. a social media account, a shared vendor portal login) — distinct from an individual's personal account password.

## Resolution Steps
1. Confirm the requester is an authorized owner of the shared/service account — these often have a designated owner or team lead who must approve changes, not just anyone on the team.
2. For service accounts tied to automated processes (scripts, integrations, scheduled tasks), check what depends on this account BEFORE changing the password — an uncoordinated password change can break production automation silently.
3. Coordinate the change with whoever owns any dependent systems, and schedule it during a low-impact window if the account is business-critical.
4. Update the new password in the organization's password vault/secrets manager immediately — never leave a shared credential only known to one person or communicated over chat/email.
5. For shared mailboxes and team accounts, communicate the change to all authorized users through a secure channel, and confirm each dependent integration is updated before considering the ticket closed.

## Escalation
Service accounts with access to production systems or sensitive data require Security sign-off before any password change, and should ideally be migrated to certificate-based or managed identity authentication rather than static passwords where possible — flag this as a modernization opportunity if the account is still password-based.

## SLA
P4 (standard shared account) — target resolution 2 business days, coordinated with dependent system owners.
P2 (service account with production dependencies) — target resolution requires a scheduled change window, not immediate.
