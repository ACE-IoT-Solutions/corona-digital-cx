# 2.5 Cybersecurity Validation

## Overview

Building automation systems constitute critical operational technology (OT) infrastructure that requires comprehensive cybersecurity measures. This section establishes validation requirements for cybersecurity controls to ensure BAS networks are protected against unauthorized access, data breaches, and operational disruptions.

## Requirements

### 2.5.1 User Account Management

User account policies shall be documented and verified. The following shall be validated:

- All default passwords have been changed on all devices and systems
- User accounts follow principle of least privilege
- Account naming conventions prevent identification of privilege levels
- Inactive accounts are disabled or removed
- Password length requirements meet current security standards (minimum 15 characters for user accounts, minimum 20 characters for administrative accounts)
- Multi-factor authentication is implemented for administrative access where supported

### 2.5.2 Network Encryption

Data encryption standards shall be verified for all network communications:

- TLS 1.2 or higher is enabled for all HTTPS communications
- TLS 1.3 is implemented where supported by devices
- Older encryption protocols (SSL, TLS 1.0, TLS 1.1) are disabled
- Certificate validity and trust chains are verified
- Encryption is enforced for all supervisory and management interfaces

### 2.5.3 Network Segmentation

Network architecture shall implement proper segmentation:

- BAS network is isolated from enterprise IT network
- VLANs or physical separation is used to segment OT traffic
- Firewall rules explicitly define allowed traffic between zones
- Remote access requires VPN connection to isolated management network
- Internet-facing systems are prohibited unless explicitly approved with compensating controls

### 2.5.4 Remote Access Controls

Remote access methods shall be validated:

- VPN is the only permitted method for remote access
- Direct internet exposure of BAS devices is prohibited
- VPN endpoints require multi-factor authentication
- Remote access sessions are logged and auditable
- Remote access accounts are individual (no shared credentials)

### 2.5.5 Backup and Recovery

System backup and disaster recovery procedures shall be documented and tested:

- Automated backup schedules are configured and operational
- Backup storage is segregated from production systems
- Backup integrity verification is performed regularly
- Disaster recovery procedures are documented
- Recovery Time Objective (RTO) and Recovery Point Objective (RPO) are defined
- Recovery procedures have been tested and validated

### 2.5.6 Audit Logging

Security event logging shall be enabled and validated:

- User authentication events (success and failure) are logged
- Administrative actions are logged with user attribution
- Network access attempts are logged
- Log retention meets organizational requirements (minimum 90 days)
- Logs are stored on separate system or exported regularly
- Log review procedures are documented

## Examples

### Example 1: User Account Validation

**Scenario:** Validation of user accounts on a BACnet/IP network with Niagara supervisory system.

**Validation Process:**
1. Inventory all user accounts across all systems (controllers, supervisory stations, network devices)
2. Verify no default accounts remain active (admin/admin, root/root, etc.)
3. Confirm password complexity meets requirements
4. Verify MFA enabled for all administrative accounts
5. Check for shared accounts or generic usernames (admin, user, operator)
6. Validate least-privilege implementation (operators cannot modify programs)

**Result:** 100% of accounts comply with security policy; no default credentials; MFA enforced.

### Example 2: Network Encryption Validation

**Scenario:** HTTPS/TLS validation for web-based BAS interfaces.

**Implementation:**
- Use SSL Labs or similar tool to scan all web interfaces
- Verify TLS 1.2 minimum, TLS 1.3 preferred
- Confirm no SSL or TLS 1.0/1.1 support
- Validate certificate chains and expiration dates
- Test that HTTP redirects to HTTPS
- Verify strong cipher suites only

**Result:** All interfaces achieve "A" rating; modern encryption enforced; legacy protocols disabled.

### Example 3: Backup and Recovery Testing

**Scenario:** Validation of backup procedures for BAS supervisory system.

**Test Procedure:**
1. Document current system state (graphics, programs, trends)
2. Verify automated backups are running on schedule
3. Perform test restore to separate system
4. Validate restored system matches documented state
5. Measure recovery time against RTO requirement
6. Document any gaps or failures

**Result:** Backup restoration successful in 45 minutes (meets 1-hour RTO); minor configuration gaps documented and corrected.

## Verification

### Security Policy Review

- **Objective:** Verify cybersecurity policies are documented and comprehensive
- **Method:** Review cybersecurity documentation for:
  - User account management policy
  - Network encryption standards
  - Network segmentation architecture
  - Remote access procedures
  - Backup and disaster recovery plan
  - Audit logging configuration
- **Acceptance Criteria:** All required policies documented with specific technical requirements

### Account Security Audit

- **Objective:** Verify user account controls are properly implemented
- **Method:**
  - Inventory all user accounts across all systems
  - Attempt login with known default credentials (should fail)
  - Verify password complexity enforcement
  - Validate MFA implementation for admin accounts
  - Check for inactive or unnecessary accounts
- **Acceptance Criteria:** Zero default credentials; 100% MFA on admin accounts; no policy violations

### Encryption Validation

- **Objective:** Verify encryption is properly configured and enforced
- **Method:**
  - Scan all HTTPS interfaces with SSL testing tools
  - Verify TLS version enforcement
  - Validate certificate integrity and trust chains
  - Attempt connection with legacy protocols (should fail)
- **Acceptance Criteria:** TLS 1.2 minimum on all interfaces; no weak ciphers; valid certificates

### Network Segmentation Testing

- **Objective:** Verify network isolation and segmentation controls
- **Method:**
  - Review firewall rules and VLAN configuration
  - Attempt unauthorized cross-zone access (should be blocked)
  - Verify BAS network isolation from IT network
  - Test remote access requires VPN
- **Acceptance Criteria:** All unauthorized access blocked; VPN required for remote access; proper segmentation verified

### Backup and Recovery Validation

- **Objective:** Verify backup systems are operational and recovery procedures work
- **Method:**
  - Verify automated backups running on schedule
  - Perform test restoration to alternate system
  - Measure recovery time against RTO
  - Validate restored system functionality
- **Acceptance Criteria:** Successful restoration within RTO; full functionality verified; procedures documented

### Required Deliverables

- [ ] Cybersecurity policy document
- [ ] User account inventory and access matrix
- [ ] Network segmentation diagram with firewall rules
- [ ] Encryption configuration documentation
- [ ] Remote access procedures and VPN configuration
- [ ] Backup schedule and disaster recovery plan
- [ ] Audit logging configuration and retention policy
- [ ] Security validation test results

### Acceptance Criteria

Cybersecurity validation is complete when all security policies are documented, technical controls are verified through testing, backup and recovery procedures are validated, and all findings are documented with corrective actions implemented.

---

*This document is part of the Digital Commissioning of Building Automation Systems Standard, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
