# SOP: MFA Registration Failures (New Device / Re-registration)

## Issue
User cannot complete MFA registration on a new phone, gets stuck on the Microsoft Authenticator QR scan step, or registration succeeds but codes don't work. This is distinct from SOP "Password Reset & Account Lockout" — here the password is correct, MFA setup itself is the blocker.

## Common Causes
1. Device clock out of sync (TOTP codes are time-based — even 60 seconds of drift breaks them)
2. User scanning the QR code with the wrong app (camera app instead of Authenticator)
3. Old MFA registration wasn't removed before attempting a new one, causing a conflict
4. Conditional Access policy blocking registration from an unmanaged/unenrolled device
5. Company portal enrollment not completed, so the device isn't recognized as compliant

## Resolution Steps
1. Confirm the user is opening the registration link from `myaccount.microsoft.com > Security info`, not a stale email link.
2. Have the user check their phone's date/time is set to automatic (not manual) — this fixes the majority of "code invalid" issues.
3. If re-registering, go to Entra ID admin center > User > Authentication methods, and remove the old Authenticator method first to avoid a conflict.
4. Confirm the registration attempt isn't being blocked by Conditional Access — check Sign-in Logs for a "registration blocked" entry tied to device compliance state.
5. If the device needs to be enrolled first, walk the user through Company Portal enrollment before retrying MFA registration.
6. As a last resort, generate a Temporary Access Pass (TAP) in Entra ID valid for a short window so the user can register without needing existing MFA.

## Escalation
If Conditional Access is blocking legitimate registration attempts tenant-wide, escalate to Identity/Security team — do not disable Conditional Access policies at the ticket level.

## SLA
P3 (single user) — target resolution 2 business hours.
