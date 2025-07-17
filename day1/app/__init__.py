from flask import Flask

app = Flask(__name__, static_folder='static')

env = app.config.get("ENV", "production")
if env == "production":
    app.config.from_object("config.DevelopmentConfig")
elif env == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.ProductionConfig")

from app import views
