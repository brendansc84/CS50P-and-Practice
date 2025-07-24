from fastkml import kml
from shapely.geometry import shape, Point
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import pandas as pd

# 1. Load KML polygons
def load_kml_polygons(kml_file):
    with open(kml_file, 'rt') as f:
        doc = f.read()
    k = kml.KML()
    k.from_string(doc.encode('utf-8'))
    polygons = []
    for feature in list(k.features()):
        for placemark in list(feature.features()):
            geom = placemark.geometry
            polygons.append((placemark.name, shape(geom)))
    return polygons

# 2. Extract GPS + timestamp from image
def get_exif_data(img_path):
    img = Image.open(img_path)
    exif = img._getexif()
    # Parse GPS and timestamp from exif
    # (Requires a helper function to convert GPS to decimal degrees)
    return {'lat': ..., 'lon': ..., 'timestamp': ...}

# 3. Check point in polygons and save if match
polygons = load_kml_polygons("your_areas.kml")
results = []
for img in drone_images:
    exif = get_exif_data(img)
    point = Point(exif['lon'], exif['lat'])
    for name, polygon in polygons:
        if point.within(polygon):
            results.append({
                'image': img,
                'lat': exif['lat'],
                'lon': exif['lon'],
                'timestamp': exif['timestamp'],
                'area': name
            })
pd.DataFrame(results).to_csv('output.csv', index=False)
