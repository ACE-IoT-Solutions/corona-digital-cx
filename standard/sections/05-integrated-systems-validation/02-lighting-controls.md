# 5.2 Lighting Controls Integration

## Overview

Lighting control systems often integrate with BAS for coordinated scheduling, occupancy-based control, and energy management. This section establishes validation requirements for lighting control system integration points where lighting data is exchanged with or made available through the BAS.

## Requirements

### 5.2.1 Integration Scope Documentation

Where lighting controls integrate with the BAS, the following shall be documented:

- List of all lighting control points exposed to the BAS (zones, loads, occupancy sensors, daylight sensors, schedules)
- Communication protocol used for integration (BACnet, Modbus, proprietary API, etc.)
- Integration architecture diagram showing connection between lighting and BAS networks
- Intended use of lighting data in BAS (monitoring only, coordinated control, scheduling, energy analytics)

### 5.2.2 Data Connectivity Validation

Communication between lighting and BAS systems shall be verified:

- All specified lighting control points are visible and accessible from BAS supervisory station
- Data updates at specified refresh rate (typically 1-5 seconds for status, 30-60 seconds for energy data)
- Communication failures or errors are logged and reported
- Network addressing for lighting controllers follows project IP addressing scheme

### 5.2.3 Lighting Point Accuracy

Lighting control data accuracy shall be validated:

- Lighting zone status (on/off, dimming level) matches actual field conditions
- Occupancy sensor states accurately reflect space occupancy
- Daylight sensor values correlate with measured light levels
- Energy/power consumption data is within ±5% of independent measurement
- Scheduled events execute at correct times and affect correct zones

### 5.2.4 Coordinated Control Sequences

Where BAS and lighting systems execute coordinated control, validation shall verify:

- Occupancy-based HVAC setback triggers when lighting confirms space unoccupied
- Daylight harvesting adjustments coordinate with perimeter HVAC zoning
- After-hours HVAC requests properly enable associated lighting zones
- Coordinated shutdowns execute in proper sequence (lighting confirmation before HVAC setback)

### 5.2.5 Metadata Compliance

Lighting control points integrated into the BAS shall comply with metadata validation requirements:

- **Level 1 (Naming):** Lighting point names follow the same naming convention as native BAS points
- **Level 2 (Tagging):** Lighting equipment and points include appropriate tags (equip: Lighting, point: Switch, Sensor, etc.)
- **Level 3 (Semantic):** Lighting zones are properly related to served spaces in the semantic model

## Examples

### Example 1: Occupancy-Based HVAC Integration

**Scenario:** Office spaces with lighting occupancy sensors that trigger HVAC setback.

**Integration Configuration:**
- Lighting occupancy sensors communicate via BACnet to lighting panel
- Lighting panel exposes aggregated zone occupancy to BAS via BACnet/IP
- BAS logic monitors occupancy status and implements 30-minute setback delay
- If occupancy=false for 30 minutes, HVAC setpoint setback initiated

**Validation:**
- Simulate occupancy (motion in space) → verify sensor status changes to occupied
- Verify BAS receives occupied status within 5 seconds
- Simulate vacancy → verify 30-minute timer starts correctly
- Confirm HVAC setback occurs only after timer expires
- Test re-occupancy cancels setback timer

**Result:** Coordinated sequence reduces energy use while maintaining comfort; proper integration validated.

### Example 2: Lighting Load Monitoring

**Scenario:** BAS trending lighting energy consumption by floor.

**Implementation:**
- Lighting panels provide kW data via Modbus TCP
- BAS polls Modbus registers every 60 seconds
- Lighting loads tagged with floor designation
- BAS trends and displays energy by floor

**Validation:**
1. Use temporary power meter to measure lighting panel output
2. Compare BAS-displayed kW value to measured value (should be within ±5%)
3. Verify trending intervals are 60 seconds as specified
4. Confirm floor designation tagging is correct
5. Validate historical trend data accumulates properly

**Result:** Accurate lighting energy data enables load profiling and anomaly detection.

### Example 3: Daylight Harvesting Coordination

**Scenario:** Perimeter zones with daylight harvesting affecting HVAC load.

**Integration:**
- Daylight sensors in lighting system report lux levels to BAS
- BAS logic adjusts perimeter cooling anticipating reduced lighting heat gain
- Coordination prevents overcooling when lights dim

**Validation:**
- Verify daylight sensor values accessible in BAS
- Compare BAS lux reading to calibrated light meter (within ±10%)
- Simulate high daylight → confirm lights dim → verify HVAC cooling reduces
- Monitor space temperature to confirm comfort maintained
- Test cloudy condition → lights increase → HVAC cooling responds

**Result:** Coordinated control optimizes comfort and energy by accounting for dynamic lighting loads.

## Verification

### Integration Documentation Review

- **Objective:** Verify lighting integration is completely documented
- **Method:** Review integration documentation for:
  - Complete list of integrated lighting points
  - Communication protocol and architecture diagram
  - Network addressing compliance with project standards
  - Intended use cases for lighting data in BAS
- **Acceptance Criteria:** All integration points documented; architecture clearly defined

### Communication Validation

- **Objective:** Verify data connectivity between lighting and BAS systems
- **Method:**
  - Verify all lighting points are accessible from BAS supervisory station
  - Monitor data refresh rates (status, energy, sensors)
  - Simulate communication failure and verify error reporting
  - Check network addressing follows project scheme
- **Acceptance Criteria:** 100% of points accessible; refresh rates meet specification; errors are logged

### Data Accuracy Testing

- **Objective:** Verify lighting data values are accurate
- **Method:**
  - Compare lighting status in BAS to field observations
  - Verify occupancy sensor states with actual occupancy
  - Measure light levels and compare to BAS sensor values (±10%)
  - Validate energy data against independent metering (±5%)
  - Test scheduled events execute at correct times
- **Acceptance Criteria:** All data values within specified accuracy; schedules execute correctly

### Coordinated Sequence Testing

- **Objective:** Verify coordinated control between lighting and HVAC systems
- **Method:**
  - Test occupancy-based setback sequences (simulate occupied/vacant)
  - Verify daylight coordination sequences
  - Test after-hours lighting enable with HVAC request
  - Validate shutdown sequences execute in correct order
- **Acceptance Criteria:** All coordinated sequences function as designed; proper delays and interlocks verified

### Metadata Compliance Check

- **Objective:** Verify lighting points comply with metadata standards
- **Method:**
  - Validate naming convention compliance (Level 1)
  - Check tagging accuracy and completeness (Level 2)
  - Verify semantic relationships in model (Level 3)
- **Acceptance Criteria:** Lighting points meet same metadata standards as native BAS points

### Required Deliverables

- [ ] Lighting integration point list
- [ ] Communication protocol and architecture documentation
- [ ] Coordinated control sequence descriptions
- [ ] Data accuracy validation test results
- [ ] Metadata compliance verification for lighting points
- [ ] As-built integration diagrams

### Acceptance Criteria

Lighting controls integration validation is complete when all integration points are documented and accessible, data accuracy is verified, coordinated control sequences function correctly, and lighting points comply with metadata validation requirements.

---

*This document is part of the Digital Commissioning of Building Automation Systems Standard, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
