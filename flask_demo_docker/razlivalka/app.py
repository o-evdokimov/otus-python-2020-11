from flask import Flask, redirect, url_for
from views.deploy import deploy_app
from views.settings import settings_app

app = Flask(__name__)
app.register_blueprint(deploy_app)
app.register_blueprint(settings_app)

@app.route('/')
def index():
    return redirect(url_for('deploy_app.deploy', title='deploy'))


