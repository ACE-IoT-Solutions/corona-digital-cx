# 3.10 BACnet/SC Security and PKI Ownership

## Overview

BACnet Secure Connect (BACnet/SC) provides secure, authenticated communication using Transport Layer Security (TLS) and a Public Key Infrastructure (PKI). To prevent vendor lock-in and ensure long-term system maintainability, the building owner must control the PKI and have unrestricted ability to provision certificates for any authorized device or service provider. Additionally, networks that route between BACnet/SC and traditional BACnet/IP or MS/TP must provide diagnostic access points for troubleshooting.

## Requirements

### 3.10.1 PKI Ownership and Control

The building owner shall be the Certificate Authority (CA) or shall control the Certificate Authority for the BACnet/SC network:

- **Owner-Controlled CA:** The owner shall operate the Certificate Authority or designate a trusted third party to operate it on the owner's behalf (not the BAS contractor or vendor)
- **Root Certificate Ownership:** The owner shall hold the private key for the root certificate
- **No Vendor CA Dependency:** The system shall not depend on certificates issued by vendor-controlled or cloud-based CAs that restrict owner's provisioning ability
- **CA Documentation:** Complete CA setup documentation, including certificate issuance procedures, shall be provided to the owner

### 3.10.2 Certificate Provisioning Rights

The owner shall have unrestricted rights to provision certificates for BACnet/SC devices and participants:

- **Self-Provisioning Capability:** The owner shall be able to generate and sign certificates for new devices without vendor involvement
- **Third-Party Provisioning:** Any qualified service provider chosen by the owner shall be able to provision devices with owner-signed certificates
- **No License Restrictions:** Software licenses shall not restrict the owner's ability to issue certificates
- **Revocation Authority:** The owner shall have authority to revoke certificates for any device or participant

### 3.10.3 Certificate Management Tools

Certificate management tools shall be accessible to the owner:

- **Standard Tools:** Certificate generation and signing shall be achievable using standard PKI tools (OpenSSL, Microsoft CA, or open-source equivalents)
- **Vendor Tool Transfer:** If vendor-specific tools are used during installation, they shall be transferred to the owner with perpetual licenses
- **Documentation:** Complete procedures for certificate generation, signing, installation, and revocation shall be documented
- **No Proprietary Formats:** Certificates shall use standard formats (X.509) with no proprietary extensions that prevent third-party provisioning

### 3.10.4 Certificate Validation and Direct Trust Model

BACnet/SC uses a direct trust model where devices validate certificates against locally installed signing certificates. The following shall be verified:

- **Signing Certificate Trust:** All device certificates shall be signed by a certificate that chains to the owner's root CA
- **Two-Slot Trust Model:** BACnet/SC devices support two trusted signing certificate slots; the owner's signing certificate(s) shall be installed in these slots
- **No Chain Validation in Devices:** Individual devices do not verify full certificate chains; they only validate that certificates are signed by one of their two trusted signing certificates
- **Owner Signing Certificate Authority:** The signing certificate used to issue device certificates shall be controlled by the owner and chain to the owner's root CA
- **No External Trust Dependencies:** Devices shall not require trust of vendor CAs, public CAs, or any signing certificate not controlled by the owner
- **Certificate Expiration Policy:** Certificate lifetimes shall be documented; automated renewal procedures shall be implemented where supported
- **Expired Certificate Handling:** System behavior with expired certificates shall be documented and tested

### 3.10.5 BACnet/SC Hub and Router Configuration

BACnet/SC infrastructure components shall meet ownership requirements:

- **Hub Configuration Access:** BACnet/SC hubs shall be fully configurable by the owner using standard interfaces (web, CLI, BACnet services)
- **Router Ownership:** Devices that route between BACnet/SC and BACnet/IP or MS/TP shall be owned and controlled by the building owner (not locked to vendor cloud services)
- **Connection Authorization:** The owner shall control which devices and hubs can participate in the BACnet/SC network via certificate policy
- **No Cloud Lock-in:** Hub or router functionality shall not depend on vendor cloud services or external platforms

### 3.10.6 Diagnostic Access for Routed Networks

Where BACnet/SC networks route to traditional BACnet/IP or MS/TP networks, diagnostic access shall be provided:

- **Service Ports on Routers:** BACnet/SC to BACnet/IP routers shall provide a service port on the local BACnet/IP network segment for diagnostic packet capture
- **MS/TP Diagnostic Access:** BACnet/SC to MS/TP routers shall provide a method to capture MS/TP traffic (service port, mirror port, or tap connection)
- **Unencrypted Local Traffic:** Traffic on the local BACnet/IP or MS/TP side of routers shall remain unencrypted to allow standard diagnostic tools (Wireshark, VTS, etc.)
- **No Interference:** Diagnostic service ports shall not interfere with normal network operations or create security vulnerabilities

