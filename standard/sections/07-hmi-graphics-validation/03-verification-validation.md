# 7.2 HMI Graphics Verification and Validation Procedures

## 7.2.1 Acceptance Plan and Hold Points

Before testing, the integrator shall submit an acceptance plan for DCA and Owner approval. It shall identify requirement IDs, approved design/task revisions, the deployed configuration, the complete display/binding population, critical tasks, witnesses, test procedures, coverage, acceptance limits, evidence format, and deficiency workflow. Unfilled limits or unresolved conflicts shall block the affected test, rather than permit acceptance by observation alone.

The following hold points shall apply:

1. **Design review:** approve users/tasks, philosophy/style guide/toolkit, navigation, bindings, state definitions, and task/performance criteria before accepting detailed construction.
2. **Offline verification:** test reusable templates, state combinations, invalid/unauthorized interactions, failure behavior, and scripts before integrated testing.
3. **Installed verification:** confirm actual bindings, state transitions, performance, permissions, and recovery on the released configuration and intended clients.
4. **Installed validation and handover:** complete representative-user tasks, close defects, verify training and restoration evidence, and obtain DCA recommendation and Owner acceptance before operational handover.

Simulation shall be identified in each result, including what it bypasses. Offline success shall not replace installed binding, communication, permission, or performance evidence. Dangerous or disruptive conditions shall be tested by approved simulation/injection methods; tests shall not defeat protective interlocks or create uncontrolled process conditions. Each test shall define prerequisites, safe boundaries, abort conditions, and restoration checks.

## 7.2.2 Coverage and Sampling

The following minimum coverage is an applied requirement of this commissioning standard, rather than an ISA sampling rule:

- **All instances:** inspect 100% of display and faceplate inventory, navigation links, required labels/units/states, bindings including write destinations, configured permissions, and required quality indicators against controlled exports and the point schedule. Record population and inspected counts; unresolved or unsupported export fields shall receive manual examination.
- **Reusable behavior:** exercise every unique template, faceplate, command workflow, quality path, and defined operating/alarm state. Include each distinct controller/integration family where behavior differs. Shared template testing shall not substitute for instance binding inspection.
- **Installed witnessed sample:** include every critical equipment/task instance designated in the approved risk assessment, every custom/non-template display, and at least one installed instance of each remaining equipment/template/controller-integration combination. The DCA shall select additional instances after receiving the population register; the plan shall record their number and selection basis before execution. For each selected instance, stimulate or compare independent source evidence for every displayed/writable binding and execute the applicable scenario tests.
- **Users and clients:** validation shall include at least two representative primary operators in total, at least one user for each distinct operating role, and each distinct supported operating context/client with applicable tasks. If staffing cannot meet this minimum, the Owner shall approve a documented concession and additional witness or follow-up validation before acceptance. Secondary roles shall be tested where their assigned tasks differ. A small usability sample is commissioning evidence, not a statistical claim about all users.
- **Defect expansion:** a template or common workflow defect shall trigger correction and regression across every affected instance. An instance-specific binding/configuration defect shall trigger examination of the entire affected equipment/template/integration stratum, correction of all affected instances, and DCA-selected witnessed retests. The matrix shall show the expanded population and results; sampling shall not conceal a known defect.

## 7.2.3 Verification Test Families

Every executed test shall record the detailed setup and injected/source values so another tester can reproduce it. The pass conditions below apply in addition to the approved project limits.

### V-01: Design Basis and Traceability — HMI-01

1. Compare the task register with approved sequences and interviews with primary users. Include normal, startup/shutdown, abnormal, and recovery tasks and secondary-user requirements.
2. Walk through conceptual displays and navigation with those users. Trace every task to required information, actions, role permissions, procedures, and planned U tests.
3. Review philosophy, style guide, toolkit revisions, exceptions, measurable limits, and named approval authorities.

**Pass:** no in-scope task or requirement lacks an approved design basis, acceptance criterion, implementation reference, and test assignment. Record approved exclusions explicitly.

