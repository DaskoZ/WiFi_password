import os, re, platform
from prettytable import PrettyTable

def get_wifi_pass_lin():
    regx = r'tions\/([\S]+)\..+=([\S]+)'
    out = os.popen('sudo grep psk= /etc/NetworkManager/system-connections/*').read()
    table = PrettyTable(['WiFi-Name', 'WiFi-Password'])
    for name,key in re.findall(regx, out):
        table.add_row([name, key])
    return table

def get_wifi_pass_win():
    out = os.popen('netsh wlan show profile').read().split(':')[2:]

    wifi_name = []
    for i in out:
        idx = i.find('\n')
        wifi_name.append(i[:idx].strip())
    regx = r'Content\s+:\s([\S]+)'
    wifi_pass = []
    for i in wifi_name:
        out = os.popen(f'netsh wlan show profile name= "{i}" key=clear').read()
        wifi_pass.append( re.search(regx, out).group(1) )

    table = PrettyTable(['WiFi-Name', 'WiFi-Password'])
    for i in range(len(wifi_name)):
        table.add_row([wifi_name[i], wifi_pass[i]])

    return table

if __name__ == '__main__':
    if platform.system() == 'Windows':
        with open('./WiFi_passwords.txt', 'a') as f:
            f.write(str(get_wifi_pass_win())+'\n\n')
            
    elif platform.system() == 'Linux':
        with open('./Wifi_passwords.txt', 'a') as f:
            f.write(str(get_wifi_pass_lin())+'\n\n')
    else:
        print('Platform not supported!')