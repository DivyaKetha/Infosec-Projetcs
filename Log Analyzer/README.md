# Log Analyzer - Failed Login Detection

A lightweight Python tool for analyzing system logs to detect failed login attempts and identify potential brute-force attacks.

---

## 📋 Overview

This tool parses authentication logs to track failed login attempts, counts occurrences per IP address, and flags suspicious activity based on configurable thresholds. Designed for quick security assessments and incident response.

---

## ✨ Features

- **Failed Login Detection** - Parses log files for "Failed password" entries
- **IP-based Tracking** - Counts failed attempts per source IP address
- **Threshold Alerting** - Flags IPs exceeding configurable attempt limits
- **Lightweight & Fast** - Pure Python with no external dependencies
- **Simple Output** - Clear, readable console output for rapid analysis

---

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- Log file in standard authentication format

---

## 📊 Sample Output

```
Failed Login Attempts per IP:

192.168.1.105 → 5 attempts
10.0.0.23 → 12 attempts
203.0.113.42 → 2 attempts
172.16.0.89 → 8 attempts

Suspicious Activity:

ALERT: 192.168.1.105 is suspicious with 5 attempts
ALERT: 10.0.0.23 is suspicious with 12 attempts
ALERT: 172.16.0.89 is suspicious with 8 attempts
```

---

## 🛠 Configuration

### Adjusting the Alert Threshold

Modify the threshold value in the script:


### Supported Log Formats

Currently supports logs where:
- Failed login entries contain "Failed password"
- Source IP appears as the last field in the log entry

Example log format:
```
Feb 24 10:15:32 server sshd[1234]: Failed password for root from 192.168.1.105 port 54321 ssh2
```

---

## 🎯 Use Cases

| Use Case | Benefit |
|----------|---------|
| **SOC Analysis** | Quickly identify compromised credentials |
| **Incident Response** | Rapid triage of ongoing attacks |
| **Security Auditing** | Review historical attack patterns |
| **Training** | Learn log analysis fundamentals |

---

## ⚠️ Limitations & Future Improvements

**Current Limitations:**
- Hardcoded log path (modify manually for different files)
- Assumes specific log format
- No real-time monitoring capabilities
- Command-line arguments not fully implemented

---

## 🙏 Acknowledgments

- Inspired by common cybersecurity use cases in SOC environments
- Built for educational and practical security analysis

---

*Last Updated: June 2026*
