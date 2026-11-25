# 7.1 HMI Graphics Commissioning Specifications

## Requirements

The following stable identifiers shall be used in the requirements-to-evidence matrix. Each applicable requirement shall identify its implementation, tests, acceptance criteria, and evidence. A requirement marked not applicable shall have a scope-based reason approved by the DCA and Owner's representative.

### HMI-01: Users, Tasks, and Controlled Design Basis

Before detailed graphic construction, the project shall document primary and secondary users; their responsibilities and privileges; and normal operation, startup, shutdown, abnormal operation, and recovery tasks. Each task shall identify the starting condition, decision, information needed, permitted action, expected result, and applicable operating procedure. Secondary-user needs shall not obstruct the primary operator's specified tasks.

The Owner's representative and representative operators shall review the conceptual displays and navigation against those tasks. The controlled philosophy, style guide, and toolkit shall address terminology, symbols and states, alarm emphasis, data quality, number formatting, navigation, interactions, supported clients, and exceptions. Each artifact shall have a revision and owner.

### HMI-02: Display Inventory and Navigation

The integrator shall provide an inventory of every operational display and faceplate, its purpose, equipment and space identifiers, template revision, entry links, and supported roles. Each display shall preserve equipment identity and orientation when navigating to alarms, trends, related equipment, and diagnostics. All applicable tasks shall have a documented route to the required information and controls.

The project shall specify task-based navigation limits and demonstrate them with users. Overview, primary operation, detail, and diagnostics shall be allocated deliberately; they may share a screen where appropriate. Acceptance shall not require exactly four screens or treat hierarchy levels as click counts.

### HMI-03: Point Identity and Binding

Every displayed measurement, status, alarm, calculated value, and writable control shall be traceable to its source. The binding register shall include display and element IDs, equipment/space identity, source object/property or equivalent address, units, scaling, precision, enumeration meanings, and read/write status. Calculated values shall identify their inputs, formula, and treatment of bad inputs. Writable elements shall additionally identify destination, limits, role permission, and applicable command priority or arbitration.

Displayed names and relationships shall agree with the approved point schedule, sequence, and metadata. Template instances shall bind to their actual equipment. A source label or link that resolves successfully shall not by itself prove that the binding is correct.

### HMI-04: Process Context and Operating State

Each operating display shall present the information necessary for its tasks, including applicable actual values, effective setpoints, operating modes, schedule/occupancy state, enable conditions, commands, and independent feedback. The design shall distinguish requested, effective, commanded, and proven states wherever those differ. Missing feedback shall be identified as unavailable; a command shall not be relabeled as proof.

Relevant expected ranges, limits, interlocks, overrides, and trends shall be accessible in the task's agreed route. Ranges and limits shall have an approved basis in the sequence or operating requirements. A graphic shall distinguish process deviation, an alarm, and an expected transition or intentional off state; it shall not invent alarm thresholds from display decoration.

### HMI-05: Data Quality, Time, and Display Failure

The project shall define quality states and freshness rules for each point class, including source failures, supervisory disconnect, invalid values, and unreliable calculations. The register shall distinguish last successful acquisition, last value change, and source timestamp where available. An unchanged value shall not be classified as stale solely because a change-of-value event has not occurred; use a verified communication health mechanism or bounded acquisition strategy.

When current information cannot be trusted, affected displays shall identify that condition within the approved detection limit, distinguish retained observations from current observations, and show the last successful observation time or age. Missing data shall not appear as zero, normal, or confirmed equipment status. Overview summaries and calculated values shall propagate relevant uncertainty. Reconnection shall require fresh valid evidence before restoring a good indication.

The installed client shall expose a frozen display or loss of updates through a freshness/health mechanism appropriate to the platform. A server-side quality flag alone shall not be accepted as proof that a stalled client can warn its operator.

### HMI-06: Visual Meaning and Readability

