import os
import sys
import subprocess
import Kill
import platform
import Version
import Uptime
import Kernel
import Hardware
import Open_file
import AdresseIP
import Interfaces
import Routes
import Forward
import json

User = {
    'Version' : Version.version(1),
    'Uptime' : Uptime.uptime(1),
    'Kernel' : Kernel.kernel(1),
    'Hardware' : Hardware.hardware(1),
    'Open file' : Open_file.open_file(1)
}

Network = {
    'Adresse IP' : AdresseIP.list_command(1),
    'Interfaces' : Interfaces.interface(1),
    'Routes' : Routes.route(1),
    'Forward' : Forward.forward(1)
}
def ToJson(param=None):
    if param == 1:
        with open('user.json','w') as f:
            json.dump(User, f,ensure_ascii=False,indent=4)
    elif param == 2:
        with open('network.json','w',encoding='utf-8') as f:
            json.dump(Network, f,ensure_ascii=False,indent=4)