# SOC Alert Triage & Incident Response Center

## Overview

A Splunk-based security dashboard for monitoring failed authentication attempts, detecting brute force attacks, and tracking IP reputation with automated blocklist integration. Designed for SOC analysts to quickly triage and investigate high-risk threats.

---

## Dashboard Components

### 1. Critical Alerts
Single-value panel showing total failed login attempts within the selected time range. Provides an immediate health indicator for authentication systems.

---

### 2. Attack Timeline
Line chart visualizing failed login frequency over time. Use this to identify attack patterns, spikes, and anomalous behavior.

---

### 3. Top Attacker's IPs
Bar chart ranking source IPs by failed attempt count. Quickly identifies the most active threat actors.

---

### 4. Attack Map
Geographic visualization showing attack origin countries. Uses MaxMind GeoIP database for IP-to-location mapping.

---

### 5. Brute Force Detection
Stacked bar chart comparing failed vs successful login attempts per IP. Critical for identifying compromised accounts where attackers eventually gained access.

---

### 6. Risk Scoring
Color-coded table assigning risk levels based on attempt thresholds:

| Attempts | Risk Level |
|----------|------------|
| >50 | Critical |
| >20 | High  |
| >10 | Medium |
| ≤10 | Low  |

---

### 7. IP Blocking Status
Table showing whether attacking IPs are currently blocked, with lookup against a CSV blocklist.

---

### 8. Investigation Panel
Detailed event table with timestamps, hosts, usernames, and source IPs. Used for incident analysis and evidence collection.

---

### 9. Active Alerts
Table of unresolved alerts from Splunk's alerting framework. Serves as the analyst's work queue.

---

## Data Extraction

### Regex Patterns

| Field | Pattern |
|-------|---------|
| Source IP | `from (?<ip>\d+\.\d+\.\d+\.\d+)` |
| Username | `for (?:invalid user )?(?<user>\w+)` |

### IP Blocklist
External CSV lookup `blocked_ips.csv` with single column `ip`. Used for status enrichment.

---

## Drilldown Actions

All tables include drilldown links to:
- Open searches in new tab
- Auto-populate time ranges
- Filter to specific IPs or users

---

## Use Cases

| Scenario | Workflow |
|----------|----------|
| **Triage** | Start with Critical Alerts → Review Top Attackers → Block Active IPs |
| **Investigation** | Select IP → View Investigation Panel → Check Brute Force metrics |
| **Compromise Assessment** | Brute Force Detection → Identify successful breaches → Reset compromised accounts |
| **Threat Hunting** | Attack Timeline → Identify patterns → Correlate with Attack Map |
| **Reporting** | Risk Scoring → Export findings → Document for compliance |

---

## Dependencies

- **Splunk Cloud
- **MaxMind GeoIP** database for iplocation command
- **blocked_ips.csv** in lookup directory
- **Splunk REST API** for fired alerts

---

## Customization

### Adjust Risk Thresholds
Modify the case statement in the Risk Scoring search:
```spl
eval risk_level = case(attempts > YOUR_HIGH, "Critical", ...)
```

### Modify Blocklist
Update `blocked_ips.csv` with new IPs to mark as blocked.

### Change Time Range Default
Set `defaultValue` in input_global_trp options.