### 3.10.7 Third-Party Diagnostic Tool Compatibility

Network architecture shall support third-party diagnostic tools:

- **Packet Capture Support:** Network infrastructure shall allow packet capture on local network segments using standard tools (Wireshark, tcpdump)
- **BACnet Protocol Analysis:** Captured traffic shall be analyzable using standard BACnet protocol analyzers (VTS, YABE, etc.)
- **No Encryption of Local Traffic:** BACnet/IP and MS/TP networks that connect to BACnet/SC shall not encrypt local segment traffic
- **Documentation of Capture Points:** Network diagrams shall identify all available diagnostic capture points

## Examples

### Example 1: Owner-Operated Certificate Authority

**Scenario:** Building owner establishes local CA for BACnet/SC network.

**Implementation:**
- Owner installs Microsoft Active Directory Certificate Services on local server
- Root CA certificate generated and secured by owner IT department
- BAS contractor receives subordinate CA certificate for device provisioning during installation
- After project completion, owner IT assumes all certificate provisioning responsibilities
- Any future service provider can request subordinate CA cert from owner to provision new devices

**Validation:**
1. Verify owner holds root CA private key
2. Confirm contractor used owner's CA for all device certificates
3. Test certificate provisioning using owner's tools (no vendor software required)
4. Validate any qualified integrator can obtain subordinate cert from owner
5. Test certificate revocation by owner

**Result:** Owner has complete control of PKI; no vendor dependency for future device additions.

### Example 2: Certificate Provisioning Testing with Direct Trust Model

**Scenario:** Validation that new devices can be provisioned without vendor involvement using BACnet/SC's two-slot direct trust model.

**Trust Architecture:**
- Owner operates root CA (secured, offline)
- Owner creates subordinate "Device Signing CA" that chains to root
- Device Signing CA certificate installed in both trust slots on all BACnet/SC devices
- Individual device certificates signed by Device Signing CA

**Test Procedure:**
1. Obtain new BACnet/SC device (controller, hub, etc.)
2. Install owner's Device Signing CA certificate in device's two trust slots (typically via web interface or provisioning tool)
3. Using owner's CA tools, generate certificate request for new device
4. Sign device certificate using owner's Device Signing CA (no vendor tools)
5. Install device certificate on device using standard methods (web interface, BACnet service, USB)
6. Verify device connects to BACnet/SC network and communicates
7. Confirm device validates peer certificates signed by the same Device Signing CA
8. Validate device appears in network roster and is fully functional

**Acceptance:**
- Trust slots contain only owner-controlled signing certificates ✓
- Device certificate generated using standard tools (OpenSSL, Microsoft CA) ✓
- No vendor-specific software required for signing ✓
- Certificate installation achievable via standard interfaces ✓
- Device validates peers using owner's signing certificate ✓
- Device fully operational with owner-issued certificate ✓

**Result:** Owner can add devices at will using direct trust model; no vendor lock-in for certificate provisioning.

### Example 3: Diagnostic Access Validation for Routed Networks

**Scenario:** BACnet/SC network with router to existing BACnet/IP building network.

**Configuration:**
- BACnet/SC hub connects to secure WAN
- Router bridges BACnet/SC to local BACnet/IP network (192.168.10.0/24)
- Router provides service port on BACnet/IP side for diagnostics

**Validation:**
1. Connect laptop to BACnet/IP service port on router
2. Launch Wireshark and capture BACnet/IP traffic
3. Verify unencrypted BACnet packets are visible and decodable
4. Use VTS to discover devices on local BACnet/IP network
5. Confirm diagnostic access does not interfere with normal operations
6. Verify BACnet/SC traffic remains encrypted on WAN side

**Network Diagram:**
```
[BACnet/IP Devices] ←→ [Service Port] ←→ [BACnet/SC Router] ←→ [Encrypted WAN]
                              ↓
                     [Diagnostic Laptop]
                     (Wireshark/VTS)
```

**Result:** Technicians can troubleshoot local network using standard tools; BACnet/SC security maintained.

### Example 4: MS/TP to BACnet/SC Router Diagnostics

**Scenario:** Legacy MS/TP field controllers routed to BACnet/SC infrastructure.

**Implementation:**
- MS/TP network at 76.8 kbps on RS-485 bus
- Router provides diagnostic tap or mirror port for MS/TP traffic
- Local diagnostics use MS/TP sniffer or USB interface

**Diagnostic Options:**
- **Option 1:** Router provides USB port for MS/TP traffic capture
- **Option 2:** Router includes physical tap points on MS/TP terminals
- **Option 3:** Router mirrors MS/TP traffic to Ethernet service port (encapsulated)

