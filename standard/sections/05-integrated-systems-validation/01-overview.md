# 5.0 Integrated Systems Validation

## 5.1 Overview

Modern building automation systems do not operate in isolation. To achieve operational efficiency, occupant comfort, and energy performance goals, BAS networks routinely integrate with lighting control systems, utility metering infrastructure, and other building subsystems. This section establishes validation requirements for systems that exchange data with the BAS.

## 5.2 Scope of Integration Validation

This section addresses validation of systems that **interface and exchange data** with the building automation system, specifically:

- **Lighting Control Systems:** Where lighting integrates with BAS for scheduling, occupancy coordination, or daylight harvesting
- **Utility Metering:** Where electric, water, thermal, or gas metering data feeds into the BAS for monitoring, trending, or demand response
- **Data Accessibility:** Performance requirements for data access, visualization, and system responsiveness

### What This Section Does

- Validates that integration points between systems are correctly configured
- Verifies that data exchange between systems is functional and accurate
- Ensures integrated systems meet performance requirements for data access
- Confirms metadata for integrated points follows the same standards as native BAS points

### What This Section Does Not Do

- Prescribe which systems must be integrated (determined by project requirements)
- Define the operational requirements of the integrated systems themselves (e.g., lighting levels, meter accuracy)
- Replace the commissioning requirements for the integrated systems in their own specifications

## 5.3 Integration Validation Approach

Where integrated systems are present and exchange data with the BAS, validation shall verify:

1. **Data Connectivity:** Integration points are configured and communication is functional
2. **Data Accuracy:** Values exchanged between systems are accurate and update at required intervals
3. **Metadata Compliance:** Integrated points include proper naming, tagging, and semantic modeling per metadata validation levels
4. **Performance Requirements:** Data access and visualization meet specified performance criteria

## 5.4 Applicability

Integration validation requirements apply when:

- The project specifications require integration between BAS and other building systems
- Data from non-BAS systems is made available through the BAS supervisory interface
- Coordinated control sequences involve multiple systems (e.g., HVAC and lighting)
- Utility metering data is required to be trended or visualized in the BAS

Where no integration is specified or required, this section does not apply.

---

*This document is part of the Digital Commissioning of Building Automation Systems Standard, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
