# 3.3 BACnet Network Numbering

Each BACnet network segment (both IP and MS/TP) shall be assigned a unique BACnet Network Number. Duplicate network numbers are not permitted.

Network numbers shall be allocated logically, following a documented scheme (e.g., 1xx for IP backbone, 2xx for Floor 2 MS/TP networks, etc.).

The contractor shall submit a schedule of all BACnet Network Numbers used in the project.

## Verification
#### BACnet Routing Table
- **Network Number Assignment**: Verify unique BACnet network numbers for each routed segment
- **Routing Table Entries**: Confirm all downstream networks are properly advertised
- **Network Reachability**: Test that devices on different network segments can communicate
- **BBMD Configuration**: If applicable, verify Broadcast Distribution Table entries

---

*This document is part of the Digital Commissioning of Building Automation Systems Standard, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
