# FLAP – Flight Location and Proximity (v0.1.0-alpha)
This is a lightweight Python script that connects to the [OpenSky Network](https://opensky-network.org/) API to display the nearest aircraft to a specific location (Rome, Italy by default). This script is designed to be used with SwiftBar to display real-time information in the Mac menu bar. However, it can also be run from the terminal if needed.

## Example output
```python
✈️ AEE123 5.6 km
12:45:17 Alt: 11250 m | Vel: 250 m/s
```

## Authentication 
This script uses client credentials (OAuth2) to authenticate with OpenSky. To obtain your own `clientId` and `clientSecret`:
1. Create a free account at https://opensky-network.org.
2. Once logged in, go to your user dashboard and create an API application.
3. Download the `credentials.json` file provided.
4. Inside that file, you'll find your personal `clientId` and `clientSecret`.

## Command Line Usage
You can also run the script from your terminal:
```python
python nearest_flight.1s.py
```

## Using with SwiftBar
[SwiftBar](https://github.com/swiftbar/SwiftBar) lets you run scripts and display their output right in your Mac’s menu bar. You can integrate this Python script to show the nearest flight info live.
The script is already named `nearest_flight.1m.py` to follow SwiftBar’s naming convention, since it was designed for use with SwiftBar. The `1m` in the filename means SwiftBar will refresh the output every minute. Adjust as you prefer (5m, 30s, etc.). This way, you get real-time nearest flight info in your Mac menu bar, refreshing automatically.
Make sure your script is executable running:
```terminal
chmod +x nearest_flight.1s.py
```
SwiftBar expects the first line of output to be the menu bar text, followed by menu items separated by lines with `"---"`. The script may print:
```python
✈️ AEE123 5.6 km
---
12:45:17 Alt: 11250 m | Vel: 250 m/s
```
At this point, copy the script into your SwiftBar plugins folder, usually located at `~/Documents/SwiftBarPlugins` but this path can vary depending on your SwiftBar installation or macOS version. You can check or change the plugins directory in SwiftBar’s preferences.

## Known Limitations
This script relies on the OpenSky Network API, which has some constraints:
- **Token Expiry:** The OAuth token expires after a short period (usually 1 hour). After that, you'll need to request a new one.
- **Rate Limits:** OpenSky enforces request limits, especially for non-commercial users. If you exceed the limit, you may receive empty data or errors.
- **Limited Uptime:** The OpenSky API may not provide full availability or complete data throughout the day. This is normal behavior for free-tier access.

If the script works for a while and then stops, it's most likely due to one of these limitations. Feel free to share issues, suggestions, or improvements.Your feedback is highly appreciated!



## Requirements
- Python 3.7+
- `requests`
- `geopy`

