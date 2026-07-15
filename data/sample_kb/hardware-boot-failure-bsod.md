# SOP: Laptop Won't Boot / Blue Screen (BSOD)

## Issue
Laptop won't turn on, gets stuck on the manufacturer logo, or shows a Blue Screen of Death (BSOD) during startup or use.

## Common Causes
1. Recent driver update causing a hardware conflict
2. Corrupted system file after an interrupted Windows Update
3. Failing storage drive (especially if BSODs are recurring, not one-off)
4. Overheating causing an emergency shutdown that looks like a boot failure

## Resolution Steps
1. Note the exact BSOD error code if one appears (e.g. "IRQL_NOT_LESS_OR_EQUAL") — this narrows the cause significantly, don't skip recording it.
2. Attempt to boot into Safe Mode (hold Shift while clicking Restart, or interrupt boot 3 times to trigger Automatic Repair options). If Safe Mode works, the issue is software/driver-related, not hardware failure.
3. If a driver update coincided with the first BSOD, roll it back via Device Manager in Safe Mode.
4. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated Command Prompt in Safe Mode to repair corrupted system files.
5. If the laptop won't boot into Safe Mode either, or BSODs are recurring with different error codes, treat as probable hardware failure (commonly storage or RAM) — do not keep attempting software fixes.

## Escalation
Any suspected hardware failure (recurring BSODs, won't boot at all) should be escalated for a hardware diagnostic/replacement rather than repeated remote troubleshooting — don't let this sit as an open ticket for days.

## SLA
P2 (user fully blocked from work) — target resolution 4 business hours to diagnose; hardware replacement per asset management SLA.