**Validation:**
1. Connect MS/TP diagnostic tool to router's diagnostic interface
2. Capture MS/TP token passing and data frames
3. Verify MS/TP addressing and timing is correct
4. Troubleshoot any field controller communication issues
5. Confirm diagnostic connection does not load MS/TP network or cause errors

**Result:** MS/TP troubleshooting possible using standard tools; BACnet/SC security unaffected.

## Verification

### PKI Ownership Validation

- **Objective:** Verify owner controls the Certificate Authority and can provision certificates independently
- **Method:**
  - Verify owner holds root CA private key
  - Confirm no dependency on vendor or cloud-based CAs
  - Review certificate issuance procedures documentation
  - Test that owner can generate and sign certificates using standard tools
  - Validate third-party service providers can obtain subordinate certificates from owner
- **Acceptance Criteria:** Owner operates or controls CA; no vendor CA dependencies; certificate provisioning possible with standard tools

### Certificate Provisioning Testing

- **Objective:** Verify unrestricted certificate provisioning capability
- **Method:**
  - Obtain test device and provision certificate using owner's CA and tools
  - Verify no vendor-specific software required
  - Test certificate installation via standard methods
  - Validate device operates normally with owner-issued certificate
  - Test certificate revocation by owner
- **Acceptance Criteria:** Successful device provisioning without vendor involvement; revocation authority confirmed

### Direct Trust Model Validation

- **Objective:** Verify BACnet/SC direct trust model is correctly implemented with owner-controlled signing certificates
- **Method:**
  - Verify owner's Device Signing CA certificate is installed in both trust slots on all devices
  - Confirm Device Signing CA chains to owner's root CA (validated out-of-band, not by devices)
  - Inspect all device certificates and verify they are signed by owner's Device Signing CA
  - Confirm devices do not trust vendor signing certificates or external CAs
  - Test that devices accept peers with certificates signed by owner's Device Signing CA
  - Test that devices reject peers with certificates from untrusted signing CAs
  - Validate certificate renewal procedures
  - Test system behavior with expired certificates
- **Acceptance Criteria:** All devices trust only owner-controlled signing certificates; device certificates signed by owner's CA; no vendor or external CA dependencies; peer validation functions correctly; expiration handling documented

### BACnet/SC Infrastructure Control

- **Objective:** Verify owner controls hubs and routers
- **Method:**
  - Access hub and router configuration interfaces
  - Verify owner credentials provide full administrative access
  - Confirm no cloud service dependencies for core functionality
  - Test connection authorization controls
- **Acceptance Criteria:** Full administrative access to all BACnet/SC infrastructure; no cloud lock-in

### Diagnostic Access Verification for Routed Networks

- **Objective:** Verify diagnostic access is available on routed networks
- **Method:**
  - Identify all BACnet/SC to BACnet/IP routers and verify service port availability
  - Identify all BACnet/SC to MS/TP routers and verify diagnostic access method
  - Connect diagnostic tools to service ports
  - Capture and analyze traffic using standard tools (Wireshark, VTS)
  - Verify diagnostic access does not interfere with operations
- **Acceptance Criteria:** Service ports available on all routers; packet capture successful; traffic analyzable with standard tools; no operational interference

### Third-Party Tool Compatibility

- **Objective:** Verify standard diagnostic tools can analyze network traffic
- **Method:**
  - Capture packets on local BACnet/IP segments using Wireshark
  - Analyze BACnet protocol using VTS or YABE
  - Verify MS/TP traffic is accessible and analyzable
  - Confirm traffic is unencrypted on local segments
  - Document all diagnostic capture points on network diagrams
- **Acceptance Criteria:** Standard tools successfully capture and analyze traffic; all diagnostic points documented

### Required Deliverables

- [ ] Certificate Authority setup documentation with owner as operator
- [ ] Root certificate and private key secured by owner
- [ ] Certificate issuance and revocation procedures
- [ ] Trust chain verification for all device certificates
- [ ] BACnet/SC hub and router configuration documentation
- [ ] Network diagrams showing diagnostic service ports and capture points
- [ ] Third-party certificate provisioning test results
- [ ] Diagnostic access validation test results
- [ ] Certificate management tool documentation and licenses

### Acceptance Criteria

BACnet/SC security and PKI ownership requirements are met when the owner controls the Certificate Authority, can provision certificates independently using standard tools, has unrestricted revocation authority, controls all BACnet/SC infrastructure, and diagnostic access is available on all routed networks for third-party troubleshooting tools.

---

*This document is part of the Digital Commissioning of Building Automation Systems Standard, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
