# SOP: Low Disk Space Warning

## Issue
Windows shows a "Low disk space" warning, or the user can't save files/install updates due to insufficient storage.

## Common Causes
1. Large local OneDrive cache with "always keep on this device" enabled for too many files
2. Accumulated temp files, old Windows Update leftovers, or browser cache
3. Local user profile bloated with downloads/desktop files never cleaned up
4. Hibernation file or System Restore points consuming significant space on smaller-capacity drives

## Resolution Steps
1. Run Disk Cleanup (search "Disk Cleanup" in Start) and select "Clean up system files" for the deepest clean — includes old Windows Update files that regular cleanup misses.
2. Check OneDrive settings > "Free up space" to convert rarely-used local files to online-only (cloud) rather than deleting them.
3. Check the Downloads folder specifically — this is the most common silent culprit, often gigabytes of forgotten installers and attachments.
4. For persistent low space on 128-256GB drives, consider disabling Hibernation (`powercfg /hibernate off` from an elevated prompt) if Fast Startup / Hibernate isn't required — frees several GB matching RAM size.
5. Confirm with the user before deleting anything from Desktop or Documents — those are personal files, not system clutter.

## Escalation
If the device's drive capacity is simply too small for the user's role (e.g. design/data work), escalate to the user's manager as a hardware spec issue, not a repeated cleanup ticket.

## SLA
P4 (single user) — target resolution 1 business day.
