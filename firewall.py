from requests import get
import os


def gcpFirewall():
    # Get the current IP address
    ip = get('https://api.ipify.org').text
    print(f'My public IP address is: {ip}')
    knownIPAddr = ""
    os.system('gcloud compute firewall-rules update nc-de-doc-sec2 --source-ranges ' + ip + ',' + knownIPAddr)


gcpFirewall()
