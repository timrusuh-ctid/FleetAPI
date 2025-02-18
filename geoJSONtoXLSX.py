import json
import pandas as pd
import datetime
now = datetime.datetime.now().strftime('%Y%m%d')

# Load JSON file
with open('D:/New/Geofence/BAHA00004/BEKASI/BEKASI/WADMKC_Babelan.geojson', 'r') as f:
    data = json.load(f)

# Prepare data for DataFrame
time = now + '01'
rows = []
geofenceName = data['name']
for feature in data['features']:
    geofence_name = geofenceName
    geofence_description = 'Geofence Testing'
    
    # Extract and format coordinates
    coordinates = feature['geometry']['coordinates']
    formatted_points = []
    for multi_polygon in coordinates:
        for polygon in multi_polygon:
            for point in polygon:
                lat, long = point[1], point[0]  # Swap to LAT#LONG format
                formatted_points.append(f'{lat}#{long}')
    
    points = '#'.join(formatted_points)
    
    # Append row data
    rows.append([geofence_name, geofence_description, points, '', ''])

# Create DataFrame
df = pd.DataFrame(rows, columns=['Geofence Name', 'Geofence Description', 'Point(Lat#Lon#Lat#Lon...)', 'Group Name', 'Group Description'])

# Save to Excel
fileName = f'D:/New/Geofence/{geofenceName}-{time}.csv'
df.to_csv(fileName, index=False)

print(f"Excel file has been created: {fileName}")
