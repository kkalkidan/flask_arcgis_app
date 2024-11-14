from flask import Blueprint, render_template, jsonify, request
from app.services.arcgis_service import ArcGISService


map_bp = Blueprint('map', __name__)

@map_bp.route('/map')
def show_map():
    """Display the main map page"""
    return render_template('map.html')

@map_bp.route('/buffer', methods=['GET'])  # This becomes /map/buffer
def buffer_point():
    try:
        latitude = float(request.args.get('latitude'))
        longitude = float(request.args.get('longitude'))
        arcgis_service = ArcGISService()
        buffer = arcgis_service.buffer_point(
            latitude=latitude,
            longitude=longitude,
            buffer_distance_meters=1000
        )
        return jsonify(buffer)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
