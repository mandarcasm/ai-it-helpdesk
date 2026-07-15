# SOP: Self-Service Password Reset (SSPR) Not Working

## Issue
User tries to reset their own password via the self-service portal but it fails, doesn't send a verification code, or says they're not enrolled.

## Common Causes
1. User was never registered for SSPR (no authentication methods configured)
2. Registered phone number or authenticator app is out of date (old phone, changed number)
3. Conditional Access policy blocking the SSPR flow from the user's current location/device
4. SSPR is enabled for MFA but the user only has one authentication method registered, which fails

## Resolution Steps
1. Check the user's registered authentication methods in Entra ID (Authentication methods blade) — confirm what's actually on file before assuming SSPR should just work.
2. If their registered phone number is outdated, this itself needs identity verification before updating — don't take a phone number change request at face value without verifying identity through another channel.
3. If SSPR shows "not enrolled," the user needs to complete enrollment at `aka.ms/mfasetup` first — this can't be skipped, it's a security requirement, not a technicality.
4. Check Sign-in Logs for the SSPR attempt if it's failing silently — a Conditional Access block will show explicitly there.
5. If all else fails and the user is fully locked out with no working authentication method, this requires manual identity verification and a manual reset by IT (see SOP "Password Reset & Account Lockout").

## Escalation
Patterns of SSPR failing for many users at once should be escalated to Identity team — may indicate a Conditional Access policy or SSPR configuration issue affecting the whole tenant, not individual accounts.

## SLA
P3 (single user) — target resolution 2 business hours.
