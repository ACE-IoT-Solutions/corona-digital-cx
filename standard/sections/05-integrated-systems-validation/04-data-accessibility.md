# 5.4 Data Accessibility and Performance

## Overview

The ultimate value of validated digital infrastructure lies in its usability for building operations and advanced applications. This section establishes performance requirements for data access, visualization responsiveness, and system usability to ensure that correctly structured data is also performant and accessible.

## Requirements

### 5.4.1 Graphical User Interface Performance

The BAS supervisory system graphical interface shall meet the following performance criteria:

- **Graphic Display Time:** Graphics containing up to 20 dynamic data points shall display in ≤5 seconds
- **Graphic Update Rate:** Dynamic values on displayed graphics shall update in ≤8 seconds after field value change
- **Navigation Responsiveness:** Navigation between graphics, menus, or system views shall complete in ≤3 seconds
- **Large Graphic Performance:** Complex graphics (50+ dynamic points) shall display in ≤10 seconds

These criteria shall be measured on the minimum specified workstation hardware and under normal network loading conditions.

### 5.4.2 Alarm Annunciation Performance

The alarm and event notification system shall meet the following criteria:

- **Alarm Display Latency:** Critical alarms shall appear in the supervisory interface within ≤15 seconds of the triggering condition
- **Alarm Notification Delivery:** Email/SMS alarm notifications shall be delivered within ≤60 seconds (subject to external email system performance)
- **Alarm Acknowledgment:** Operator alarm acknowledgment shall register in the system within ≤3 seconds
- **Alarm History Retrieval:** Alarm history queries shall return results within ≤10 seconds for typical date ranges (30 days)

### 5.4.3 Trend Data Retrieval

Historical trend data access shall meet the following performance requirements:

- **Real-time Trend Display:** Current trend data (last 24 hours) shall display in ≤5 seconds
- **Historical Trend Queries:** Historical trend retrieval (30-day range) shall complete in ≤15 seconds
- **Trend Data Export:** Export of trend data to CSV/Excel shall complete in ≤30 seconds for up to 10 points over 30 days
- **Multi-point Trending:** Displaying overlay trends of up to 10 points shall complete in ≤10 seconds

### 5.4.4 Data Query and Reporting

System data queries and report generation shall meet performance requirements:

- **Point Search:** Searching for points by name or tag shall return results in ≤3 seconds for typical queries
- **Equipment Lists:** Displaying equipment lists filtered by type or location shall complete in ≤5 seconds
- **Custom Reports:** Standard operational reports (runtime summaries, alarm summaries, setpoint schedules) shall generate in ≤30 seconds
- **Energy Dashboards:** Energy monitoring dashboards with multiple meters and graphics shall load in ≤10 seconds

### 5.4.5 Mobile and Remote Access

Where mobile or remote access is provided, performance shall be validated:

- **Mobile App Performance:** Mobile applications shall meet the same graphic display and navigation performance as workstation interfaces (±2 seconds acceptable variance)
- **VPN Access Performance:** Performance over VPN shall degrade by no more than 20% compared to local network access
- **Web Browser Performance:** Web-based interfaces shall meet all performance criteria when accessed via supported browsers

### 5.4.6 Concurrent User Performance

System performance shall be validated under concurrent user load:

- **Multiple Users:** System shall maintain performance standards with up to the maximum specified concurrent users
- **Performance Degradation Limit:** With maximum concurrent users, performance degradation shall not exceed 25% of single-user benchmarks
- **Load Testing:** System shall be tested at 125% of maximum concurrent users to verify graceful degradation

### 5.4.7 API and Integration Performance

Where programmatic data access is provided via APIs:

- **API Response Time:** REST API calls shall return data within ≤2 seconds for typical point queries
- **Bulk Data Retrieval:** API requests for bulk data (100+ points) shall complete within ≤10 seconds
- **API Availability:** API endpoints shall maintain ≥99.5% availability during normal operations
- **Rate Limiting:** API rate limits shall be documented and sufficient for intended applications (minimum 60 requests/minute recommended)

## Examples

### Example 1: Graphics Performance Validation

**Scenario:** Testing GUI performance for HVAC graphics with 20 dynamic points.

**Test Procedure:**
1. Clear browser cache and restart supervisory workstation
2. Start timer and navigate to complex AHU graphic (20 dynamic points: temperatures, status, setpoints)
3. Record time until graphic fully displays with all values populated
4. Change field setpoint and measure time until graphic updates
5. Navigate to different graphic and measure transition time
6. Repeat test 3 times and average results

**Acceptance:**
- Graphic display: ≤5 seconds (tested: 3.2 seconds average) ✓
- Value update: ≤8 seconds (tested: 5.1 seconds average) ✓
- Navigation: ≤3 seconds (tested: 1.8 seconds average) ✓

