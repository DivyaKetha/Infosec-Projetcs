-- Top Attacking IPs
index=main "Failed password" | rex "from (?<ip>\d+\.\d+\.\d+\.\d+)" | search ip=$row.ip$

-- Most Targeted Users
index=main "Failed password" | rex "Failed password for (?:invalid user )?(?<user>\w+)" | search user=$row.user$

-- Attack Timeline
index=main "Failed password" | bin _time span=1m | search _time=$click.value$

-- Threat Level
index=main "Failed password" | rex "from (?<ip>\d+\.\d+\.\d+\.\d+)" | search ip=$ip.value$

-- Total Attacks
index=main "Failed password"

-- Attacks Per IP with Locations
index=main "Failed password" | rex "from (?<ip>\d+\.\d+\.\d+\.\d+)" | search ip=$ip.value$
