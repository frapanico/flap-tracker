# FLAP – Flight Location and Proximity (v0.1.0-alpha)
<p align="center">
  <img src="https://github.com/user-attachments/assets/09642846-f054-4c46-a0a3-b563a2289ee1" alt="FLAP – Flight Location and Proximity" />
  <br/>
  <em></em>
</p>

A lightweight Python script that connects to the [OpenSky Network](https://opensky-network.org/) API to retrieve and display real-time information about the closest aircraft to a specified location (Rome, Italy by default), including its callsign, distance, altitude, and speed. This script is designed to be used with [SwiftBar](https://github.com/swiftbar/SwiftBar) to display real-time information in the Mac menu bar. However, it can also be run from the terminal if needed.


## Example output
For the example output below, the line with the three dashes `"---"` has been removed (see the **Using with SwiftBar** section,  the script is designed to work with SwiftBar, which requires this formatting). However, if you want to run it from the terminal instead, you can simply remove the `"---"` line, and the output will look like this:

```python
✈️ AEE123 5.6 km
12:45:17 Alt: 11250 m | Vel: 250 m/s
```

## Requirements
- Python 3.7+
- `requests`
- `geopy`

## Authentication 
This script uses client credentials (OAuth2) to authenticate with OpenSky. To obtain your own `clientId` and `clientSecret`:
1. Create a free account at https://opensky-network.org.
2. Once logged in, go to your user dashboard and create an API application.
3. Download the `credentials.json` file provided.
4. Inside that file, you'll find your personal `clientId` and `clientSecret`.
5. Replace the placeholders `your-client-id` and `your-client-secret` on lines 9 and 10 of the script with your own credentials.

## Using with SwiftBar
SwiftBar lets you run scripts and display their output right in your Mac’s menu bar. You can integrate this Python script to show the nearest flight info live.
The script is already named `nearest_flight.1s.py` to follow SwiftBar’s naming convention, since it was designed for use with SwiftBar. The `1s` in the filename means SwiftBar will refresh the output every minute. Adjust as you prefer (5m, 30s, etc.). This way, you get real-time nearest flight info in your Mac menu bar, refreshing automatically.
Make sure your script is executable running:
```terminal
chmod +x nearest_flight.1s.py
```
SwiftBar expects the first line of output to be the menu bar text, followed by menu items separated by lines with `"---"`. These separators are already included by default in the script. It may print:
```python
✈️ AEE123 5.6 km
---
12:45:17 Alt: 11250 m | Vel: 250 m/s
```
At this point, copy the script into your SwiftBar plugins folder, usually located at `~/Documents/SwiftBarPlugins` but this path can vary depending on your SwiftBar installation or macOS version. You can check or change the plugins directory in SwiftBar’s preferences.

## Command Line Usage
You can also run the script from your terminal:
```terminal
python nearest_flight.1s.py
```

## Known Limitations
This script relies on the OpenSky Network API, which has some constraints:
- **Token Expiry:** The OAuth token expires after a short period (usually 1 hour). After that, you'll need to request a new one.
- **Rate Limits:** OpenSky enforces request limits, especially for non-commercial users. If you exceed the limit, you may receive empty data or errors.
- **Limited Uptime:** The OpenSky API may not provide full availability or complete data throughout the day. This is normal behavior for free-tier access.

If the script works for a while and then stops, it's most likely due to one of these limitations. Feel free to share issues, suggestions, or improvements. Your feedback is highly appreciated!


