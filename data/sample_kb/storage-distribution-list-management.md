# SOP: Distribution List / Security Group Management Request

## Issue
A request to create a new distribution list or security group, or to add/remove members from an existing one.

## Resolution Steps
1. Determine whether a distribution list (email-only) or a security group (also controls resource access) is actually needed — these are often confused, and using the wrong type creates access issues later.
2. Confirm who owns the request — for existing lists, only the list owner or their manager should be able to request membership changes, not any requester.
3. For new list/group creation, confirm the naming convention matches team standards and that an owner is explicitly assigned — an ownerless group becomes unmanageable within months.
4. For membership changes, verify the person being added/removed and their manager's awareness, especially for removals — unexpected removal from a list can look like an account problem to the affected user if not communicated.
5. For security groups tied to resource access (not just email), understand what access changes when someone joins or leaves — check what the group actually grants before making the change.

## Common Follow-up Issues
- Requester wants a dynamic membership rule (auto-add based on department/role) instead of manual management — this is supported in Entra ID but requires more careful rule-writing; don't set up a dynamic rule without testing it against existing members first.

## Escalation
Requests to create groups with access to sensitive systems require the relevant data/system owner's approval before creation.

## SLA
P4 (standard request) — target resolution 2 business days.
