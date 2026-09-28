log_file = "sample_log.txt"
report_file = "alerts.txt"
failed_count = 0
failures_by_ip = {}
alert_threshold = 3

with open(log_file, "r") as file:
    for line in file:
        if "Failed login attempt" in line:
            failed_count += 1
            ip_address = line.strip().split()[-1]
            failures_by_ip[ip_address] = failures_by_ip.get(ip_address, 0) + 1

print(f"Total failed login attempts: {failed_count}")
print("Failed attempts by IP:")

with open(report_file, "w") as report:
    for ip_address, count in failures_by_ip.items():
        print(f"{ip_address}: {count}")

        if count >= alert_threshold:
            alert = f"ALERT: {ip_address} had {count} failed login attempts"
            print(alert)
            report.write(alert + "\n")