### V-02: Inventory, Navigation, and Binding — HMI-02–HMI-03

1. Export or enumerate all displays/elements and bindings. Reconcile against installed equipment, the point schedule, required task routes, and metadata. Check for duplicate IDs, orphan graphics, unresolved links, and cross-equipment references.
2. For the witnessed sample, apply distinguishable source values/states, compare with an independent controller/source read and the HMI, and record source and displayed timestamps, units, scaling, precision, and enumerations. Check calculation outputs against independently calculated expectations, including invalid inputs.
3. For each writable element in the sample, verify its destination using controlled source readback and command records; also confirm that an adjacent similar equipment instance is unaffected. Use bounded test values or an approved isolated harness.

**Pass:** 100% of register bindings and routes agree with the approved design; every witnessed observation and destination is correct within approved measurement/scaling tolerances. No incorrect equipment/space identity or unresolved binding is acceptable.

### V-03: Operating Modes and Independent Feedback — HMI-04

1. Exercise applicable occupied/unoccupied, automatic/manual, enabled/disabled, startup/shutdown, unavailable, and interlocked states using the approved state table.
2. Set command/proof combinations independently: on/on, off/off, on/off, and off/on. Apply the sequence-defined transition/proof delays.
3. Compare effective target, range/limit, schedule, demand, command, proof, and interlock indications with the sequence and source evidence.

**Pass:** each state is correctly identified, including expected transitions; proof is independent or explicitly unavailable. A disagreement remains visible after its allowed interval, and commanded state never establishes proof by itself.

### V-04: Data Quality, Frozen Client, and Recovery — HMI-05

1. With a known valid observation, interrupt the point/device path, supervisory path, and client update path separately. Inject invalid/out-of-range quality and loss of an input to a calculation. Record failure onset and visible detection times.
2. Verify current/retained distinction, timestamp/age, unknown-state propagation, and the effect on overviews, trends, and command availability. Leave a healthy constant source unchanged beyond the stale threshold to check that freshness is not based solely on value changes.
3. Stall or disconnect client updates while the last normal page remains visible. Verify the specified health mechanism and recovery procedure; if the client cannot self-report a total stall, demonstrate the approved independent watchdog or operator detection method within its limit.
4. Restore each path. Confirm fresh valid observations before good state returns and verify that pending commands are not replayed.

**Pass:** all relevant failures become apparent within approved limits; no failure produces a false normal, zero, proven state, or current-looking retained value. A healthy unchanged source remains good. Recovery requires valid evidence and follows the approved procedure.

### V-05: Readability and Supported Interaction — HMI-06

1. Review normal and abnormal displays in color and grayscale on minimum supported screens and at actual workstation lighting/viewing distances, zoom/scaling, and specified input methods.
2. Check text, symbols, emphasis, focus order/visibility, labels, control targets, and layout against the approved style guide. Use keyboard-only navigation for supported web-client tasks.
3. Introduce multiple abnormalities and open faceplates/trends. Confirm they do not hide priority information or destination identity.

**Pass:** required information remains readable and task controls reachable on every supported configuration; important conditions are identifiable without color alone. Retain measurements and observed exceptions, rather than an unexplained "looks good."

### V-06: Alarm Lifecycle and Context — HMI-07

1. Inject a documented alarm condition with its configured delay/priority. Capture source trigger and HMI annunciation times; navigate to the correct equipment, trend, and response guidance.
2. Acknowledge while the condition remains active; return the source to normal separately. Exercise supported reset, shelving, and suppression with authorized and unauthorized roles.
3. Inject simultaneous conditions of different approved priorities, including a communication fault, and inspect sorting, visibility, counts, and state indications.

**Pass:** displayed source, state, priority, time, and routing agree with the alarm configuration and Section 5.4 limits. Acknowledgment does not imply normality or recovery; suppression does not conceal its own status. Record any alarm-design deficiency separately from graphic behavior.

### V-07: Command Transaction, Roles, and Override Release — HMI-08

