from flask import Blueprint, jsonify, render_template

main_bp = Blueprint("main", __name__)

@main_bp.route('/')
@main_bp.route('/index')
def index():
    return render_template("base.html")
