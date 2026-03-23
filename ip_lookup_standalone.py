#!/usr/bin/env python3
import argparse
import json
import os
import socket
import sys
import urllib.parse
import urllib.request


def http_get_json(url: str, headers: dict | None = None) -> dict:
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))

def normalize_indicator(indicator: str) -> tuple[str, str]:
    if "://" in indicator:
        parsed = urllib.parse.urlparse(indicator)
        host = parsed.hostname or indicator
        return "url", host
    return "ip", indicator

def reverse_dns(ip: str) -> str | None:
    try:
        host, _, _ = socket.gethostbyaddr(ip)
        return host
    except Exception:
        return None

def resolve_hostname(host: str) -> str:
    return socket.gethostbyname(host)

def geo_lookup(ip: str) -> dict:
    return http_get_json(f"https://ipwho.is/{urllib.parse.quote(ip)}")


def abuse_lookup(ip: str) -> dict | None:
    api_key = os.environ.get("ABUSEIPDB_KEY")
    if not api_key:
        return None
    url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={urllib.parse.quote(ip)}&maxAgeInDays=90"
    data = http_get_json(url, headers={"Key": api_key, "Accept": "application/json"})
    return data.get("data")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("indicator")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--abuse", action="store_true")
    args = parser.parse_args()

    kind, ip = normalize_indicator(args.indicator)
    if kind == "url":
        ip = resolve_hostname(ip)    

    result = {
        "ip": ip,
        "geo": geo_lookup(ip),
        "ptr": reverse_dns(ip),
    }

    if args.abuse:
        result["abuse"] = abuse_lookup(ip)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"IP: {ip}")
        print(f"PTR: {result['ptr']}")
        print(f"Country: {result['geo'].get('country')}")
        print(f"City: {result['geo'].get('city')}")
        print(f"Org: {result['geo'].get('connection', {}).get('org')}")
        print(f"ASN: {result['geo'].get('connection', {}).get('asn')}")
        if "abuse" in result and result["abuse"]:
            print(f"Abuse Score: {result['abuse'].get('abuseConfidenceScore')}")
            print(f"Reports: {result['abuse'].get('totalReports')}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())