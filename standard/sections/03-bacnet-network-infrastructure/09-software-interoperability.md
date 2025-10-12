# 3.9 Software Interoperability and Licensing

## Overview

True system openness requires both protocol-level interoperability and freedom from proprietary software licensing restrictions. This section establishes requirements to prevent vendor lock-in at the software and licensing level, ensuring long-term system maintainability and owner control.

## Requirements

### 3.9.1 Open Protocol Implementation

All integration platforms and supervisory systems shall use open, non-proprietary communication protocols:

- BACnet/IP (ASHRAE 135) as primary protocol
- Modbus TCP/IP for compatible devices
- SNMP for network equipment monitoring
- Standard IT protocols (HTTPS, REST API, MQTT) where appropriate
- Proprietary protocols are prohibited for device-to-supervisor or system-to-system communication

### 3.9.2 Network Integration Controller (NIC) Openness

For systems using Niagara Framework or similar integration platforms, the following shall be verified:

- **Open NIC Statement** provided by the contractor documenting that:
  - All programming and configuration is accessible via standard Niagara Workbench
  - No vendor-specific tools or dongles are required for system access
  - No encrypted or obfuscated program files that prevent editing
  - All graphics, logic, and configuration are fully editable by any qualified Niagara integrator

### 3.9.3 Software License Ownership

Software licensing shall ensure owner control and prevent lock-in:

- **Owner as Named License Holder:** All software licenses for supervisory systems, integration platforms, and graphical interfaces shall be registered to the building owner, not the contractor
- **License Transferability:** Licenses shall be transferable to any qualified service provider chosen by the owner
- **No Subscription Lock-in:** Ongoing subscription fees shall be for optional services only; core system operation shall not be dependent on active subscriptions
- **Source File Access:** Owner shall receive all source files, programs, graphics, and configuration databases

### 3.9.4 Third-Party Access

The system shall support unrestricted access by qualified third-party service providers:

- No vendor-specific passwords or access codes that cannot be shared with owner
- No license restrictions preventing third-party programming or modification
- Standard tools (Workbench, standard browsers, BACnet tools) sufficient for all system access
- No encrypted files or proprietary formats that prevent modification

### 3.9.5 Documentation of Interoperability

The contractor shall provide documentation demonstrating software-level openness:

- Software architecture diagram showing all communication paths and protocols
- Listing of all software licenses with owner as named holder
- Open NIC Statement (where applicable)
- Confirmation that no proprietary tools are required for system maintenance
- List of standard tools required for system programming and access

## Examples

### Example 1: Niagara Framework Open NIC Validation

**Scenario:** A BAS using Tridium Niagara as the supervisory platform.

**Open NIC Statement Verification:**
- Contractor provides written statement confirming no encrypted program files
- All graphics created in standard Niagara PX or AX editors
- No vendor-specific modules or extensions that prevent third-party access
- Logic programs are standard .bog files, fully editable
- Owner receives Workbench licenses in their name
- Any integrator with standard Niagara Workbench can access system

**Result:** Owner can hire any qualified Niagara integrator for future service without contractor involvement.

### Example 2: License Ownership Verification

**Scenario:** Validation that software licenses are properly registered to the owner.

**Verification Process:**
1. Obtain copy of all software license agreements
2. Verify owner organization is named licensee
3. Confirm licenses are perpetual or clearly documented subscription terms
4. Validate license allows third-party service providers
5. Ensure owner receives all license keys and activation codes
6. Document all software version numbers and support terms

**Result:** Owner has direct relationship with software vendors; can maintain licenses independent of contractor.

### Example 3: Protocol-Only Interoperability (Insufficient)

**Scenario:** A system using BACnet/IP but with proprietary licensing restrictions.

**Issue Identified:**
- All devices communicate via open BACnet/IP protocol ✓
- Supervisory software requires annual subscription to vendor for system access ✗
- Programming tools are vendor-specific and cannot be purchased by owner ✗
- Graphics are in proprietary encrypted format ✗

**Corrective Action:**
- Require contractor to provide open-licensed supervisory software
- Owner receives perpetual licenses in their name
- All graphics converted to standard formats
- Subscription for support only, not for access

**Result:** Protocol openness combined with software/licensing openness prevents lock-in.

## Verification

### Open Protocol Validation

- **Objective:** Verify all system communications use open, standard protocols
- **Method:**
  - Review network architecture for protocol usage
  - Confirm BACnet/IP as primary protocol
  - Identify any proprietary protocol usage
  - Validate standard IT protocols for supervisory access
- **Acceptance Criteria:** Zero use of proprietary protocols for device communication or supervisory access

### NIC Openness Verification

- **Objective:** Verify integration platform is accessible to any qualified integrator
- **Method:**
  - Obtain Open NIC Statement from contractor
  - Verify no encrypted or obfuscated program files
  - Confirm standard tools (Workbench) sufficient for all access
  - Test that programming is editable without vendor-specific tools
  - Validate no vendor-specific extensions prevent third-party access
- **Acceptance Criteria:** Complete Open NIC Statement provided; all files editable with standard tools

### License Ownership Audit

- **Objective:** Verify owner is the named holder of all software licenses
- **Method:**
  - Review all software license agreements
  - Verify owner organization is named licensee
  - Confirm license terms allow third-party service
  - Validate owner has received all license keys
  - Check that no subscription is required for basic system operation
- **Acceptance Criteria:** 100% of licenses registered to owner; no restrictions on third-party service

### Third-Party Access Testing

- **Objective:** Verify unrestricted access for qualified third-party service providers
- **Method:**
  - Document all tools required for system access
  - Confirm no vendor-specific passwords or dongles
  - Validate standard tools are sufficient
  - Test access using generic credentials and standard tools
- **Acceptance Criteria:** Full system access achievable with standard industry tools; no vendor-specific access restrictions

### Required Deliverables

- [ ] Software architecture diagram with protocols documented
- [ ] Open NIC Statement (for Niagara or similar platforms)
- [ ] All software license agreements with owner as named holder
- [ ] Complete list of tools required for system access and maintenance
- [ ] All source files, programs, graphics, and databases
- [ ] Written confirmation of no proprietary access restrictions
- [ ] License key inventory and registration documentation

### Acceptance Criteria

Software interoperability requirements are met when all communications use open protocols, integration platforms are confirmed as open via NIC statements, all software licenses are held by the owner, and third-party access is unrestricted by proprietary tools or licensing.

---

*This document is part of the Digital Commissioning of Building Automation Systems Standard, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