1. Test below/at/above numeric limits; blank, malformed, and non-finite values; wrong permissions; cancellation; and the approved confirmation flow. Record attempted and actual writes.
2. Send a valid command and independently record requested value, acceptance/rejection, effective readback, priority arbitration, and physical feedback. Test a higher-priority active command, a proof failure after its delay, controller rejection, and write/readback timeout.
3. Interrupt communication before and after request transmission. Restore it and check the unresolved-result message, readback reconciliation, and absence of automatic replay. Use command logs to detect unintended duplicate writes.
4. Create and release a permitted override, including expiry where supported. Verify the underlying schedule/control state resumes. Attempt a forbidden write directly through the supported service/API or protocol as the restricted user, not just through a hidden/disabled button.

**Pass:** invalid/canceled/unauthorized requests make no effective write; valid requests reach only their intended destination. Outcomes and unknown results are truthful, feedback is independent, and release/expiry restores the expected control. No unauthorized service write, hidden residual override, or implied physical success is accepted.

### V-08: Trend Integrity and Schedule Behavior — HMI-09

1. Compare raw history/export and displayed samples, scales, units, timezone, quality, and aggregation for known source values, a gap, and a bad-quality interval. Include an excursion outside the initial plotted range.
2. Compare active and next schedule states against the source schedule. Exercise a normal transition, holiday/calendar exception, manual override precedence, and authorized edit.
3. Where daylight saving applies, use an isolated clock/calendar fixture to exercise skipped/repeated local times. Record expected behavior from the approved schedule design before execution.

**Pass:** plots and exports represent the source history and gaps accurately; schedule state, next transition, precedence, and edit results match approved expectations. No ambiguous local-time interpretation or clipped excursion conceals a condition relevant to the task.

### V-09: End-to-End Timing and Load — HMI-10

1. Record minimum supported hardware/client, topology, source update/polling strategy, network load, point counts, and concurrent users. Synchronize measurement clocks or use one recording clock; record measurement resolution and uncertainty.
2. For each selected graphics class, measure call-up from request until all required elements have valid data or explicit quality status. Measure navigation completion separately. Measure source-change-to-visible-update, request-to-controller-acceptance, request-to-effective-readback, alarm onset-to-presentation, and trend retrieval as separate intervals.
3. Include cold and warm call-ups; perform at least ten repetitions per applicable metric/configuration at single-user and maximum specified load. Also test 125% load for stability as required by Section 5.4. Retain raw results and report count, failures, median, and maximum.

**Pass:** every measured run meets its adopted absolute limit at single-user and maximum specified load, and the Section 5.4 degradation limits are met. At 125% load, demonstrate the specified graceful degradation and truthful quality indications. Do not average away a failed run. A measurement whose uncertainty straddles a limit is inconclusive and shall be resolved by better measurement or retest. These repetition and reporting rules are commissioning choices, not ISA-prescribed rates.

### V-10: Training, Backup Restoration, and Regression — HMI-11

1. Reconcile role-specific training, procedures, and known limitations with the installed display/toolkit revisions. Observe the relevant U tasks after training.
2. Restore the delivered backup/source and dependencies into an approved isolated or controlled environment. Compare display/binding/permission inventories and exercise selected quality, history, and command tests.
3. For a representative change, trace affected templates/instances/tasks, approvals, updated training, regression scope, and rollback evidence through the management-of-change record.

**Pass:** the delivered configuration is recoverable, matches the tested baseline, and preserves required behavior. Training and change records identify roles and revisions; all applicable regression tests pass.

## 7.2.4 Installed Task Validation With Operators

Before observing users, approve each scenario's starting condition, available evidence, expected diagnosis/uncertainty, permitted response, critical errors, detection time, completion time, navigation limit where applicable, and allowed assistance. Set limits from task/process risk and operating needs before seeing results. Diagnostic success shall require recognizing what the evidence supports; it shall not require guessing a hidden root cause.

