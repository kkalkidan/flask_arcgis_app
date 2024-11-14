from arcgis.gis import GIS
from arcgis.geometry import Point
from arcgis.geometry.functions import buffer

class ArcGISService:
    def __init__(self):
        self.gis = GIS()  # Anonymous access
        
    def buffer_point(self, latitude, longitude, buffer_distance_meters=1000):
        """
        Create a buffer around a point
        
        Args:
            latitude (float): Latitude of the point
            longitude (float): Longitude of the point 
            buffer_distance_meters (float): Buffer distance in meters
            
        Returns:
            dict: Buffer polygon geometry
        """
        # Create a point geometry
        point = Point({
            "x": longitude,
            "y": latitude,
            "spatialReference": {"wkid": 4326}
        })
        
        # Create buffer using the buffer function
        buffer_result = buffer(
            geometries=[point],
            distances=buffer_distance_meters,
            unit=9001,  # Meters
            in_sr=4326,  # WGS84
            out_sr=4326,  # Output in WGS84
            geodesic=True
        )
        
        return buffer_result[0] if buffer_result else None