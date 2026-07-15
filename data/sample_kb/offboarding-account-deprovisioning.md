# SOP: Employee Offboarding / Account Deprovisioning

## Issue
An employee is leaving the company and their account and access need to be deactivated on their last day (or immediately, for involuntary terminations).

## Resolution Steps
1. Confirm the termination request came through HR with an exact effective date and time — involuntary terminations often require immediate action, coordinate timing precisely with HR/Security for these.
2. Disable (do not immediately delete) the Entra ID account — this preserves mailbox/OneDrive data for the legally required retention period while blocking sign-in.
3. Revoke all active sessions immediately (Entra ID > user > Revoke Sessions) — disabling the account alone doesn't kill already-active tokens.
4. Remove the user from all security groups and distribution lists, but leave their mailbox intact and convert it to a shared mailbox if the manager needs ongoing access to it.
5. Set up mail forwarding or an out-of-office auto-reply only if instructed by the manager/HR — don't do this by default without explicit instruction.
6. Notify Asset Management to arrange device and badge return.

## Common Follow-up Issues
- Manager requests access to the departed employee's files/mailbox — this requires HR or Legal approval before granting, don't provision on a verbal request alone.
- Scheduled emails or automated processes were tied to the departed user's account — check with their team before full deprovisioning.

## Escalation
Involuntary/for-cause terminations should be treated as time-sensitive Security actions — coordinate directly with Security and HR for exact timing rather than treating as a standard ticket queue item.

## SLA
P2 (involuntary termination, immediate access revocation required) — target resolution: same hour as notification.
P3 (standard resignation, scheduled) — target resolution: effective on last working day.
