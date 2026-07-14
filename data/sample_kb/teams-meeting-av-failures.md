# SOP: Teams Meeting Audio / Video / Screen Share Failures

## Issue
User can join Teams meetings but others can't hear them, their camera doesn't show, or screen share shows a black screen to other participants. This is an in-meeting media issue, distinct from SOP "Outlook & Teams Sync / Login Issues" which covers sign-in and sync problems.

## Common Causes
1. Wrong microphone/camera selected in Teams device settings (common after plugging in a new headset or docking station)
2. Windows privacy settings blocking Teams from accessing camera/microphone at the OS level
3. Screen share black screen typically caused by GPU hardware acceleration conflicts, especially on docked laptops with external monitors
4. Conflicting app (another video app, or a second Teams instance) holding exclusive access to the camera
5. Outdated or corrupt audio/video drivers after a recent Windows Update

## Resolution Steps
1. In Teams, go to Settings > Devices and confirm the correct microphone, speaker, and camera are selected — this alone resolves the majority of "can't hear me" tickets.
2. Check Windows Settings > Privacy & Security > Camera/Microphone — confirm "Let apps access your camera/microphone" is on, and Teams specifically is allowed.
3. For screen share black screen: in Teams, go to Settings > General and toggle off "GPU hardware acceleration," restart Teams, retry the share.
4. Confirm no other application (Zoom, OBS, another browser tab with camera access) is running and holding the camera device.
5. If the issue is isolated to a docking station setup, test directly on the laptop's built-in camera/mic to isolate whether the dock's USB hub is the actual fault.
6. Update audio/video drivers via Windows Update or Intune-managed driver package if consistently reproducible on a specific device model.

## Escalation
If multiple users report screen share failures simultaneously across different devices, check Microsoft 365 Service Health first — this may be a Teams service issue, not local.

## SLA
P3 (single user) — target resolution 4 business hours.
