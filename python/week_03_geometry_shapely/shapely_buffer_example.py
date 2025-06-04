"""
Shapely Buffer Example
This script demonstrates basic usage of Shapely for geometry operations
and reads a raster using Rasterio.
"""

from shapely.geometry import Point
import rasterio

# Create a point and a buffer around it
point = Point(100, 200)
buffer = point.buffer(50)  # 50 unit buffer

print("Original Point:", point)
print("Buffered Polygon:", buffer)

# Example raster read (update with a real file path if needed)
raster_path = "data/raw/sample.tif"  # Replace with your actual raster path

try:
    with rasterio.open(raster_path) as src:
        print("Raster CRS:", src.crs)
        print("Raster Bounds:", src.bounds)
except Exception as e:
    print("Raster read failed:", e)
