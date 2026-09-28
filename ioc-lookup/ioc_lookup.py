import ipaddress
import json
import re
from getpass import getpass
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

indicator = input("Enter a public IP address or SHA-256 hash: ").strip()

try:
    ip_address = ipaddress.ip_address(indicator)
except ValueError:
    if re.fullmatch(r"[0-9a-fA-F]{64}", indicator):
        indicator_type = "SHA-256 hash"
        url = f"https://www.virustotal.com/api/v3/files/{indicator}"
    else:
        print("Enter a valid public IP address or 64-character SHA-256 hash.")
        raise SystemExit(1)
else:
    if not ip_address.is_global:
        print("Please enter a public IP address.")
        raise SystemExit(1)

    indicator_type = "IP address"
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_address}"

api_key = getpass("Paste your VirusTotal API key: ")
request = Request(url, headers={"x-apikey": api_key})

try:
    with urlopen(request, timeout=15) as response:
        data = json.load(response)
except HTTPError as error:
    if error.code == 404:
        print("VirusTotal has no report for this indicator.")
    else:
        print(f"VirusTotal returned HTTP {error.code}.")
except URLError as error:
    print(f"Could not connect to VirusTotal: {error.reason}")
else:
    stats = data["data"]["attributes"]["last_analysis_stats"]
    print(f"{indicator_type}: {indicator}")
    print(f"Malicious detections: {stats.get('malicious', 0)}")
    print(f"Suspicious detections: {stats.get('suspicious', 0)}")
    print(f"Harmless detections: {stats.get('harmless', 0)}")
    print(f"Undetected: {stats.get('undetected', 0)}")