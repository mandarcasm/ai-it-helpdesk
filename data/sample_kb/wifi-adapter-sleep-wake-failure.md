# SOP: Wi-Fi Drops or Fails to Reconnect After Sleep/Wake

## Issue
Laptop connects to Wi-Fi normally at first login, but after the device sleeps (lid close, screen timeout) and wakes, Wi-Fi either doesn't reconnect automatically or the adapter disappears entirely until a reboot. Distinct from SOP "Wi-Fi Connectivity Issues" — this is a power-management/driver problem tied specifically to the sleep/wake cycle, not general connectivity.

## Common Causes
1. Windows power management set to allow Windows to turn off the Wi-Fi adapter to save power, and it fails to re-enable properly on wake
2. Outdated or buggy Wi-Fi adapter driver with a known sleep/wake bug (common on certain Intel and Realtek chipsets after specific Windows Update releases)
3. Fast Startup enabled, causing an inconsistent hardware re-initialization state
4. Docking station Wi-Fi/Ethernet switching conflict on wake

## Resolution Steps
1. Device Manager > Network Adapters > right-click the Wi-Fi adapter > Properties > Power Management tab — uncheck "Allow the computer to turn off this device to save power."
2. Check Windows Update history for a recent driver update coinciding with when the issue started — if so, roll back the specific driver via Device Manager > Update Driver > Roll Back.
3. Disable Fast Startup: Control Panel > Power Options > Choose what the power buttons do > uncheck "Turn on fast startup."
4. If the issue only happens when docked, test undocked through a full sleep/wake cycle to isolate whether the dock itself is the trigger.
5. As a more permanent fix, push the latest OEM-tested Wi-Fi driver (not the generic Windows Update one) via Intune for affected device models.

## Escalation
If this is affecting a specific laptop model fleet-wide, escalate to Endpoint Engineering to evaluate a standard driver package rollout rather than fixing devices one at a time.

## SLA
P3 (single user) — target resolution 4 business hours.