**Result:** GUI performance meets all specified criteria.

### Example 2: Alarm Annunciation Testing

**Scenario:** Validating critical alarm notification performance.

**Test Procedure:**
1. Configure test point with critical alarm (high temperature)
2. Start timer and force point into alarm condition
3. Measure time until alarm appears in supervisory interface
4. Record time until email notification received
5. Acknowledge alarm and measure acknowledgment response time
6. Query alarm history for last 30 days and measure retrieval time

**Results:**
- Alarm display latency: 8 seconds (meets ≤15 second requirement) ✓
- Email notification: 22 seconds (meets ≤60 second requirement) ✓
- Acknowledgment response: <1 second (meets ≤3 second requirement) ✓
- History retrieval (30 days): 6 seconds (meets ≤10 second requirement) ✓

**Result:** Alarm system performance verified; operators receive timely notifications.

### Example 3: Concurrent User Load Testing

**Scenario:** Validating system performance with multiple simultaneous users.

**Test Setup:**
- System specified for 10 concurrent users
- Baseline single-user performance established
- 12 users simultaneously access system (125% of maximum)

**Test Activities:**
- All users navigate to different graphics simultaneously
- Multiple users query trend data
- Several users acknowledge alarms
- Some users generate reports

**Performance Results:**
- Single-user graphic display: 3.5 seconds
- 12 concurrent users graphic display: 4.8 seconds (37% degradation - FAILS)

**Corrective Action:**
- Database query optimization implemented
- Graphics caching enabled
- Re-test shows 12-user performance: 4.2 seconds (20% degradation - PASSES)

**Result:** System maintains acceptable performance under peak load after optimization.

## Verification

### Graphics Performance Testing

- **Objective:** Verify graphical interface meets response time requirements
- **Method:**
  - Test graphic display time for standard and complex graphics
  - Measure dynamic value update rates
  - Validate navigation responsiveness
  - Test under minimum specified hardware configuration
- **Acceptance Criteria:** All graphics meet specified display and update time requirements

### Alarm System Performance Validation

- **Objective:** Verify alarm annunciation meets latency requirements
- **Method:**
  - Force alarm conditions and measure display latency
  - Test notification delivery times (email, SMS)
  - Measure alarm acknowledgment response
  - Validate alarm history query performance
- **Acceptance Criteria:** All alarm functions meet specified time requirements

### Trend Data Performance Testing

- **Objective:** Verify trend data retrieval meets performance criteria
- **Method:**
  - Display real-time trends and measure load time
  - Query historical data ranges and measure retrieval time
  - Test trend data export performance
  - Validate multi-point overlay trend performance
- **Acceptance Criteria:** Trend access and export meet all specified time requirements

### Report and Query Performance

- **Objective:** Verify data query and reporting performance
- **Method:**
  - Test point search response times
  - Measure equipment list display times
  - Generate standard reports and measure completion time
  - Load energy dashboards and measure display time
- **Acceptance Criteria:** All queries and reports complete within specified times

### Concurrent User Load Testing

- **Objective:** Verify system performance under multi-user load
- **Method:**
  - Establish single-user performance baseline
  - Test with maximum specified concurrent users
  - Test at 125% of maximum users
  - Measure performance degradation percentage
  - Verify graceful degradation (no crashes)
- **Acceptance Criteria:** Performance degradation ≤25% at maximum users; system remains stable at 125% load

### Mobile and Remote Access Validation

- **Objective:** Verify mobile and VPN access meet performance requirements
- **Method:**
  - Test mobile app performance against workstation baseline
  - Measure VPN access performance degradation
  - Test web browser interface performance
  - Validate across supported devices and browsers
- **Acceptance Criteria:** Mobile/remote performance within acceptable variance of local access

### API Performance Testing

- **Objective:** Verify programmatic data access meets performance requirements
- **Method:**
  - Test API response times for typical queries
  - Measure bulk data retrieval performance
  - Monitor API availability over test period
  - Validate rate limiting configuration
- **Acceptance Criteria:** API calls meet response time requirements; availability ≥99.5%; rate limits documented and adequate

### Required Deliverables

- [ ] GUI performance test results with screenshots and timing data
- [ ] Alarm annunciation performance validation report
- [ ] Trend data retrieval performance test results
- [ ] Concurrent user load testing report with baseline and multi-user results
- [ ] Mobile/remote access performance validation
- [ ] API performance and availability test results
- [ ] Performance optimization documentation (if corrective actions required)

### Acceptance Criteria

Data accessibility and performance validation is complete when all graphical interface, alarm, trend, query, and API performance requirements are met under both single-user and maximum concurrent user loads, with mobile and remote access validated where applicable.

---

*This document is part of the Digital Commissioning of Building Automation Systems Standard, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*
