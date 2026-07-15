# SOP: VPN Certificate Expired

## Issue
VPN connection fails specifically with a certificate error, or was working fine and suddenly stopped around the same time each year — a strong signal of certificate expiry rather than a general connection fault.

## Common Causes
1. Client certificate used for VPN authentication reached its expiration date (typically 12-month lifecycle)
2. Certificate renewal via Intune failed silently and wasn't reissued
3. Device clock significantly wrong, causing a valid certificate to appear expired or not-yet-valid

## Resolution Steps
1. Check the certificate error message specifically — "certificate expired," "certificate not trusted," and "certificate not yet valid" all point to different root causes.
2. Confirm the device's date/time is correct and set to automatic — a wrong clock can make a perfectly valid certificate appear invalid.
3. Check Intune's certificate deployment status for this device — if the renewal task failed, trigger a manual sync (Company Portal > Sync) to retry issuance.
4. If the certificate profile itself needs troubleshooting (not just a one-off failed renewal), check whether the device is still correctly enrolled and compliant, since certificate deployment depends on compliance status.

## Escalation
If multiple users hit certificate expiry around the same date, this indicates a batch of certificates issued together are expiring together — escalate to Identity/PKI team to review the certificate renewal automation before it recurs.

## SLA
P3 (single user) — target resolution 4 business hours.
