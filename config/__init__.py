import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, "../.env"))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev"
    ARCGIS_URL = os.environ.get("ARCGIS_URL")
    ARCGIS_USERNAME = os.environ.get("ARCGIS_USERNAME")
    ARCGIS_PASSWORD = os.environ.get("ARCGIS_PASSWORD")
