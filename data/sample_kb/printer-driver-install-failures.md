# SOP: Printer Driver Installation Failures

## Issue
Printer driver fails to install, installs but printer shows an error state, or "Access Denied" appears during install. This is distinct from SOP "Network Printer Not Responding" — here the printer is reachable but the driver itself won't set up correctly.

## Common Causes
1. User lacks local admin rights to install drivers (standard for most managed endpoints)
2. Driver package architecture mismatch (32-bit driver on a 64-bit OS or vice versa)
3. Print Spooler service corrupted from a previous failed install
4. Driver not yet approved/pushed through Intune, so Windows blocks the unsigned/unmanaged install

## Resolution Steps
1. Confirm whether the user attempted a manual install (likely to fail without admin rights) vs. requesting it through the Company Portal / Software Center, which is the supported path.
2. If manual install is required for a one-off, use Intune's "Run as System" remote install capability rather than granting local admin.
3. Check Devices > Printers & Scanners for a driver stuck in "Installing" or error state — remove it fully, restart the Print Spooler service, then retry.
4. Confirm the correct driver architecture matches the OS (`Settings > System > About` shows System type).
5. If using a print server (not direct IP), confirm the print server's driver package is current — outdated server-side drivers cause client install failures tenant-wide.

## Escalation
If the driver package itself is failing validation (not a permissions issue), escalate to Endpoint Engineering to review and repackage the driver for Intune deployment.

## SLA
P3 (single user) — target resolution 4 business hours.
