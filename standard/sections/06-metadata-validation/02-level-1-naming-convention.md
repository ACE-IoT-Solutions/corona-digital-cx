# 4.1 Level 1: Naming Convention Validation

## Objective

To enforce a strict, standardized naming convention for all assets and points.

## Requirements

All BAS controllers, equipment, and points (software and hardware) must be named according to the project-specific naming convention outlined in the Project Naming Standard (e.g., Appendix A).

## Validation and Acceptance Criteria

### Validation Requirements (100% Coverage)
All names must programmatically validate against the regular expression (regex) defined in the project naming standard. This validation must achieve 100% coverage of all BAS controllers, equipment, and points. Any name failing the validation script must be corrected in the BAS database before this level is considered complete.

### Correctness Verification (Sampling-Based)
To verify that validated names are not only syntactically correct but also accurate, the following sampling requirements must be met:

- **Controller Models**: At least one controller of each unique model type must be 100% checked for naming correctness on both the device level metadata and the point level metadata.
- **Equipment Functions**: At least one piece of equipment representing each functional type (e.g., AHU, VAV, chiller, boiler) must be 100% checked for naming correctness at the device level and the point level

#### Device Level Correctness Checks:
- **Device Name**: Each token from the project naming standard definition (e.g., Appendix A) shall match the expected value. Examples:
  - If building identifier is a token: `B01` for Building 1, `B02` for Building 2
  - If floor identifier is a token: `F01` for Floor 1, `F02` for Floor 2
  - If equipment type is a token: `AHU` for Air Handling Unit, `VAV` for Variable Air Volume box
  - If equipment id is a token: 'AHU-01' for Air Handling Unit #1, it should use the same numbering scheme as shown on drawings for that specific equipment, or an owner provide equipment naming scheme.
  - If sequence number is a token: `001`, `002`, `003` for sequential numbering
- **Device Location**: Physical location matches the naming convention location tokens
- **Device Function**: Equipment function identifier accurately represents the actual equipment type and purpose

#### Point Level Correctness Checks:
- **Point Name**: Each token in the point name shall correspond to the correct naming convention definition. Examples:
  - **Equipment Reference**: Point prefix matches parent equipment name (e.g., `AHU01_SAT` for supply air temperature from AHU01)
  - **Measurement Type**: Point suffix accurately describes the measurement:
    - `_SAT` for Supply Air Temperature
    - `_RAT` for Return Air Temperature  
    - `_SF_CMD` for Supply Fan Command
    - `_DAM_POS` for Damper Position
    - `_SP` for Setpoint values
    - `_ALM` for Alarm points
- **Data Type Verification**: Point data types match the expected type for the measurement:
  - Temperature points: `Real` or `Float` data type
  - Status/Command points: `Boolean` or `Binary` data type
  - Position feedback: `Real` or `Analog` data type (0-100%)
  - Alarm points: `Boolean` or `Binary` data type
- **Units of Measure**: Engineering units match the point type and local standards:
  - Temperature: `°F`, `°C`, or `K` as appropriate
  - Pressure: `psi`, `Pa`, `kPa`, or `inWC` as appropriate
  - Flow: `CFM`, `GPM`, `L/s`, or `m³/h` as appropriate
  - Percentage: `%` for damper positions, valve positions
  - Power/Energy: `kW`, `kWh`, `BTU/h` as appropriate

This correctness verification ensures that names follow the intended naming logic and accurately represent the physical assets and their functions within the building automation system.

---

*This document is part of the Digital Commissioning of Building Automation Systems Standard, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
