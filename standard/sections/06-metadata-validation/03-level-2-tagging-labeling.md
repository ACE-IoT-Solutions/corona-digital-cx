# 4.2 Level 2: Tagging and Labeling Validation

## 4.2.1 Validation Requirements

### Tagging Implementation Validation
The tagging and labeling implementation must be validated against the project-specific tagging standard and data model requirements. This validation ensures that all BAS points and equipment have consistent, standardized metadata tags that enable automated querying and analysis.

**Required Deliverable**: Complete tagged data model export in the format specified by project requirements (e.g., Haystack JSON, Brick TTL, custom JSON schema).

### Tag Completeness Validation
All BAS components must be validated for:

- Presence of required base tags as defined by the project tagging standard
- Appropriate equipment classification tags
- Point type and measurement classification tags
- Relationship tags linking points to parent equipment
- Location and system hierarchy tags

### Tag Consistency Validation
Tagging implementation must demonstrate:

- Consistent application of the designated tagging vocabulary
- Proper tag combinations and relationships
- Absence of conflicting or contradictory tag assignments
- Compliance with the specified data model schema

## 4.2.2 Validation Criteria Examples

The following examples illustrate validation criteria that would be applied based on project-specific tagging standards:

### Industry Standard Tagging Examples

- **Project Haystack**: Validation against Haystack tag definitions and entity relationships (e.g., `site`, `equip`, `point`, `sensor`, `cmd`, `sp`, `air`, `temp`)
- **Brick Schema**: Validation against Brick ontology classes and relationships
- **Custom Taxonomy**: Validation against project-specific tag dictionary and relationship rules

### Tag Coverage Requirements Examples

- **Base Tags**: All entities have required foundational tags (site, equipment type, point classification)
- **Measurement Tags**: All sensor and setpoint entities include units, measurement type, and substance tags
- **Relationship Tags**: All points are properly linked to parent equipment through relationship tags
- **Location Tags**: All entities include appropriate spatial hierarchy tags

### Schema Compliance Examples

- **Required Tag Combinations**: Verify mandatory tag patterns (e.g., temperature sensors must have `temp` + `sensor` + substance tag)
- **Prohibited Tag Conflicts**: Identify mutually exclusive tag combinations
- **Enumeration Validation**: Confirm enumerated tags use only allowed values from the specified vocabulary

## 4.2.3 Verification Procedures

### Data Model Parsing Method
1. **Schema Validation**
   - **Objective**: Verify submitted data model conforms to specified format and schema
   - **Method**: Automated parsing and schema validation against project-specified data model format
   - **Acceptance Criteria**: 100% successful parsing with zero schema validation errors

2. **Tag Dictionary Compliance**
   - **Objective**: Confirm all tags are from approved vocabulary
   - **Method**: Cross-reference all tags against the project-specified tag dictionary or ontology
   - **Acceptance Criteria**: 100% of tags are recognized terms from the approved vocabulary

### Tag Completeness Testing Method
1. **Required Tag Coverage**
   - **Objective**: Verify all entities have mandatory tags per project requirements
   - **Method**: Automated queries to identify entities missing required tag categories
   - **Acceptance Criteria**: 100% of entities have all required base tags as defined by project tagging standard

2. **Tag Relationship Validation**
   - **Objective**: Confirm proper parent-child and system relationships through tags
   - **Method**: Graph analysis and relationship queries to verify tagged connections
   - **Acceptance Criteria**: 100% of points are properly linked to parent equipment and system hierarchies

### Semantic Correctness Verification Method (Sampling-Based)
1. **Equipment Tag Accuracy**
   - **Objective**: Verify equipment tags accurately represent physical equipment types and functions
   - **Method**: Sample-based verification of at least one instance of each unique equipment type
   - **Acceptance Criteria**: 100% of sampled equipment have semantically correct tag combinations

2. **Point Tag Accuracy**
   - **Objective**: Verify point tags accurately represent measurement types, units, and functions
   - **Method**: Sample-based verification covering all point type categories (sensors, commands, setpoints, alarms)
   - **Acceptance Criteria**: 100% of sampled points have semantically accurate tag combinations and proper units of measure

### Query Validation Method
1. **Functional Query Testing**
   - **Objective**: Verify tagged data supports intended analytical and operational queries
   - **Method**: Execute a suite of predefined validation queries designed to test tag completeness and correctness
   - **Acceptance Criteria**: All validation queries return expected results without errors

2. **Data Accessibility Testing**
   - **Objective**: Confirm tagged data enables automated discovery and filtering
   - **Method**: Test ability to programmatically find and filter entities by tag combinations
   - **Acceptance Criteria**: All major equipment types and point categories can be successfully discovered and filtered using tag-based queries

---

*This document is part of the Digital Commissioning of Building Automation Systems Standard, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
