# SOP: VPN Blocked by Local Network or Public Wi-Fi Firewall

## Issue
VPN works fine at the office or at home, but fails specifically when connecting from certain locations — hotel Wi-Fi, airport Wi-Fi, a client site, or a public network.

## Common Causes
1. Public/guest networks often block the VPN protocol's specific ports (especially IPSec/IKEv2)
2. Captive portal on the public network hasn't been completed yet, blocking all traffic including VPN
3. The network's own firewall deliberately blocks outbound VPN traffic (common in hotels, some corporate guest networks)

## Resolution Steps
1. First confirm the user has completed the public network's captive portal login (open a browser to any HTTP site to trigger it) — VPN attempts will silently fail if the portal itself hasn't been passed yet.
2. If the portal is confirmed complete and VPN still fails, try switching the VPN client's protocol if it offers an alternative (e.g. SSL/TLS-based fallback instead of IPSec) — many restrictive networks block IPSec specifically but allow TLS-based VPN traffic on port 443 since it looks like regular HTTPS.
3. If no protocol fallback is available and the network is confirmed to be blocking VPN traffic, the practical workaround is using a personal mobile hotspot instead of the restrictive network.
4. Note the specific network/location in the ticket — if this is a recurring client site or travel destination, it's useful for the Network team to know which locations cause problems.

## Escalation
If this is a frequently-visited client site or partner location, escalate to Network team to evaluate whether a permanent protocol change or alternate VPN gateway config is worth implementing.

## SLA
P3 (single user, workaround available via hotspot) — target resolution 4 business hours.