Each representative operator shall perform the applicable scenarios on the installed configuration and intended client after normal role training. An approved harness may introduce abnormal conditions, with the bypassed paths recorded and covered by installed verification. The observer shall record first detection, completion, route, errors, assistance, and outcome; the observer shall not coach scored trials. If assistance is needed, record the trial as assisted and apply the preapproved criterion. After corrections or retraining, use an equivalent scenario to reduce memorization effects.

| Scenario | Starting condition and task | Required observable result |
| --- | --- | --- |
| U-01: Normal operation and transition | Start on overview; identify a selected AHU/plant/zone, effective mode, target, schedule, and next transition. Follow an approved startup or shutdown transition. | Correct equipment and state; distinguish scheduled off/transition from a fault; no unintended command. |
| U-02: Thermal problem | Supply/zone temperature rises with a changing target or high cooling demand. Assess condition, direction, relevant evidence, and next action. | Identify deviation/trend, target and mode, source quality, command/proof evidence; select the procedure-supported response without claiming an unproven cause. |
| U-03: Failure to prove and concurrent alarms | Fan/pump command differs from feedback after the allowed delay; another alarm is present. Prioritize and investigate. | Detect disagreement and priorities, reach interlock/proof/response context, and distinguish acknowledgment from recovery. |
| U-04: Loss of trustworthy information | Retain a previously normal observation during source or client update failure. Decide what is known and how to proceed. | Recognize unknown current state and age, identify affected scope, and follow the approved communication/recovery procedure. |
| U-05: Command and override lifecycle | Make a permitted bounded change, encounter an overriding priority or rejected command, and return to automatic control. | Confirm destination and intent, distinguish acceptance/effective value/proof, recognize rejection/arbitration, and verify release without residual overrides. |
| U-06: Schedule and historical diagnosis | A space is uncomfortable after a calendar exception or occupancy override; use schedule and trend evidence. | Identify timezone, effective/next event, exception precedence and history gaps; make only the role-permitted correction and verify its effective result. |

**Pass:** every mandatory trial meets its preapproved task criteria, including correct outcome, time/route limits, and zero predefined critical errors. Aggregate averages shall not offset a failed critical task. Mark nonapplicable scenarios with an approved reason and replace them with tasks representing that equipment/role. Include plant, plumbing, and integrated systems where in scope rather than accepting AHU-only validation for all systems.

## 7.2.5 Evidence, Deficiencies, and Acceptance

Each test record shall include project/release, requirement and test IDs, equipment/display/element IDs, tester/witness/role, environment/client, prerequisites, source/injection method, expected result and numeric limit, actual result and raw timestamps, evidence location, coverage/population, pass/fail/inconclusive/not-tested/not-applicable status, deficiency ID, correction revision, and retest reference. An operator scorecard shall also include scenario, participant role, detection/completion times, navigation, assistance, critical errors, and outcome. Participant codes may be used in exported records.

The requirements matrix shall link every applicable requirement to all assigned tests and evidence. A blank result, missing witness, unsupported exclusion, or inconclusive measurement shall not count as a pass. Screenshots may support state/readability evidence; timings, bindings, command destinations, permissions, and recovery shall have corresponding source, log, or test records.

The project shall classify defects before testing. Incorrect equipment/write destinations, false normal/proof/quality indications, unauthorized control, concealed priority conditions, failed required tasks, and violations of adopted performance limits shall block acceptance. Cosmetic or other nonblocking defects may remain only under a written Owner concession recording impact, interim measure, responsible party, and closure date; a concession shall not be recorded as a passed test. Corrected defects shall be retested and affected coverage expanded as specified above.

Final acceptance shall require completed coverage, passing applicable verification and validation trials, closed blocking defects, approved remaining concessions, a reconciled final configuration, training evidence, and a demonstrated restoration. The DCA shall recommend acceptance and the Owner's representative shall sign the handover. The Owner shall assign recurring review and revalidation after relevant changes under HMI-11.

---

*This document is part of the Digital Commissioning of Building Automation Systems Standard, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
