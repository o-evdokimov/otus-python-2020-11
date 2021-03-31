from flask import Blueprint, render_template, request

settings_app = Blueprint("settings_app", __name__, url_prefix='/settings')

network_os = ['Junos','Cisco_IOS','Cisco_Nexus','Cisco_XR','Huawei']
context = {'network_os': network_os}

@settings_app.route("/", endpoint='settings', methods=['GET', 'POST'])
def settings():
    print('Settings !!!')
    if request.method == 'POST':
        print('POST')
        form = request.form
        #print((form))
        for k,v in form.items():
            print(f'{k}:{v}')
    return render_template('settings/index.html', title = 'Settings', **context)
