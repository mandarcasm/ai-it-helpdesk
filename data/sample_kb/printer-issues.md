# SOP: Network Printer Not Responding

## Issue
User cannot print, print jobs stuck in queue, or printer shows offline.

## Resolution Steps
1. Confirm printer is powered on and shows an active network connection (check printer's own display panel for IP address).
2. On the user's machine, open Services (services.msc) and restart the "Print Spooler" service.
3. If jobs are stuck, clear the spooler manually: stop Print Spooler service, delete all files in `C:\Windows\System32\spool\PRINTERS\`, restart the service.
4. Ping the printer's IP from the user's machine. If unreachable, the printer may have been assigned a new DHCP lease — check DHCP reservation and update the printer port if needed.
5. Confirm the user's device is on the correct VLAN/subnet as the printer (common issue after office moves or Wi-Fi reconnects).
6. If using driver-based printing, verify the correct driver version is installed — mismatched drivers after a Windows Update are a frequent cause.

## Escalation
If printer is unreachable network-wide (multiple users affected), escalate immediately to Network team as a P1 — this is a shared resource issue, not single-user.

## SLA
P3 (single user) — target resolution 4 business hours.
P1 (shared printer, multiple users) — target resolution 1 business hour.
