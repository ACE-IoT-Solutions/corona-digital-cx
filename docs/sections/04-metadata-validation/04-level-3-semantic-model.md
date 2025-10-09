# 4.3 Level 3: Semantic Model Validation

## Objective

To define and validate the functional and physical relationships between all system components, spaces, and the services they provide.

## Requirements

The complete BAS asset inventory and relationships must be modeled using the Brick Schema (v1.3 or later). The model must define key relationships such as `isFedBy`, `isLocatedIn`, and `serves`.

## Validation and Acceptance Criteria

The submitted model (e.g., in Turtle `.ttl` format) must be syntactically valid and pass a series of SPARQL validation queries designed to confirm the system's topological integrity. Successful validation demonstrates a complete and accurate digital representation of the building systems.

### Required Query Capabilities

The model must be able to answer the following types of queries:

#### Energy Chain Trace

Provided a room or space ID, the model must return all equipment in the energy chain that serves and controls the conditions in that space. The trace must terminate at a building service entrance (e.g., `Electrical_Service`, `Gas_Service`, `Chilled_Water_Service`).

*(Placeholder for additional validation queries)*

---

*This document is part of the Digital Commissioning of Building Automation Systems Standard, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
