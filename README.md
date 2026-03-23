# SOC Triage Tool

Lightweight Python tool for rapid SOC triage and IP enrichment using threat intelligence sources (AbuseIPDB, geolocation, reverse DNS).

---

## 🚀 Features

- Reverse DNS lookup (PTR)
- Geolocation (country, city)
- Organization and ASN lookup
- AbuseIPDB reputation scoring
- JSON output option for automation

---

## 📦 Requirements

- Python 3
- Internet access
- AbuseIPDB API key (optional)

---

## ⚙️ Setup

Clone the repo:

```bash
git clone https://github.com/mccoy6038/soc-triage-tool.git
cd soc-triage-tool

$env:ABUSEIPDB_KEY="your_api_key"

## Usage 
py ip_lookup_standalone.py 8.8.8.8
py ip_lookup_standalone.py 8.8.8.8 --abuse
py ip_lookup_standalone.py 8.8.8.8 --json

## Example Output
IP: 8.8.8.8
PTR: dns.google
Country: United States
City: Mountain View
Org: Google LLC
ASN: 15169
Abuse Score: 0
Reports: 8

## Use Cases
SOC alert triage
Investigating suspicious IPs
Enriching SIEM alerts
Threat hunting

## Notes:
ASN/Org data depends on external API accuracy
AbuseIPDB requires an API key for reputation scoring

## Roadmap
URL analysis (VirusTotal)
 IOC extraction from logs
 Batch processing
 Risk scoring improvements



