# 3.6 BACnet MS/TP & ARC156 Network Properties

## MAC Addresses

Each device on a given MS/TP or ARC156 segment must have a unique MAC address. Addresses shall be assigned in contiguous blocks to simplify troubleshooting and device management.

## Baud Rate

The baud rate must be consistent across all devices on a single segment (e.g., 38400 or 76800 for MS/TP).

## Max Masters (MS/TP)

The Max-Info-Frames and Max-Master properties shall be configured correctly on all master devices to ensure stable token passing. The configuration for each trunk shall be documented as a commissioning deliverable. The number of master devices on a single segment should not exceed 64.

---

*This document is part of the Digital Commissioning of Building Automation Systems Standard, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
