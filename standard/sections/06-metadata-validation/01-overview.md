# 4.0 Metadata Validation Framework

## Overview

This section defines the validation and verification requirements for digital metadata representation of building automation systems. The validation process is structured in three progressive levels, each building upon the previous to create increasingly sophisticated machine-readable representations.

## Three-Level Validation Structure

### Level 1: Naming Convention Validation
Validates that all device and point names conform to the project-specific naming standard through automated pattern matching and syntax verification.

### Level 2: Tagging and Labeling Validation  
Validates that metadata tags and labels are consistently applied and semantically correct through systematic verification of classification and descriptive attributes.

### Level 3: Semantic Model Validation
Validates that system relationships and hierarchies are properly modeled and machine-readable through graph analysis and semantic verification.

## Validation Independence

Each level of metadata validation is designed to work with any project-specific:

- Naming convention or standard (e.g., project appendices, industry standards)
- Tagging taxonomy or vocabulary 
- Semantic modeling approach or ontology
- Database structure or format

The validation procedures verify conformance to the **specified** approach rather than prescribing a particular approach.

## Progressive Requirements

Each level has distinct validation requirements:

- **100% Coverage**: All elements at each level must pass syntax and format validation
- **Sampling-Based Correctness**: Strategic sampling ensures semantic accuracy and proper implementation
- **Cross-Level Consistency**: Higher levels must be consistent with validated lower levels

---

*This document is part of the Digital Commissioning of Building Automation Systems Standard, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
