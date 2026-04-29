# 3.4 BACnet Device Instance Numbers (Device IDs)

Every BACnet device on the internetwork shall have a globally unique Device Instance Number. Duplicate Device IDs are not permitted.

Device IDs shall follow a structured, documented scheme that allows for easy identification of the device.

**Example Scheme:** `<Site Code><Equipment Type Code><Sequential Number>`

**Example ID:** `102501` (Site 10, AHU Type 25, Instance 01)

Device IDs shall not be re-used, even if a device is decommissioned. A previously assigned Device Instance Number may remain in service only when a failed device is replaced on a like-for-like basis and the replacement assumes the same documented device identity.

The contractor shall submit a complete schedule of all Device Instance Numbers.

## Verification

#### Device Instance Verification
- **Global Uniqueness**: Verify that no duplicate Device Instance Numbers exist on the internetwork
- **Scheme Consistency**: Confirm Device Instance Numbers follow the documented project numbering scheme
- **Schedule Completeness**: Verify the submitted Device Instance schedule includes all commissioned BACnet devices
- **Replacement Traceability**: Where a failed device was replaced like-for-like, confirm the retained Device Instance Number is documented in turnover records

---

*This document is part of the Digital Commissioning of Building Automation Systems Standard, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
