# SOP: Browser Slow, Crashing, or Extensions Blocked

## Issue
Web browser is slow, freezes, crashes frequently, or a needed extension is greyed out/blocked from installing.

## Common Causes
1. Too many open tabs/extensions consuming memory
2. Corrupted browser profile/cache
3. Extension blocked by a managed browser policy (common for security reasons — not a bug)
4. Outdated browser version no longer receiving performance/security patches

## Resolution Steps
1. Check installed extension count and open tab count first — high numbers of either are the most common cause of slowness, not a fault.
2. Clear browsing cache and cookies (not saved passwords/bookmarks) via browser Settings > Privacy.
3. If a specific extension won't install, check whether it's on the company's blocked extensions policy — this is deliberate for unapproved extensions, not a technical fault. Direct the user to request approval if it's genuinely needed for work.
4. Confirm the browser is on a current version — managed browsers usually auto-update, but check `chrome://settings/help` or equivalent if unsure.
5. As a last resort for persistent crashes, create a new browser profile and migrate bookmarks — isolates whether the old profile itself is corrupted.

## Escalation
Requests to approve a currently-blocked extension go through Security review, not a direct unblock — don't bypass policy at the ticket level.

## SLA
P4 (performance/slowness) — target resolution 1 business day.
P3 (business-critical extension blocked) — target resolution 4 business hours for review, pending Security sign-off.
