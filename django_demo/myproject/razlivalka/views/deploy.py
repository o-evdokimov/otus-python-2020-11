from django.shortcuts import render
from typing import Dict

# Create your views here.

LOGS = []

def deploy(request):
    my_logs = ''.join(LOGS)
    context: Dict[str, str] = {'title' : "Deploy",
               'my_logs' : my_logs}
    return render(request, 'deploy/index.html', context=context)

