file = open("../logs/sample.log", "r")

ip_count = {}

for line in file:
    if "Failed password" in line:
        parts = line.split(" ")
        ip = parts[-1].strip()

        if ip in ip_count:
            ip_count[ip] += 1
        else:
            ip_count[ip] = 1

file.close()

print("\nFailed Login Attempts per IP:\n")

for ip, count in ip_count.items():
    print(f"{ip} → {count} attempts")

print("\nSuspicious Activity:\n")

for ip, count in ip_count.items():
    if count >= 3:
        print(f"ALERT: {ip} is suspicious with {count} attempts")


        
