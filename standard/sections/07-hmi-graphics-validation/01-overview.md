# 7.0 BMS HMI Graphics Validation

## 7.0.1 Purpose and Scope

This section defines commissioning specifications and verification procedures for the operator interfaces commonly called BMS or BAS "graphics." Acceptance shall address whether users can recognize conditions, understand their significance, and perform the required tasks using trustworthy process information. Visual appearance alone is insufficient evidence.

The scope includes operational overviews, equipment and system displays, point faceplates, alarm views, trends, schedules, and command interactions provided for HVAC, plumbing, and integrated building systems. Each project shall identify the included systems, operator roles, clients, and control functions. A graphic does not establish that the underlying control sequence or field installation is correct; those shall have separate commissioning evidence linked where relevant.

## 7.0.2 Basis and Requirement Status

The technical reference reviewed for this section is **ANSI/ISA-101.01-2015**, particularly clauses 3.1.44–3.1.45, 4–5, and 6–9. Clause locators below refer specifically to that edition. This section uses original summaries and BMS applications; the licensed standard is not part of the deliverable.

The 2015 edition includes mandatory provisions in clauses 4, 5, and 9; clauses 6–8 provide recommendations. A clause containing requirements also includes recommendations. Display hierarchy, specific colors, timing examples, and this section's coverage rules shall not be represented as universal ISA mandates.

The **shall** statements in this section are requirements of this commissioning standard when adopted by the project. They include applied BMS requirements selected to make acceptance testable. The basis table in Section 7.1 identifies the relevant ISA subject matter, rather than asserting that ISA prescribes each implementation detail. Passing this section does not establish conformity with every provision of ISA-101 or constitute ISA certification.

## 7.0.3 Verification and Validation

In this section:

- **Verification** evaluates the output of a lifecycle activity against its defined objectives and requirements, using reviews, examinations, tests, and other objective evidence. It includes design review, configuration inspection, offline tests, and integrated tests.
- **Validation** demonstrates that the HMI as installed meets applicable requirements and specifications. It draws on verification evidence and includes representative users performing their specified tasks in the intended operating context.

These distinctions follow the subjects of ISA-101 clauses 3.1.44–3.1.45. Validation shall be planned across the lifecycle; it shall not be reduced to an operator preference survey or a final screenshot review.

## 7.0.4 Coordination and Precedence

The Lead System Integrator, Digital Commissioning Authority (DCA), and Owner's representative shall carry the responsibilities assigned in Section 2.4 into the HMI acceptance plan. The integrator shall prepare the requirements, configuration, test procedures, and results. The DCA shall review coverage, witness the designated tests, and verify deficiency closure. The Owner's representative shall approve the task basis and acceptance criteria, provide representative users, and accept the completed evidence.

Section 5.4 remains the source of existing data-access and performance limits; Section 7 adds content, interaction, and task-effectiveness evidence. Sections 2.5 and 3.9 govern cybersecurity and software/source access; Section 6 governs metadata. The HMI acceptance plan shall identify these dependencies and resolve conflicts before testing. A project-specific HMI requirement shall not silently relax another adopted requirement.

The project shall approve its HMI philosophy, style guide, and reusable toolkit, or identify equivalent controlled documents. This section validates the specified design and its operational outcomes without selecting a vendor, a universal palette, or a fixed number of screens.

---

*This document is part of the Digital Commissioning of Building Automation Systems Standard, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