Important process, alarm, quality, and override states shall have persistent textual or symbolic distinctions in addition to color. Normal presentation shall leave abnormalities discernible. Animation, flashing, three-dimensional decoration, or corporate branding shall not obscure the specified task information or compete with priority indications.

The style guide shall define text sizes, contrast criteria, input target sizes, focus treatment, and layout behavior for supported clients. Verification shall include actual viewing distances, ambient lighting, zoom/scaling, input devices, and relevant user sensory needs. Grayscale review shall supplement these checks. Required labels, values, and actions shall remain legible and reachable in supported layouts, including keyboard operation for supported web clients.

### HMI-07: Alarm and Event Context

The project alarm philosophy shall define priority, thresholds/delays, routing, acknowledgment, shelving/suppression, return-to-normal behavior, and response responsibilities. HMI acceptance shall verify these configured behaviors and their linkage to equipment, source condition, timestamps, response guidance, and relevant trends. Acknowledgment shall be distinguishable from condition clearance, reset, or equipment recovery.

Active, acknowledged, returned-to-normal, and applicable suppressed or shelved states shall remain distinguishable. Multiple simultaneous abnormalities shall preserve visibility of the approved priorities. HMI testing shall not create or revise alarm rationalization implicitly; discrepancies shall be referred to the responsible alarm/sequence designer.

### HMI-08: Commands, Permissions, and Override Lifecycle

Writable interactions shall identify the destination equipment, requested action/value, units, effective limits, and applicable operating restrictions. Invalid, out-of-range, non-finite, and unauthorized requests shall be rejected with an actionable explanation. Cancellation shall send no command. Confirmation shall be applied to the risk-significant actions identified in the approved task analysis and shall show the exact equipment and proposed action.

The HMI shall distinguish a pending request, controller acceptance/rejection, effective value after arbitration, and observed process response. Timeout or loss of connection shall show an unresolved outcome where acceptance is unknown; the client shall not infer success or silently replay a request after reconnecting. Feedback disagreement shall be exposed after the sequence-defined proof interval.

Override status, applicable BACnet priority or equivalent arbitration, ownership, expiry where supported, and a permitted release-to-automatic action shall be available to the authorized operator. Tests shall verify that releasing an override restores the expected underlying control and that a higher-priority command is not misrepresented as a successful lower-priority change. Authorization shall be enforced by the system accepting the write, including attempts outside the visible interface.

### HMI-09: Trends and Schedules

Trends used for decisions shall identify signals, units, axes, time window, timezone, sampling/aggregation, and relevant targets or limits. Gaps, quality loss, and out-of-range values shall be distinguishable from valid history; lines shall not imply observations across missing data without a visible qualification. Exported data shall preserve timestamps, units, and quality or an accompanying quality record.

Schedule views shall identify the affected equipment, timezone, effective occupied/unoccupied state, upcoming transition, and applicable holiday/exception/override precedence. Authorized edits shall be validated, confirmed where specified, and traceable. Acceptance shall include a calendar exception and daylight-saving transition where applicable to the configured timezone.

### HMI-10: Performance and Task Criteria

The acceptance plan shall include measurable limits for display call-up, refresh/data age, write acceptance, write readback, alarm presentation, and task completion. It shall identify the measurement start/end events, test hardware/client, network path, point counts, concurrent load, repetitions, and allowed failures. Write readback shall not be treated as proof of physical response; proof timing shall come from the sequence.

The plan shall apply Section 5.4's existing limits and fill uncovered cases, including graphics with 21–49 dynamic points and command acceptance/readback. Where navigation and full data population have different limits, both shall be measured. Slower polled or remote sources shall remain subject to an explicit approved freshness and task-risk assessment. Numeric ISA examples shall not be substituted for the adopted project limits.

### HMI-11: Training, Recovery, and Change Control

