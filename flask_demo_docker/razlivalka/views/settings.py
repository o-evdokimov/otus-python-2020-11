from flask import Blueprint, render_template, request
from models.devices import Device
from models.database import db


settings_app = Blueprint("settings_app", __name__, url_prefix='/settings')

network_os = ['Junos','Cisco_IOS','Cisco_Nexus','Cisco_XR','Huawei']

context = {}
context['network_os'] = network_os

@settings_app.route("/", endpoint='settings', methods=['GET', 'POST'])
def settings():
    global context
    devices_hostnames = []
    print('Settings !!!')
    devices_list = Device.query.order_by(Device.name).all()
    for item in devices_list:
        item : Device
        devices_hostnames.append(item.name)

    context['devices_list'] = devices_hostnames
    if request.method == 'POST':
        print('POST')
        form = request.form
        form_settings  = form.to_dict()
        devices = form_settings.get('settings_devices').split()
        db.session.query(Device).delete()
        for item in devices:
            if not Device.query.filter_by(name=item).first():
                db.session.add(Device(item))
        db.session.commit()

    return render_template('settings/index.html', title = 'Settings', **context)
