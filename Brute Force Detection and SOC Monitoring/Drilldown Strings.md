''' FOR TOP ATTACKING IPS DASHBOARD '''
index=main "Failed password" | rex "from (?<ip>\d+\.\d+\.\d+\.\d+)" | search ip=$row.ip$

''' FOR MOST TARGETED USERS DASHBOARD '''
index=main "Failed password"
| rex "Failed password for (?:invalid user )?(?<user>\w+)"
| search user=$row.user$

''' FOR ATTACK TIMELINE DASHBOARD '''
index=main "Failed password" | bin _time span=1m | search _time=$click.value$

''' FOR THREAT LEVEL DASHBOARD '''
index=main "Failed password"
| rex "from (?<ip>\d+\.\d+\.\d+\.\d+)"
| search ip=$ip.value$

''' FOR TOTAL ATTACKS DASHBOARD '''
index=main "Failed password"

''' FOR ATTACKS PER IP WITH LOCATIONS DASHBOARD '''
index=main "Failed password"
| rex "from (?<ip>\d+\.\d+\.\d+\.\d+)"
| search ip=$ip.value$ MAKE IT MD TEXT bold heading make queries as code
