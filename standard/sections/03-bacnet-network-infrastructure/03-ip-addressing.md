# 3.2 IP Addressing

All BACnet/IP devices, including supervisory controllers, routers, and servers, shall be assigned a static IP address or utilize DHCP with a MAC-based reservation. Randomly assigned or dynamic DHCP addresses are not permitted for devices.

All BAS network devices shall reside on a dedicated and isolated LAN or VLAN, coordinated with the Owner's IT department.

Subnets in use will be clearly documented, with all subnets identified with their CIDR notation, and a gateway address.
Each subnet shall have the greater of 10 available client IP addresses or 25% of the total assignable range of the subnet.
Subnets smaller than 0.0.0.0/28 must have written exceptions to be acceptable.
### Examples:
- **Subnet A** is 10.100.10.0/24 with Gateway 10.100.10.254, giving us 253 usable addresses. This subnet shall not have more than 189 devices at commissioning.
- **Subnet B** is 10.100.11.0/26 with Gateway 10.100.11.62, giving us 61 usable addresses. This subnet shall not have more than 46 devices at commissioning.
- **Subnet C** is 10.100.11.64/28 with Gateway 10.100.11.78, giving us 13 usable addresses. This subnet shall not have more than 3 devices at commissioning.

The Controls Contractor shall complete and submit a full IP Address Schedule for all devices as a commissioning deliverable.
### Verification
#### Network Configuration
- **IP Address Assignment**: Verify router has correct static IP address or DHCP reservation
- **Subnet Configuration**: Confirm router is on correct network segment with proper subnet mask
- **Default Gateway**: Verify correct default gateway configuration for routing between networks
- **VLAN Configuration**: If applicable, confirm proper VLAN tagging and membership

---

*This document is part of the Digital Commissioning of Building Automation Systems Standard, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
