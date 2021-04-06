from flask import Flask, redirect, url_for
from views.deploy import deploy_app
from views.settings import settings_app
from models.database import db
from flask_migrate import Migrate


app = Flask(__name__)
app.register_blueprint(deploy_app)
app.register_blueprint(settings_app)

app.config.from_object('config.DevelopmentConfig')
db.init_app(app)
mg = Migrate(app, db)


@app.route('/')
def index():
    return redirect(url_for('deploy_app.deploy', title='deploy'))



