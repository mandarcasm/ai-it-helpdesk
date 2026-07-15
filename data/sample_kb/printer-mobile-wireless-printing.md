# SOP: Mobile or Wireless Printing Failure

## Issue
User can't print from a mobile device (phone/tablet) or via wireless printing (AirPrint, Mopria, or similar) even though the printer works fine for standard desktop printing.

## Common Causes
1. Mobile device and printer are on different network segments/VLANs (common in offices with separate corporate and guest/mobile Wi-Fi)
2. Wireless printing protocol (AirPrint/Mopria) not enabled on the specific printer
3. Mobile device's printing app cache showing a stale/offline printer list
4. Print job blocked by mobile device management (MDM) policy on managed mobile devices

## Resolution Steps
1. Confirm the mobile device is on the same network segment as the printer — if the office uses a separate mobile/BYOD VLAN, wireless printing protocols often can't discover printers across VLAN boundaries without specific configuration.
2. Check the printer's control panel to confirm AirPrint (iOS) or Mopria (Android) is enabled — not all business printers have this on by default.
3. On the mobile device, remove and re-add the printer in the device's print settings to clear a stale discovery cache.
4. For managed/MDM-enrolled mobile devices, check whether a device policy is restricting printing — this is a deliberate control on some devices, not a bug.
5. If wireless discovery genuinely can't cross network segments, the practical fix is enabling a print bridge/server that's reachable from both segments — this is a Network/Facilities configuration change, not a per-device fix.

## Escalation
If this affects most mobile users in a specific building/floor, escalate to Network team to evaluate the VLAN configuration for printer discovery — fixing this centrally beats troubleshooting each device individually.

## SLA
P4 (single user) — target resolution 1 business day.
