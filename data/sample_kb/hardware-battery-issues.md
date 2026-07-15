# SOP: Laptop Battery Not Charging or Draining Fast

## Issue
Laptop battery won't charge past a certain percentage, shows "Plugged in, not charging," or drains unusually fast even when idle.

## Common Causes
1. Charger/cable fault (most common — test with a known-good charger before anything else)
2. Battery health degraded from age (expected after roughly 2-3 years of daily use)
3. Background processes preventing sleep, keeping the device awake and draining power
4. Windows battery driver glitch showing incorrect charge state

## Resolution Steps
1. Test with a different charger/cable if one is available — rules out a simple cable fault before troubleshooting the device itself.
2. Check battery health via `powercfg /batteryreport` from Command Prompt, which generates an HTML report showing design capacity vs current full charge capacity — significant degradation means the battery itself needs replacing, not a software fix.
3. If "Plugged in, not charging" appears with a known-good charger, uninstall the battery driver in Device Manager (under Batteries) and let Windows reinstall it on restart.
4. For fast drain, check Battery Usage per app (Settings > System > Power & Battery) to identify what's preventing sleep or consuming excess power.
5. Confirm the user isn't running the laptop in extreme temperatures — heat significantly accelerates battery degradation.

## Escalation
Confirmed battery hardware failure (via battery report) should go to Asset Management for a replacement battery or device swap depending on age/warranty — not repeated troubleshooting.

## SLA
P3 (single user, device still usable plugged in) — target resolution 4 business hours to diagnose.
