\# SOC Triage Tool



A lightweight standalone Python tool for quick IP enrichment and threat triage.



\## Features



\- Reverse DNS lookup

\- Geolocation lookup

\- Organization / ASN lookup

\- AbuseIPDB enrichment



\## Requirements



\- Python 3

\- AbuseIPDB API key (optional, for `--abuse`)



\## Usage



```powershell

py ip\_lookup\_standalone.py 8.8.8.8

py ip\_lookup\_standalone.py 8.8.8.8 --abuse

py ip\_lookup\_standalone.py 8.8.8.8 --json

