# 3.2 IP Addressing Validation

## 3.2.1 Validation Requirements

### IP Address Assignment Validation
The IP addressing implementation must be validated against the project-specific addressing scheme and network design requirements.

**Required Deliverable**: Complete IP Address Schedule documenting all BAS devices with their assigned IP addresses, subnet assignments, and addressing method (static or DHCP reservation).

### Subnet Configuration Validation
Network subnet implementation must be verified for:

- Compliance with documented subnet design
- Adequate address space for current and planned devices
- Proper subnet isolation and VLAN configuration
- Coordination with facility IT infrastructure

## 3.2.2 Validation Criteria Examples

The following examples illustrate validation criteria that would be applied based on project-specific requirements:

### Address Assignment Validation

- **Static IP Verification**: Confirm devices configured with static IP addresses match the IP Address Schedule
- **DHCP Reservation Verification**: Verify MAC-address-based DHCP reservations are properly configured and functional
- **Dynamic Address Prohibition**: Confirm no devices are using randomly assigned or dynamic DHCP addresses

### Subnet Capacity Validation  
Examples of subnet capacity validation against project requirements:

- **Subnet A Example**: 10.100.10.0/24 (253 usable addresses) - verify device count does not exceed capacity threshold per project requirements
- **Subnet B Example**: 10.100.11.0/26 (61 usable addresses) - validate current device count against design capacity
- **Subnet C Example**: 10.100.11.64/28 (13 usable addresses) - confirm subnet size meets minimum requirements or has documented exception

## 3.2.3 Verification Procedures

### IP Address Schedule Verification Method
1. **Documentation Completeness Check**

    - **Objective**: Verify IP Address Schedule includes all BAS devices
    - **Method**: Cross-reference schedule against network discovery results
    - **Acceptance Criteria**: 100% of discovered devices are documented in schedule

2. **Address Assignment Verification**

    - **Objective**: Confirm devices are configured per the documented addressing scheme
    - **Method**: Network scanning to verify actual IP configurations match schedule
    - **Acceptance Criteria**: 100% correlation between documented and actual IP assignments

### Network Configuration Testing Method
1. **Subnet Verification**

    - **Objective**: Validate subnet configuration and device placement
    - **Method**: Network topology discovery and subnet boundary testing
    - **Acceptance Criteria**: All devices are on correct subnets with proper network masks and gateways

2. **VLAN Configuration Testing** (If Applicable)

    - **Objective**: Verify VLAN tagging and membership
    - **Method**: VLAN discovery and traffic flow analysis
    - **Acceptance Criteria**: All BAS devices are on designated VLANs with proper isolation from other networks

3. **Connectivity Validation**

    - **Objective**: Confirm all devices can communicate as required by system design
    - **Method**: Automated ping testing and BACnet communication verification
    - **Acceptance Criteria**: 100% of devices respond to network communication tests

---

*This document is part of the Digital Commissioning of Building Automation Systems Standard, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
