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