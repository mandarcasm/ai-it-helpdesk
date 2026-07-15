# SOP: Guest Wi-Fi Onboarding Failures

## Issue
Visitor or contractor cannot connect to the Guest Wi-Fi network, portal page doesn't load, or they connect but have no internet access. Distinct from SOP "Wi-Fi Connectivity Issues" which covers corporate-managed device Wi-Fi problems — Guest Wi-Fi has no device management or certificates involved.

## Common Causes
1. Captive portal page not loading due to the guest device's private DNS or "Limit IP address tracking" setting interfering with portal redirect
2. Daily/session guest access code expired or not yet activated by reception/front desk
3. Guest device connected to the wrong SSID (confusing Guest network with the internal corporate SSID, which will reject it entirely)
4. Guest network reaching device limit during high-visitor periods (e.g. large meetings, conferences)

## Resolution Steps
1. Confirm the guest is connecting to the correct SSID — the naming should be clearly distinct from the corporate network (e.g. "CompanyName-Guest" vs "CompanyName-Corp").
2. If the captive portal won't load, have the guest open a plain HTTP (not HTTPS) site manually to trigger the redirect, or try a different browser — some browsers' private DNS settings block captive portal detection.
3. Verify with reception/front desk that a valid guest code was issued and is within its active time window.
4. If the guest connects but has no internet, check the Guest VLAN's upstream firewall rule is active — a rule left disabled after maintenance is a common recurring cause.
5. During high-occupancy events, check AP client count against capacity — if maxed out, this is a capacity planning issue, not a per-guest fault.

## Escalation
Recurring Guest Wi-Fi failures across multiple visitors on the same day should be escalated immediately to Network team as a potential portal or VLAN outage, not queued as individual tickets.

## SLA
P3 (single guest) — target resolution 2 business hours (guest access is often time-sensitive).
P2 (multiple guests, event in progress) — target resolution 30 minutes.
