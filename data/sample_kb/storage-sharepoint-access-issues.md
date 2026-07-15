# SOP: SharePoint Access or Permission Issues

## Issue
User can't access a SharePoint site, sees "Access Denied," or can view a site but not specific document libraries or files within it.

## Common Causes
1. User was never granted access to the specific site (different from their organization's general SharePoint access)
2. Permission granted at the wrong level — site access doesn't always cascade to every library if unique permissions are set on a subfolder
3. User is trying to access via an outdated bookmarked link after the site was migrated/restructured
4. Sharing link expired or was set to a specific person and forwarded to someone else

## Resolution Steps
1. Confirm exactly what the user is trying to access — the top-level site, a specific document library, or a single file — permission issues can exist at any of these levels independently.
2. Check the site's permission settings (site owner or SharePoint admin can verify) to confirm the user isn't already supposed to have access before granting anything new.
3. If access is legitimately needed, request it through the site owner — IT typically doesn't own SharePoint site permissions directly except for platform-level issues.
4. For "file not found" type errors on a previously-working link, check whether the site was migrated or restructured — provide the current correct link rather than troubleshooting the old one.
5. If a sharing link was set to a specific person and forwarded, the recipient needs their own access granted — a forwarded restricted link won't work for someone else.

## Escalation
Requests for access to sensitive SharePoint sites (Finance, HR, Legal) require the site owner's explicit approval — don't grant access as a general SharePoint admin action without that sign-off.

## SLA
P4 (access request) — target resolution 1 business day.
