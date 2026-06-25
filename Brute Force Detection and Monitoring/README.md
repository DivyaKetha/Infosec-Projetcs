# 🚨 Brute Force Detection & Monitoring (Splunk)

## 📌 Overview

This project focuses on detecting and analyzing brute-force login attempts using Splunk. It simulates real-world SOC monitoring by identifying suspicious login patterns and visualizing attack sources globally.

---

## 🔧 Tools Used

* Splunk
* SPL (Search Processing Language)

---

## 🔍 Key Features

* Detection of failed SSH login attempts
* Extraction of attacker IPs using regex
* Geo-location mapping of attackers
* Dashboard visualization for SOC monitoring

---

## 📊 SPL Queries

### Extract IP + Enrich Location

```spl
index=main "Failed password"
| rex "from (?<ip>\d+\.\d+\.\d+\.\d+)"
| iplocation ip
```

### Top Attacking IPs

```spl
| stats count as attempts by ip Country lat lon
| sort -attempts
```

### Geo Map Visualization

```spl
| where isnotnull(lat) AND isnotnull(lon)
| geostats count latfield=lat longfield=lon
```

---

## 📈 Insights

* Detected 900+ brute-force login attempts
* Identified repeated attacks from specific IP addresses
* Observed attack traffic from multiple countries
* Differentiated between aggregated data (`stats`) and raw event visualization (`geostats`)

---

## 🎯 Outcome

This project demonstrates practical SOC analyst skills including log analysis, threat detection, and security visualization using Splunk.



