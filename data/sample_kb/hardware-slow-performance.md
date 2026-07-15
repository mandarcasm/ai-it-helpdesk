# SOP: Laptop Running Slow / High CPU or Disk Usage

## Issue
User reports their laptop is generally slow — apps take long to open, typing lags, or the fan runs constantly. Distinct from a single app crashing; this is overall system performance.

## Common Causes
1. Too many startup programs launching automatically at boot
2. Background sync processes (OneDrive, antivirus scan) competing for resources
3. Low disk space triggering aggressive background cleanup/indexing
4. Malware or an unusually resource-heavy rogue process (less common, but check)

## Resolution Steps
1. Open Task Manager (Ctrl+Shift+Esc) and sort by CPU and by Memory separately — identify if one process is consistently dominating or if it's broadly spread across many.
2. Check Task Manager > Startup tab and disable non-essential startup programs — this is the single most common fix for general slowness.
3. Confirm whether a large OneDrive sync or antivirus full scan is running — these are expected to slow things temporarily, not a fault.
4. Check free disk space — under about 10-15% free space causes noticeable slowdowns as Windows struggles to manage virtual memory.
5. If a single unfamiliar process is consuming high resources persistently, do not kill it blindly — note the process name and escalate to Security to rule out malware before assuming it's benign.

## Escalation
If performance issues persist after ruling out the above and the device is more than 3-4 years old, this may be a hardware refresh conversation rather than a fixable software issue — flag to the user's manager for asset planning.

## SLA
P3 (single user, workaround available) — target resolution 4 business hours.
