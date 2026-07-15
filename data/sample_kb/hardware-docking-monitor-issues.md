# SOP: Docking Station or External Monitor Not Detected

## Issue
Laptop connected to a docking station or external monitor doesn't detect the display, shows a blank/flickering screen, or peripherals connected through the dock (keyboard, mouse, USB devices) don't work.

## Common Causes
1. Cable connection issue (loose or wrong port — many docks have both DisplayPort and HDMI, mixing them up is common)
2. Docking station firmware/driver outdated
3. Laptop's display settings not detecting the second/external monitor automatically
4. Dock isn't receiving enough power (common with high-resolution monitors plus multiple USB peripherals on underpowered docks)

## Resolution Steps
1. Confirm physical connections are fully seated — reseat the dock cable and monitor cable even if they look connected.
2. Press Windows key + P to open the display detection menu and manually select "Extend" or "Duplicate" — this alone fixes a large share of "monitor not detected" cases.
3. Check Device Manager for the dock/display adapter showing a driver error (yellow warning icon) — update via Windows Update or the manufacturer's site if so.
4. If USB peripherals through the dock aren't working but the monitor is fine, try a different USB port on the dock — some docks have known-flaky ports.
5. For docks powering large monitors plus multiple accessories, confirm the dock's power adapter is the correct wattage — underpowered setups cause intermittent, hard-to-diagnose failures.
6. Test the laptop with a direct cable to the monitor (bypassing the dock) to isolate whether the fault is the dock or the monitor/cable itself.

## Escalation
If a specific dock model shows a pattern of failures across multiple users, escalate to Endpoint Engineering to evaluate a firmware update or hardware batch issue.

## SLA
P3 (single user) — target resolution 4 business hours.
