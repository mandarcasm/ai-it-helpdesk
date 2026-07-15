# SOP: Lost or Stolen Device Reported

## Issue
An employee reports their company laptop or phone is lost or stolen.

## Resolution Steps
1. Treat this as time-sensitive from the first report — every minute of delay is a window for data exposure on an unrecovered device.
2. Immediately revoke all active sessions for the user's account (Entra ID > user > Revoke Sessions) in case the device had cached credentials or an active login.
3. Trigger a remote lock and, if the device doesn't reappear within a defined grace period set by policy, a remote wipe via Intune — confirm with the user's manager and Security before wiping if there's any chance of imminent recovery, but don't delay the lock.
4. Check whether the device's disk was encrypted (BitLocker) — this significantly changes the risk assessment; document encryption status in the incident record.
5. Ask the user for the last known location and circumstances (left in a cab, stolen from a bag, etc.) — this matters for the incident report, and for a police report if theft is involved.
6. Coordinate with Asset Management to mark the device as lost/stolen in inventory once confirmed, and initiate replacement provisioning for the user in parallel.

## Escalation
Every lost or stolen device report is a Security incident by default — escalate immediately, do not treat as a routine asset ticket. If the device held access to particularly sensitive systems or data, this may also require a formal breach assessment per company policy.

## SLA
P1 (device lost or stolen) — target resolution: session revocation and lock within 15 minutes of report.
