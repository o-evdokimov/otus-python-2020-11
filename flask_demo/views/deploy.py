from typing import Dict

from flask import Blueprint, render_template
from datetime import datetime

deploy_app = Blueprint("deploy_app", __name__, url_prefix='')

LOGS = []

@deploy_app.route("/<string:title>", endpoint='deploy')
def deploy(title):
    my_logs = ''.join(LOGS)
    context: Dict[str, str] = {'title' : title,
               'my_logs' : my_logs}
    return render_template('deploy/index.html', **context)

@deploy_app.context_processor
def utility_processor():
    def run_deploy(title):
        print(f'1: {title}')
        if title=='None':
            print(f'2: {title}')
            deploy_cfg()
    return dict(run_deploy=run_deploy)

def deploy_cfg():
    global LOGS
    logs = """
 ################################
 Host:          jun9
 IP:            10.10.10.9
 Model:         QFX5100-48T-6Q 
 NetworRole:    edge
 OS:            juniper_junos
 Command file:  cmd-juniper_junos
 
 """

    print('run deploy ...')
    LOGS.append(datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S"))
    for item in logs:
        LOGS.append(f'{item}')