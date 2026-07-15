# SOP: VPN Connected but Slow / High Latency

## Issue
User is successfully connected to SolsticeConnect VPN, but experiences slow file transfers, laggy remote desktop sessions, or high latency to internal apps. This is a performance complaint, not a connectivity failure — do not confuse with SOP "VPN Connection Failures."

## Common Causes
1. Split tunneling misconfigured — all traffic (including personal streaming/browsing) is being routed through the VPN tunnel instead of only internal traffic
2. User connected to a geographically distant VPN gateway instead of their nearest regional one
3. Local Wi-Fi signal is weak, and the user is misattributing Wi-Fi latency to the VPN
4. VPN gateway itself is under high load (check during month-end/quarter-end when remote usage spikes)

## Resolution Steps
1. Confirm split tunneling is enabled and correctly scoped — only traffic to internal IP ranges should route through the tunnel. Check the client's Connection Profile setting.
2. Verify the user is connected to their nearest regional gateway (client shows gateway location under Connection Details). Manually switch if it auto-selected a distant one.
3. Run a wired-connection test if possible to rule out local Wi-Fi as the actual bottleneck before blaming the VPN.
4. Check the VPN gateway dashboard (Network team access) for current load/session count — if the gateway is near capacity, this is an infrastructure issue, not a user issue.
5. Run `ping` and `tracert` to an internal resource with VPN connected vs disconnected to isolate whether the VPN itself is adding latency or if it's an upstream ISP issue.

## Escalation
If gateway load is confirmed high or multiple users report the same symptom in the same time window, escalate to Network Infrastructure as a capacity issue — do not keep closing these as individual P3 tickets.

## SLA
P3 (single user) — target resolution 4 business hours.
P2 (multiple users, same gateway/region) — target resolution 2 business hours.
