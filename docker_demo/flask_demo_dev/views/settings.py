from flask import Blueprint, render_template

settings_app = Blueprint("settings_app", __name__, url_prefix='/settings')

network_os = ['Junos','Cisco_IOS','Cisco_Nexus','Cisco_XR','Huawei']
context = {'network_os': network_os}

@settings_app.route("/", endpoint='settings')
def settings():
    return render_template('settings/index.html', title = 'Settings', **context)
