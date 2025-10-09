# 3.5 BACnet/IP Network Services

## BBMDs (BACnet/IP Broadcast Management Devices)

For networks spanning multiple IP subnets, a clear BBMD strategy is required. One primary and at least one backup BBMD shall be configured. The contractor must provide the Broadcast Distribution Table (BDT) for each BBMD.

The contractor shall also provide a BACnet data flow diagram illustrating the logical path of communications through routers and BBMDs during both normal operation and in documented failover scenarios.

## Foreign Device Registration

The use of Foreign Device Registration shall be minimized and approved by the Owner's Representative. It is not an acceptable substitute for a properly configured BBMD architecture.

## UDP Port

All BACnet/IP communications shall use the official IANA-registered UDP port 47808 (0xBAC0). Any deviation must be explicitly approved in writing.

---

*This document is part of the Digital Commissioning of Building Automation Systems Standard, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
