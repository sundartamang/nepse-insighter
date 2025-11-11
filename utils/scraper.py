import requests

def fetch_nepse_companies():
    url = "https://backend.nepalstock.com/api/nots/company/list"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://www.nepalstock.com",
        "Referer": "https://www.nepalstock.com/",
    }

    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()  # raises exception if bad response

    data = response.json()
    companies = data.get("data", [])

    print(f"✅ Total companies fetched: {len(companies)}")
    for c in companies[:10]:  # print first 10
        print(f"{c['symbol']} - {c['company_name']}")
