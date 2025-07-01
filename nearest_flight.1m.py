#!/usr/bin/env python3
import requests
from geopy.distance import geodesic
from datetime import datetime

USER_LOCATION = (41.902782, 12.496366)  # Rome

# Replace your-client-id and your-client-secret with your own credentials found in the credentials.json file
CLIENT_ID = "your-client-id"
CLIENT_SECRET = "your-client-secret"

def get_access_token():
    url = "https://auth.opensky-network.org/auth/realms/opensky-network/protocol/openid-connect/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    token = response.json()['access_token']
    return token

def get_nearest(token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get("https://opensky-network.org/api/states/all", headers=headers, timeout=10)
    response.raise_for_status()
    data = response.json()

    flights = []
    for s in data.get("states", []):
        if s[5] is None or s[6] is None:
            continue
        pos, dist = (s[6], s[5]), geodesic(USER_LOCATION, (s[6], s[5])).km
        flights.append({
            "callsign": s[1].strip() if s[1] else "N/A",
            "dist": round(dist, 1),
            "alt": round(s[13] or 0),
            "vel": round(s[9] or 0)
        })
    return min(flights, key=lambda f: f["dist"]) if flights else None

def main():
    try:
        token = get_access_token()
    except Exception as e:
        print("✈️ Error obtaining OAuth token")
        print(str(e))
        return

    try:
        f = get_nearest(token)
    except Exception as e:
        print("✈️ Error calling flight API")
        print(str(e))
        return

    if f:
        header = f"✈️ {f['callsign']} {f['dist']} km"
        body = f"Alt: {f['alt']} m | Vel: {f['vel']} m/s"
    else:
        header = "✈️ No flight found"
        body = ""

    print(header)
    print("---")
    print(f"{datetime.now().strftime('%H:%M:%S')} {body}")

if __name__ == "__main__":
    main()
