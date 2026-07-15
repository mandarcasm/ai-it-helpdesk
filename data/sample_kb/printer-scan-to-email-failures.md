# SOP: Scan-to-Email Not Working

## Issue
Printer can print fine, but scan-to-email fails, scanned documents never arrive, or the printer shows an SMTP authentication error. This is a distinct function from print — do not troubleshoot as a general printer connectivity issue.

## Common Causes
1. Printer's stored SMTP relay credentials expired (common after a company-wide password rotation policy)
2. Modern Authentication / MFA enforcement on the mail relay account blocking legacy SMTP AUTH from the printer's firmware
3. Recipient's mailbox rejecting the message due to attachment size limits
4. Printer's scan-to-email configured with an outdated SMTP relay hostname after an Exchange Online migration

## Resolution Steps
1. Confirm whether the failure is happening at the printer (error shown on printer panel) or silently (printer says "sent" but nothing arrives) — these point to different causes.
2. Check the relay account's authentication method — most multifunction printers cannot do Modern Auth/MFA. Confirm the tenant has a dedicated SMTP AUTH exception or app password configured for this specific relay account, per Security policy.
3. Verify the relay account's password hasn't expired — printer firmware doesn't always surface a clear "auth failed" message.
4. Confirm SMTP server/port settings in the printer's admin panel match current Exchange Online relay settings (smtp.office365.com, port 587, STARTTLS) — these can go stale after tenant changes.
5. Test with a small single-page scan first to rule out attachment size limits before assuming it's an auth issue.

## Escalation
Any change to the SMTP relay account's authentication method or Conditional Access exemption must go through Security team — do not disable MFA on the relay account at the ticket level to "fix" this.

## SLA
P3 (single device) — target resolution 1 business day.
P2 (shared department printer, multiple users blocked) — target resolution 4 business hours.
