# 4.3 Level 3: Semantic Model Validation

## 4.3.1 Validation Requirements

### Semantic Model Implementation Validation
The semantic model implementation must be validated against the project-specific modeling standard and relationship requirements. This validation ensures that all BAS components, spaces, and their functional and physical relationships are accurately represented in a machine-readable format that supports advanced analytical applications.

**Required Deliverable**: Complete semantic model export in the format specified by project requirements (e.g., Brick Schema TTL, custom RDF/OWL, JSON-LD, or other specified semantic format).

### Relationship Completeness Validation
All system relationships must be validated for:

- Equipment-to-equipment connections and dependencies
- Equipment-to-space service relationships
- System hierarchy and containment relationships
- Energy and substance flow pathways
- Control and monitoring relationships

### Model Integrity Validation
The semantic model must demonstrate:

- Syntactic validity according to the specified modeling language/schema
- Semantic consistency with the designated ontology or vocabulary
- Complete representation of all physical and logical system components
- Traceable pathways from spaces to building services

## 4.3.2 Validation Criteria Examples

The following examples illustrate validation criteria that would be applied based on project-specific semantic modeling standards:

### Semantic Modeling Standard Examples

- **Brick Schema**: Validation against Brick ontology classes and relationships (e.g., `isFedBy`, `isLocatedIn`, `serves`, `hasPoint`)
- **Custom Ontology**: Validation against project-specific semantic model and relationship definitions
- **Industry Standards**: Validation against IFC, BOT (Building Topology Ontology), or other specified semantic standards
- **Hybrid Approaches**: Validation of models combining multiple ontologies or standards

### Relationship Validation Examples

- **Service Relationships**: Equipment serving spaces through appropriate relationship chains
- **Energy Pathways**: Complete energy flow chains from building services to end-use equipment
- **Spatial Relationships**: Equipment located in appropriate spaces with proper containment hierarchies
- **Control Relationships**: Controllers linked to controlled equipment and monitored points

### Query Capability Requirements Examples
Based on project-specific analytical needs, the model must support queries such as:

- **Energy Chain Tracing**: From any space, trace complete energy supply chain to building service entrance
- **Equipment Discovery**: Find all equipment of specific types serving designated areas
- **Impact Analysis**: Identify all spaces affected by equipment outages or system changes
- **Performance Analysis**: Group related equipment and points for analytics applications

## 4.3.3 Verification Procedures

### Model Syntax and Schema Validation Method
1. **Format Validation**

    - **Objective**: Verify submitted model conforms to specified semantic format and syntax
    - **Method**: Automated parsing and validation using appropriate semantic web tools (e.g., RDF validators, OWL reasoners)
    - **Acceptance Criteria**: 100% successful parsing with zero syntax errors or schema violations

2. **Ontology Compliance**

    - **Objective**: Confirm model uses only approved classes and relationships from designated ontology
    - **Method**: Automated validation against the project-specified ontology or vocabulary
    - **Acceptance Criteria**: 100% of model elements are valid according to the specified semantic standard

### Relationship Completeness Testing Method
1. **System Connectivity Validation**

    - **Objective**: Verify all system components are properly connected through semantic relationships
    - **Method**: Graph analysis to identify orphaned entities and incomplete relationship chains
    - **Acceptance Criteria**: 100% of equipment and spaces are connected to appropriate system hierarchies

2. **Service Chain Completeness**

    - **Objective**: Confirm complete service pathways from building services to served spaces
    - **Method**: Automated traversal of service relationships to verify end-to-end connectivity
    - **Acceptance Criteria**: 100% of conditioned spaces have traceable pathways to appropriate building services

### Functional Query Validation Method
1. **Required Query Execution**

    - **Objective**: Verify model supports all project-specified analytical query requirements
    - **Method**: Execute suite of validation queries designed to test semantic model completeness
    - **Acceptance Criteria**: All required query types return complete and accurate results

2. **Energy Chain Tracing Validation**

    - **Objective**: Confirm ability to trace complete energy supply chains from spaces to building services
    - **Method**: Sample-based testing using automated queries from representative spaces to building service entrances
    - **Acceptance Criteria**: 100% of tested spaces return complete energy chain traces terminating at appropriate building services (e.g., electrical service, gas service, chilled water service)

### Semantic Accuracy Verification Method (Sampling-Based)
1. **Relationship Accuracy Testing**

    - **Objective**: Verify semantic relationships accurately represent physical and functional system relationships
    - **Method**: Sample-based verification of critical relationships against design documents and field conditions
    - **Acceptance Criteria**: 100% of sampled relationships are semantically accurate and physically correct

2. **Model-Reality Correspondence**

    - **Objective**: Confirm semantic model accurately represents actual system implementation
    - **Method**: Cross-validation of model against as-built drawings, control sequences, and system commissioning data
    - **Acceptance Criteria**: No material discrepancies between semantic model and actual system implementation

### Advanced Analytics Readiness Testing Method
1. **Application Query Performance**

    - **Objective**: Verify model supports efficient execution of analytical applications
    - **Method**: Performance testing of complex queries representative of intended system applications
    - **Acceptance Criteria**: Query performance meets project-specified response time requirements

2. **Integration Capability Testing**

    - **Objective**: Confirm model can integrate with specified analytics platforms and applications
    - **Method**: Test model loading and querying in designated analytics tools or platforms
    - **Acceptance Criteria**: Successful integration and operation with all specified target applications

---

*This document is part of the Digital Commissioning of Building Automation Systems Standard, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
