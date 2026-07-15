# SOP: VPN Connection Failures

## Issue
User cannot connect to corporate VPN, or VPN connects but drops within minutes.

## Common Causes
1. Expired or incorrect credentials (especially after a recent password reset)
2. Outdated VPN client version
3. Local firewall/antivirus blocking the VPN adapter
4. DNS resolution failure over the VPN tunnel
5. MFA prompt not received (Microsoft Authenticator sync issue)

## Resolution Steps
1. Confirm the user's AD/Entra ID password is current — VPN often uses cached credentials that break after a password change.
2. Have the user fully close the VPN client (check Task Manager, not just the window) and relaunch as Administrator.
3. Run `ipconfig /flushdns` and `ipconfig /release && ipconfig /renew` before reconnecting.
4. Check Windows Defender Firewall > Allowed Apps — confirm the VPN client has both Private and Public network access enabled.
5. If MFA prompt isn't arriving, verify the user's Authenticator app time is synced (Settings > Time correction for codes) and confirm Conditional Access policy isn't blocking the sign-in risk level.
6. Check VPN concentrator logs for the user's session — look for repeated IKE/IPSec negotiation failures, which usually indicate a client version mismatch.
7. If the client is more than 2 versions behind current, uninstall and push the latest MSI via Intune.

## Escalation
If the issue persists after credential and client checks, escalate to Network team with: username, device hostname, timestamp of failed attempts, and VPN client version.

## SLA
P2 (business-impacting, single user) — target resolution 4 business hours.
