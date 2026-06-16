# 🧠 Brute Force Detection & SOC Monitoring – Full Project Explanation

## 📌 Step 1: Data Ingestion

I started by ingesting authentication logs into Splunk. These logs contained SSH login activity, including successful and failed login attempts.

---

## 📌 Step 2: Detect Failed Login Attempts

To identify brute-force activity, I searched for failed login attempts using:

```spl id="y9k7te"
index=main "Failed password"
```

This allowed me to isolate suspicious login failures.

---

## 📌 Step 3: Extract Attacker IP Addresses

The logs contained IP addresses within raw text. I extracted them using regex:

```spl id="dpm9hw"
| rex "from (?<ip>\d+\.\d+\.\d+\.\d+)"
```

This created a structured `ip` field for analysis.

---

## 📌 Step 4: Enrich Data with Geolocation

To understand where attacks were coming from, I enriched the data:

```spl id="b0pfm6"
| iplocation ip
```

This added:

* Country
* Latitude
* Longitude

---

## 📌 Step 5: Remove Noise & Prepare Data

I filtered out invalid geographic data:

```spl id="lrdkso"
| where isnotnull(lat) AND isnotnull(lon)
```

---

## 📌 Step 6: Analyze Attack Patterns

### 🔹 Aggregated Analysis (Top Attackers)

```spl id="z9rfu7"
| stats count as attempts by ip Country lat lon
| sort -attempts
```

This helped identify:

* Most active attacker IPs
* Number of attempts per attacker

---

### 🔹 Event-Level Visualization (Geo Map)

```spl id="kp4b0m"
| geostats count latfield=lat longfield=lon
```

This displayed:

* Attack density on world map
* Total attack events (~900+)

---

## 📌 Step 7: Dashboard Creation

I created a Splunk dashboard with multiple panels:

### 📊 Panels:

* Top Attacking IPs (Bar chart)
* Most Targeted Users(Bar chart)
* Attack Timeline (Line chart)
* Attack Map (Global attacks)
* Threat Level(Tables)
* Attack Count Visualization(Total Attacks Count)
* IP locations of Attacks

---

## 📌 Step 8: Drilldowns (Advanced Feature)

To simulate SOC investigation workflows, I implemented drilldowns:

* Clicking an IP → shows related logs
* Clicking a country → filters attack logs
* Clicking a time spike → shows events at that time

This transforms the dashboard into an **interactive investigation tool**.

For Dashoard Drilldown search strings: Find them in "Drilldown Strings.txt"  

---

## 📌 Step 9: Key Learnings

* Difference between:

  * `stats` (aggregated data)
  * `geostats` (event-level data)
* Importance of log parsing using regex
* Real-world SOC workflow:

  * Detect → Analyze → Investigate

---

## 🎯 Final Outcome

This project simulates a real SOC use case where brute-force attacks are detected, analyzed, and investigated using Splunk dashboards.

It demonstrates practical skills in:

* Log analysis
* Threat detection
* Data visualization
* Security monitoring
