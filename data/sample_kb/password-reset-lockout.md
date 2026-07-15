# SOP: Password Reset & Account Lockout (Entra ID)

## Issue
User is locked out of their account or has forgotten their password.

## Resolution Steps
1. Verify user identity per company ID policy (employee ID + manager confirmation or video call for remote staff) before taking any action.
2. In Entra ID admin center, go to Users > select user > Reset Password.
3. Generate a temporary password and set "Require password change at next sign-in."
4. If the account shows as locked (not just password-forgotten), check Sign-in Logs for repeated failed attempts — this may indicate a credential-stuffing attempt rather than genuine user error. If failed attempts originate from unfamiliar geographic locations, escalate to Security before unlocking.
5. Confirm MFA is still correctly registered. If the user lost their MFA device, use "Require re-register MFA" rather than disabling MFA entirely.
6. Communicate the temporary password to the user through a verified channel only (not email, since email may be inaccessible if this is a full lockout).

## Common Follow-up Issues
- User's cached credentials in Outlook/Teams still show old password — instruct them to sign out of all Microsoft 365 apps and back in.
- Mapped network drives may fail until the machine is rebooted after a password change.

## Escalation
Repeated lockouts (3+ in a week) for the same user should be flagged to Security for a Conditional Access risk review.

## SLA
P3 (single user, workaround available) — target resolution 2 business hours.
