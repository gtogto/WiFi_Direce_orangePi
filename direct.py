import os
import time

if __name__ == "__main__":
    os.system('sudo killall udhcpd')
    os.system('sudo wpa_cli -i wlan0 terminate -B')
#    os.system('sudo wpa_cli -i p2p-wlan0-0 terminate -B')
    time.sleep(1)
    os.system('echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward')
#    os.system('echo "ctrl_interface=/var/run/wpa_supplicant\nupdate_config=1" | sudo tee /etc/wpa_supplicant.conf')
    os.system('sudo wpa_supplicant -d -Dnl80211 -c /etc/wpa_supplicant.conf -iwlan0 -B')
    os.system('sudo wpa_cli -iwlan0 p2p_group_add')
    os.system('sudo ifconfig p2p-wlan0-0 192.168.1.2')
    os.system('sudo wpa_cli -i p2p-wlan0-0 p2p_find')
    os.system('sudo wpa_cli -ip2p-wlan0-0 p2p_peers')
    os.system('sudo wpa_cli -ip2p-wlan0-0 wps_pbc')
    os.system('sudo udhcpd /etc/udhcpd.conf &')

# socket generation
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(('', 6278))
    server.listen(1)
    print('listen...')
    client, addrClient = server.accept()
    print('connected to ', addrClient)

# socket read
    msg = client.recv(1024)
    while not msg or msg.__eq__('bye'):
        msg = str(msg).split("b'", 1)[1].rsplit("'",1)[0]
        #msg = str(msg).decode("utf-8", "ignore")
        print(msg)
        msg = client.recv(1024)

# close
    client.close()
    server.close()