Role-specific training and operating guidance shall cover navigation, alarm response, quality loss, command/proof distinctions, overrides, schedules, and recovery. Training shall be integrated into the Owner's training process and updated through management of change. Quiz completion alone shall not satisfy installed-HMI task validation.

The handover shall include editable source/configuration and dependencies, toolkit and display revisions, point bindings, approved standards, permissions, test evidence, open concessions, training records, backups, and a restoration procedure. Restoration shall be tested in an isolated or otherwise approved environment and shall verify bindings, permissions, history access, and command behavior after recovery.

Changes to shared symbols, bindings, firmware/platform behavior, sequences, limits, permissions, or displays shall trigger impact review and regression tests of affected requirements and instances. The Owner shall assign an ongoing review interval and owner for task effectiveness, outstanding defects, and changes in operating needs.

## Reference and Verification Matrix

The ISA column identifies supporting subject matter. All detailed BMS tests and coverage rules are applied requirements of this section. V and U identifiers are defined in Section 7.2.

| Requirement | ISA-101.01-2015 subject locators | Required evidence/test families |
| --- | --- | --- |
| HMI-01 | 4.1–4.3.4; 5.1 | Approved task/design basis; V-01; all applicable U tasks |
| HMI-02 | 6.3; 7.2.2 | Inventory, route checks; V-02; U-01–U-06 as applicable |
| HMI-03 | 4.3.4; 4.4.3–4.4.5; 7.2.1.2 | Binding register and field/source comparisons; V-02 |
| HMI-04 | 5.1.4; 6.2–6.3 | Mode/state evidence; V-03; U-01–U-03 |
| HMI-05 | 5.1; 5.1.4; 8.3.2 | Quality/failure injections and timing; V-04; U-04 |
| HMI-06 | 5.2–5.3; 7.3 | Supported-client and workplace review; V-05; applicable U tasks |
| HMI-07 | 5.1; 7.2.2; 9.1.1 | Alarm configuration/state evidence; V-06; U-02–U-03 |
| HMI-08 | 7.2.1; 7.2.3; 7.2.5; 8.3.3–8.3.4 | Command, role, priority, and feedback tests; V-07; U-03, U-05 |
| HMI-09 | 6.2; 6.3.1; 7.2.1.2 | Historical/time/schedule comparisons; V-08; U-02, U-06 |
| HMI-10 | 4.4.3; 8.1–8.3 | Raw timing/load records; V-09; all U task scores |
| HMI-11 | 4.4.4–4.6; 9.1 | Training, restoration, change records; V-10; U-05 |

## Example: AHU Unable to Maintain Supply Temperature

An AHU operating display shows the measured supply temperature, effective target, recent trend, cooling demand, fan command and independent proof, occupancy/mode, and data quality. A rising temperature with a high cooling command supports investigation; it does not prove valve movement, water flow, or a particular root cause. The operator can reach interlock and source-quality evidence without losing AHU identity. On temperature communication failure, the retained observation is labeled historical and the current temperature becomes unknown.

Acceptance evidence for this example includes the actual AHU bindings (V-02), independent command/proof states (V-03/V-07), failure and recovery records (V-04), and an operator correctly assessing a rising-temperature scenario (U-02). A screenshot alone cannot establish all four.

## Example: Occupancy Exception and Temporary Override

A zone is warm during a special weekend event. The display identifies the effective unoccupied state, local timezone, calendar exception, next occupied transition, and the precedence of any temporary override. An authorized operator requests a bounded occupancy override, sees whether it became effective, and later verifies expiry or release back to the underlying schedule. Historical temperature and occupancy traces retain any communication gaps.

Acceptance combines schedule/calendar and trend checks (V-08), permission and override lifecycle tests (V-07), and an operator using the actual installed interface to identify the cause and verify the permitted correction (U-06). An event added to a calendar is not by itself evidence that the intended equipment became occupied.

---

*This document is part of the Digital Commissioning of Building Automation Systems Standard, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
