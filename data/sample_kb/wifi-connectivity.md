# SOP: Wi-Fi Connectivity Issues

## Issue
Device won't connect to corporate Wi-Fi, connects but has no internet, or drops intermittently.

## Resolution Steps
1. Confirm the correct SSID is being used — corporate networks often have separate SSIDs for corp-managed vs BYOD devices with different auth methods.
2. For 802.1X/certificate-based auth failures, check that the device's Intune-issued certificate hasn't expired (common after 12-month cert lifecycle).
3. Forget the network on the device and reconnect fresh — stale cached credentials are the most common single cause.
4. Run `netsh wlan show wlanreport` to generate a diagnostic report if the issue is intermittent and hard to reproduce live.
5. Check for channel congestion or AP overload if multiple users in the same physical area report drops — this points to an infrastructure issue, not a device issue.
6. Confirm the device's Wi-Fi adapter driver is current, especially after a recent Windows Update.

## Escalation
Multiple simultaneous reports from the same floor/building = escalate to Network team as potential AP failure, not individual tickets.

## SLA
P3 (single user) — target resolution 4 business hours.
P2 (whole floor/area) — target resolution 2 business hours.
