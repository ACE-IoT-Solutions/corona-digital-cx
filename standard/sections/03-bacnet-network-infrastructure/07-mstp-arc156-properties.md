# 3.6 BACnet MS/TP & ARC156 Network Properties

## MAC Addresses

Each device on a given MS/TP or ARC156 segment must have a unique MAC address. Addresses shall be assigned in contiguous blocks to simplify troubleshooting and device management as well as maintain performance.

## Baud Rate

The baud rate must be consistent across all devices on a single segment (e.g., 38400 or 76800 for MS/TP).

## Max Masters (MS/TP)

The Max-Info-Frames and Max-Master properties shall be configured correctly on all master devices to ensure stable token passing. The configuration for each trunk shall be documented as a project deliverable. The number of master devices on a single segment should not exceed 64.

## Validation and Verification
The greater of (3) or 10% of all fieldbus trunks must have their configurations verified. If the project includes multiple device models serving as fieldbus routers, at least one example of each device model must be included in the verification sample.

### MS/TP Network Verification

#### Data Link Layer Verification
- **MAC Address Uniqueness**: Scan all devices on trunk to verify no duplicate MAC addresses
- **MAC Address Range**: Confirm addresses are within 0-127 range and assigned in logical blocks
- **Baud Rate Consistency**: Verify all devices on trunk operate at same baud rate (typically 38400 or 76800)
- **Max-Master Configuration**: Check that Max-Master value accommodates all devices on trunk
- **Max-Info-Frames**: Verify appropriate Max-Info-Frames setting for network performance

#### Token Passing Verification
- **Token Passing Sequence**: Monitor network to confirm proper token circulation
- **Response Time**: Measure token rotation time under normal and peak load conditions
- **Error Recovery**: Verify network recovers properly from token loss scenarios

### ARC156 Network Verification Examples

#### Protocol Verification
- **ARC156 Compliance**: Confirm devices properly implement ARC156 protocol extensions
- **Interoperability**: Verify mixed-vendor device communication on same trunk
- **Configuration Consistency**: Check that all devices have compatible ARC156 settings
- **Diagnostics**: Verify that networks have no reconfigurations while devices in steady state for 24 hours.



---

*This document is part of the Digital Commissioning of Building Automation Systems Standard, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
