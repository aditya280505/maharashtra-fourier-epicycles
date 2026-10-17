import json
import requests

URL = (
    "https://cdn.jsdelivr.net/gh/"
    "udit-001/india-maps-data@main/"
    "geojson/states/maharashtra.geojson"
)

print("Downloading Maharashtra boundary...")

response = requests.get(URL, timeout=60)
response.raise_for_status()

data = response.json()

with open("maharashtra.geojson", "w", encoding="utf-8") as f:
    json.dump(data, f)

print("Maharashtra boundary downloaded successfully!")
print("Saved as: maharashtra.geojson")
print("GeoJSON type:", data.get("type"))