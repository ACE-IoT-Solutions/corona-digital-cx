# 3.1 Network Architecture

The BAS network architecture shall consist of a BACnet/IP backbone for high-speed communication between supervisory controllers, servers, and workstations.

Field-level controllers shall be connected via BACnet MS/TP segments, which are integrated into the backbone via dedicated BACnet Routers.

"Flat" network architectures with all devices on a single broadcast domain are not permitted for projects with more than 50 devices.

The contractor shall submit a complete network architecture diagram showing all IP and MS/TP segments, routers, controllers, and server locations.

**Placeholder for Network Diagram Image/Link**

#### Performance and Reliability
- **Throughput Testing**: Measure data throughput between network segments
- **Latency Testing**: Verify acceptable response times for cross-network communication
- **Failover Testing**: If redundant routers exist, verify automatic failover functionality
- **Traffic Filtering**: Confirm appropriate broadcast filtering between network segments
---

*This document is part of the Digital Commissioning of Building Automation Systems Standard, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
