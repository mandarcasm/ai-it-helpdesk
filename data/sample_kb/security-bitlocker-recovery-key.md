# SOP: BitLocker Recovery Key Request

## Issue
User's device shows a BitLocker recovery screen on startup, asking for a recovery key — usually triggered by a hardware change, firmware update, or boot configuration change.

## Resolution Steps
1. Verify the user's identity before providing any recovery key — this is a sensitive credential that unlocks encrypted data, treat it with the same care as a password reset.
2. Look up the device's BitLocker recovery key in Entra ID (Devices > [device] > BitLocker keys) or Intune, matched by the Recovery Key ID shown on the user's screen — always match the ID shown, don't provide a key for the wrong device.
3. Provide the recovery key through a verified channel only (phone call or verified chat, not email to an address that might also be compromised).
4. Once unlocked, investigate why the recovery prompt triggered — common causes are a recent BIOS/firmware update, a hardware change (new hard drive, docking change), or a failed Windows Update. This isn't just unlocking the device, it's understanding whether it'll happen again.
5. If this is a recurring issue on the same device, escalate for a deeper check of TPM configuration or firmware settings rather than repeatedly providing recovery keys.

## Escalation
If a device's recovery key is not found in Entra ID/Intune (missing key escrow), this is a Security/Compliance gap requiring immediate investigation — flag this specifically, it may mean the device wasn't properly enrolled.

## SLA
P2 (user fully blocked from device) — target resolution 1 business hour.
