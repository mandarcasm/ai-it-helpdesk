# SOP: Wi-Fi Drops When Moving Between Access Points (Roaming)

## Issue
User's device disconnects or has a brief interruption specifically when walking between areas of the building covered by different Wi-Fi access points — not a general connectivity problem, only happens in transit.

## Common Causes
1. Device isn't roaming aggressively enough — it stays connected to a weakening signal from the old AP too long before switching to a stronger nearby one
2. Overlapping AP coverage is misconfigured, leaving a dead zone between access points
3. Device's Wi-Fi adapter power-saving settings delaying reconnection
4. Fast roaming (802.11r) not enabled or not supported by the device, causing a full re-authentication (including MFA/certificate check) on every AP switch instead of a fast handoff

## Resolution Steps
1. Confirm the pattern — does this happen at consistent physical locations (pointing to a coverage gap) or randomly anywhere in the building (pointing to a device-side roaming setting)?
2. Check the device's Wi-Fi adapter power management (Device Manager > Wi-Fi adapter > Power Management) — disable power saving on the adapter as a first test, similar to the fix for general Wi-Fi sleep/wake issues.
3. If it's location-consistent, this is a coverage/infrastructure issue — report the specific location to Network team for an AP placement or power-level review rather than continuing to troubleshoot the device.
4. Confirm whether the network has 802.11r (Fast Transition) enabled — if not, every AP handoff requires full re-authentication, which is slow and feels like a drop even though it's technically reconnecting successfully.
5. For a quick single-user test, have them manually forget and rejoin the network to rule out a corrupted local Wi-Fi profile as a contributing factor.

## Escalation
Location-consistent roaming drops affecting multiple users are an AP coverage/configuration issue — escalate to Network Infrastructure with the specific location, don't treat as a per-device fix.

## SLA
P3 (single user) — target resolution 4 business hours.
P2 (consistent dead zone affecting multiple users in one area) — target resolution 2 business hours to assess.
