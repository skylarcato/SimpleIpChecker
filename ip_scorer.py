import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("ABUSEIPDB_API_KEY")

# Base URL for AbuseIPDB
BASE_URL = "https://api.abuseipdb.com/api/v2/check"

def check_ip(ip):
    headers = {
        'Key': API_KEY,
        'Accept': 'application/json'
    }
    params = {
        'ipAddress': ip,
        'maxAgeInDays': '90'
    }

    response = requests.get(BASE_URL, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()['data']
        print(f"\n[+] IP: {data['ipAddress']}")
        print(f"    Abuse Score: {data['abuseConfidenceScore']}/100")
        print(f"    Country: {data['countryCode']}")
        print(f"    Domain: {data['domain']}")
        print(f"    Total Reports: {data['totalReports']}")
        print(f"    Last Reported: {data['lastReportedAt']}")
    else:
        print(f"\n[!] Error checking IP {ip}: {response.status_code}")
        print(response.text)

def main():
    ip = input("Enter an IP address to check: ")
    check_ip(ip)

if __name__ == "__main__":
    main()
