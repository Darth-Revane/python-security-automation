\# Python Security Automation Portfolio



Three Python tools for practicing security automation: a log parser, a local port scanner and an IOC lookup tool.



\## Tools



\- \*\*Security Log Parser:\*\* Counts failed login attempts by source IP and writes alerts when an IP reaches three failures.

\- \*\*Port Scanner:\*\* Checks selected TCP ports on `127.0.0.1`, the local computer.

\- \*\*IOC Lookup Tool:\*\* Checks a public IP address or SHA-256 file hash using the VirusTotal API.



These tools are learning projects. The log parser uses sample data and the scanner is configured for localhost.





\## Run the tools



Use Python 3 and run these commands from the main project folder.



\### Log parser



```powershell

cd log-parser

python log\_parser.py

```



The parser reads `sample\_log.txt` and writes detected alerts to `alerts.txt`.



\### Port scanner



```powershell

cd port-scanner

python port\_scanner.py

```



The scanner checks the configured ports on your own computer (`127.0.0.1`). Only scan systems you own or have permission to scan.



\### IOC lookup



```powershell

cd ioc-lookup

python ioc\_lookup.py

```



Enter a public IP address or a SHA-256 hash when prompted. You’ll also need a VirusTotal API key. Enter the key at the prompt; \*\*do not put it in the code or upload it to GitHub\*\*.

