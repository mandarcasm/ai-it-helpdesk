# SOP: Multiple Saved Wi-Fi Profiles Causing Connection Conflicts

## Issue
Device has trouble connecting or connects to the wrong network when multiple similarly-named or overlapping Wi-Fi networks are in range — common for users who travel between company offices with the same SSID name, or who have old conference/guest networks still saved.

## Common Causes
1. Multiple saved profiles for SSIDs with the same name but different security settings across office locations
2. An old, no-longer-valid saved network with a higher connection priority than the correct current one
3. Auto-connect enabled for a weaker/wrong network that happens to be prioritized
4. Corrupted individual Wi-Fi profile causing repeated failed connection attempts that block trying other networks

## Resolution Steps
1. Run `netsh wlan show profiles` from Command Prompt to list all saved networks on the device — this often reveals far more saved networks than the user remembers, including old ones from past locations or events.
2. Identify and remove outdated or duplicate profiles: `netsh wlan delete profile name="ProfileName"` — clean up anything not currently relevant rather than leaving clutter that can interfere with auto-connect priority.
3. Check connection priority order in Wi-Fi settings (Manage known networks) and confirm the correct/current network is prioritized above old ones.
4. For company offices sharing the same SSID name across locations, confirm whether the underlying security configuration is actually identical — if not, this can cause repeated authentication failures that look like a random connectivity issue.
5. After cleanup, have the user forget and freshly rejoin the correct current network to establish a clean profile.

## Escalation
If multiple offices are configured with the same SSID but inconsistent security settings, flag to Network team — standardizing this prevents recurring roaming/profile conflicts for traveling employees.

## SLA
P4 (single user) — target resolution 1 business day.
