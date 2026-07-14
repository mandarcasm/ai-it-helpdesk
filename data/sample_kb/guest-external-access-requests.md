# SOP: Guest / External User Access Requests

## Issue
An internal user requests access for an external partner, vendor, or contractor (e.g. to a Teams channel, SharePoint site, or shared mailbox). This is a provisioning request, not a lockout or password issue — handle under Access Management, not Incident.

## Resolution Steps
1. Confirm the requesting internal user is the resource owner or has manager/data-owner approval attached to the ticket — do not provision guest access on a bare request with no approval trail.
2. In Entra ID admin center > External Identities > Guest users, invite the external email address. Guest accounts use B2B collaboration and do not consume a standard license.
3. Set the guest's access scope to only the specific resource requested (Teams channel, SharePoint library, etc.) — do not add guests to broad security groups "to be safe."
4. Guest accounts should have an expiration reviewed at 90 days by default unless the ticket specifies an ongoing engagement — set a calendar reminder or use Entra ID Access Reviews if configured.
5. Confirm the guest completes the invitation redemption (they'll get an email to accept) before closing the ticket — an unredeemed invite means they still have no access.
6. Verify Conditional Access policies for guests aren't blocking sign-in from their organization (some tenants restrict guest MFA methods).

## Common Follow-up Issues
- Guest reports they can see the Teams channel but not attached files — usually a SharePoint permission that didn't inherit correctly; check the site's guest sharing settings.
- Guest's invite email lands in their spam folder — provide the direct redemption link as a fallback.

## Escalation
Requests for guest access to sensitive resources (Finance, HR, Legal SharePoint sites) require Security team sign-off before provisioning — flag and hold the ticket rather than provisioning first and asking later.

## SLA
P4 (access request, not incident) — target resolution 1 business day.
